from twisted_server import run

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        run()
