getSocket = function(thread_id) {
    var socket = new WebSocket('ws://wwars.my/' + thread_id + '/');
    socket.onmessage = function(event) {
        $('#message').html(event.data);
    }
    return socket;
}
