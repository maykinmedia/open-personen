from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from rest_framework.authtoken.models import Token

User = get_user_model()


class Command(BaseCommand):
    help = "Create or get an API Token"

    def add_arguments(self, parser):
        parser.add_argument(
            "--noinput",
            "--no-input",
            action="store_false",
            dest="interactive",
            help="Do NOT prompt the user for input of any kind.",
        )

        parser.add_argument("username", type=str)

    def handle(self, *args, **options):
        interactive = options["interactive"]
        username = options["username"]
        user, _ = User.objects.get_or_create(username=username)

        user_has_token = Token.objects.filter(user=user).exists()

        if (
            user_has_token
            and interactive
            and input(f"Replace existing token for {username}? [yes/no] ") != "yes"
        ):
            token = Token.objects.get(user=user)
        else:
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)

        self.stdout.write(f"API token: {token.key}")
