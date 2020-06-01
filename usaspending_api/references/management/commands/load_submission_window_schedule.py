from django.core.management.base import BaseCommand

SQL = ""


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("hi")
