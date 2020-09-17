import factory

from openpersonen.api.demo_models import Gezagsverhouding

from .persoon import PersoonFactory


class GezagsVerhoudingFactory(factory.django.DjangoModelFactory):

    persoon = factory.SubFactory(PersoonFactory)
    indicatie_gezag_minderjarige = 12
    indicatie_curateleregister = 1
    gemeente_waar_de_gegevens_over_gezagsverhouding = 1811
    datum_van_de_ontlening_van_de_gegevens_over_gezagsverhouding = 20110215
    beschrijving_van_het_document = "Kennisgeving curateleregister"
    aanduiding_gegevens_in_onderzoek = ""
    datum_ingang_onderzoek = 20140525
    datum_einde_onderzoek = 20161027
    indicatie_onjuist = "O"
    ingangsdatum_geldigheid_met_betrekking = 20130919
    datum_van_opneming_met_betrekking = 20131021

    class Meta:
        model = Gezagsverhouding
