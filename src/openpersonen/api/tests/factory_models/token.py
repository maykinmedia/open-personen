import factory
from rest_framework.authtoken.models import Token

from .user import UserFactory


class TokenFactory(factory.django.DjangoModelFactory):

    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Token
