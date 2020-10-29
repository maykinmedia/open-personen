import uuid

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from rest_framework.authtoken.models import Token


User = get_user_model()


class Command(BaseCommand):
    help = 'Create an API Token'

    def handle(self, *args, **options):
        user = User.objects.create(username=uuid.uuid4())
        self.stdout.write(f'Generated token: {Token.objects.create(user=user).key}')
