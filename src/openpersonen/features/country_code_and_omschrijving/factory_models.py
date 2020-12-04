import factory

from .models import CountryCodeAndOmschrijving


class CountryCodeAndOmschrijvingFactory(factory.django.DjangoModelFactory):
    code = 6030
    omschrijving = "Nederland"

    class Meta:
        model = CountryCodeAndOmschrijving
