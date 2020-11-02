from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from rest_framework.authtoken.models import Token

User = get_user_model()


class Command(BaseCommand):
    help = "Create an API Token"

    def add_arguments(self, parser):
        parser.add_argument("username", type=str)

    def handle(self, *args, **options):
        user, _ = User.objects.get_or_create(username=options["username"])
        Token.objects.filter(user=user).delete()
        self.stdout.write(f"Generated token: {Token.objects.create(user=user).key}")
