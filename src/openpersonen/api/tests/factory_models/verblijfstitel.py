import factory

from openpersonen.contrib.demo.models import Verblijfstitel

from .persoon import PersoonFactory


class VerblijfstitelFactory(factory.django.DjangoModelFactory):

    persoon = factory.SubFactory(PersoonFactory)
    aanduiding_verblijfstitel = 21
    datum_einde_verblijfstitel = 20150530
    ingangsdatum_verblijfstitel = 20100530
    aanduiding_gegevens_in_onderzoek = 100000
    datum_ingang_onderzoek = 19951205
    datum_einde_onderzoek = 19951207
    indicatie_onjuist = "O"
    ingangsdatum_geldigheid_met_betrekking = 20110130
    datum_van_opneming_met_betrekking = 20110131

    class Meta:
        model = Verblijfstitel
