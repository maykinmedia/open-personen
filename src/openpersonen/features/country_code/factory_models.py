import factory

from .models import CountryCode


class CountryCodeFactory(factory.django.DjangoModelFactory):
    code = 6030
    omschrijving = "Nederland"

    class Meta:
        model = CountryCode
