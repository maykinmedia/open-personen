import factory

from openpersonen.accounts.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
