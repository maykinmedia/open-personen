import factory

from openpersonen.accounts.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        instance = super()._create(model_class, *args, **kwargs)

        instance.set_password(kwargs.get("password", "secret"))
        instance.save()

        return instance
