from twisted.internet import reactor, protocol as twisted_protocol, defer
from txsockjs.factory import SockJSFactory

from pika import ConnectionParameters, PlainCredentials
from pika.adapters.twisted_connection import TwistedProtocolConnection

from twisted.python import log

from django.conf import settings


class AmqpSubProtocol(TwistedProtocolConnection):
    def __init__(self, host, port,
                 user, password, vhost):
        parameters = ConnectionParameters(
            credentials=PlainCredentials(user, password),
            host=host,
            port=port,
            virtual_host=vhost,
            heartbeat_interval=30,
        )
        super(AmqpSubProtocol, self).__init__(parameters)
        self.on_handshaking_made = defer.Deferred()

    def connectionMade(self):
        super(AmqpSubProtocol, self).connectionMade()
        self.ready.addCallback(lambda _: self.handshakingMade())
        self.ready.addErrback(self.handshakingFailed)

    def queueDeclare(self, channel):
        channel.queue_declare(queue='thread')

    @defer.inlineCallbacks
    def handshakingMade(self):
        self.channel = yield self.channel()
        yield self.queueDeclare(self.channel)

    def handshakingFailed(self, failure):
        log.err(failure)
        self.transport.loseConnection()

    def consumeFrom(self, callback, queue):
        self.channel = yield self.channel()
        self.channel.basic_consume(callback, queue=queue)


class AmqpSubFactory(twisted_protocol.ReconnectingClientFactory):
    protocol = AmqpSubProtocol

    def __init__(self, **credentials):
        self._host = credentials['host']
        self._port = credentials['port']
        self._user = credentials['user']
        self._password = credentials['password']
        self._vhost = credentials['vhost']

    def buildProtocol(self, addr):
        self.proto = self.protocol(
            self._host, self._port,
            self._user, self._password,
            self._vhost
        )

        self.proto.factory = self
        self.resetDelay()

        return self.proto


class MainRoomProtocol(twisted_protocol.Protocol):
    addr = None

    def __init__(self, addr):
        self.addr = addr

    def connectionMade(self):
        print("Connection Made!")
        print dir(self.factory)
        print self.factory.sockets

    def send(self, channel, message):
        self.transport.write(message)

    def done(self, *args):
        reactor.callLater(1, self.transport.loseConnection)

    def connectionLost(self, reason=None):
        pass

    def dataReceived(self, data):
        pass


class MainRoomFactory(twisted_protocol.Factory):
    protocol = MainRoomProtocol
    sockets = {}
    amqp = None

    def __init__(self):
        factory = AmqpSubFactory(**settings.AMQPS['default'])
        reactor.connectTCP('localhost', 5672, factory)
        self.amqp = factory.buildProtocol(None)
        self.amqp.consumeFrom(self.callback, 'thread')

    def callback(self, ch, method, properties, body):
        print 'in callback'

    def buildProtocol(self, addr):
        ws_protocol = self.protocol(addr)
        ws_protocol.factory = self
        self.sockets[addr] = ws_protocol
        return ws_protocol


def run():
    reactor.listenTCP(8001, SockJSFactory(MainRoomFactory()))
    reactor.run()
