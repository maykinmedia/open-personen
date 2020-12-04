import factory

from .models import RedenCodeAndOmschrijving


class RedenCodeAndOmschrijvingFactory(factory.django.DjangoModelFactory):
    code = "A"
    omschrijving = (
        "Vermissing van een persoon gevolgd door ander huwelijk/geregistr. partnerschap"
    )

    class Meta:
        model = RedenCodeAndOmschrijving
