from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="ebarq-admin").exists():
            User.objects.create_superuser("ebarq-admin", "ebarq11@gmail.com", "ebarq-admin")
