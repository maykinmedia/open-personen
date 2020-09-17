import factory

from openpersonen.api.demo_models import Overlijden

from .persoon import PersoonFactory


class OverlijdenFactory(factory.django.DjangoModelFactory):

    persoon = factory.SubFactory(PersoonFactory)
    datum_overlijden = 20141010
    plaats_overlijden = 599
    land_overlijden = 6030
    registergemeente_akte_waaraan_gegevens = 599
    aktenummer_van_de_akte_waaraan_gegevens = "20A1564"
    gemeente_waar_de_gegevens_over_overlijden = 0
    datum_van_de_ontlening_van_de_gegevens_over_overlijden = 0
    beschrijving_van_het_document_waaraan_de_gegevens = "Verkeerde JV"
    aanduiding_gegevens_in_onderzoek = 60000
    datum_ingang_onderzoek = 20151112
    datum_einde_onderzoek = 20151213
    indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde = "O"
    ingangsdatum_geldigheid_met_betrekking = 20161214
    datum_van_opneming_met_betrekking = 20161218
    rni_deelnemer = 202

    class Meta:
        model = Overlijden
