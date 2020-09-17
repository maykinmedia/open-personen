import factory

from openpersonen.api.demo_models import Ouder
from openpersonen.api.tests.utils import get_a_nummer, get_bsn

from .persoon import PersoonFactory

a_nummer_generator = get_a_nummer()
bsn_generator = get_bsn()


class OuderFactory(factory.django.DjangoModelFactory):

    persoon = factory.SubFactory(PersoonFactory)
    a_nummer_ouder = factory.Sequence(lambda n: next(a_nummer_generator))
    burgerservicenummer_ouder = factory.Sequence(lambda n: next(bsn_generator))
    voornamen_ouder = "Groot"
    adellijke_titel_predikaat_ouder = "dhr"
    voorvoegsel_geslachtsnaam_ouder = "van"
    geslachtsnaam_ouder = "Oud"
    geboortedatum_ouder = 19481215
    geboorteplaats_ouder = 1265
    geboorteland_ouder = 6030
    geslachtsaanduiding_ouder = "V"
    datum_ingang_familierechtelijke_betrekking_ouder = 19590417
    registergemeente_akte_waaraan_gegevens_over_ouder_ontleend_zijn = 518
    aktenummer_van_de_akte_waaraan_gegevens = "1AA0007"
    gemeente_waar_de_gegevens_over_ouder = 599
    datum_van_de_ontlening_van_de_gegevens_over_ouder = 19940310
    beschrijving_van_het_document_waaraan_de_gegevens = "PK"
    aanduiding_gegevens_in_onderzoek = 22000
    datum_ingang_onderzoek = 19960510
    datum_einde_onderzoek = 19960615
    indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde = "O"
    ingangsdatum_geldigheid_met_betrekking = 19950515
    datum_van_opneming_met_betrekking = 19950516

    class Meta:
        model = Ouder
