import factory

from .models import GemeenteCodeAndOmschrijving


class GemeenteCodeAndOmschrijvingFactory(factory.django.DjangoModelFactory):
    code = 624
    omschrijving = "Voorburg"

    class Meta:
        model = GemeenteCodeAndOmschrijving
