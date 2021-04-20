import factory

from .models import GemeenteCodeAndOmschrijving


class GemeenteCodeAndOmschrijvingFactory(factory.django.DjangoModelFactory):
    code = 624
    omschrijving = "Amsterdam"

    class Meta:
        model = GemeenteCodeAndOmschrijving
