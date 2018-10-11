from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="dbadmin").exists():
            User.objects.create_superuser("dbadmin", "ebarq11@gmail.com", "Ebarq2018!!")
