import factory

from openpersonen.api.demo_models import Kiesrecht
from .persoon import PersoonFactory


class KiesrechtFactory(factory.django.DjangoModelFactory):

    persoon = factory.SubFactory(PersoonFactory)
    aanduiding_europees_kiesrecht = 1
    datum_verzoek_of_mededeling_europees_kiesrecht = 20041020
    einddatum_uitsluiting_europees_kiesrecht = 20070101
    aanduiding_uitgesloten_kiesrecht = 'A'
    einddatum_uitsluiting_kiesrecht = 20090204
    gemeente_waar_de_gegevens_over_kiesrecht = 599
    datum_van_de_ontlening_van_de_gegevens_over_kiesrecht = 20110514
    beschrijving_van_het_document = 'Gerechtelijke uitspraak'

    class Meta:
        model = Kiesrecht
