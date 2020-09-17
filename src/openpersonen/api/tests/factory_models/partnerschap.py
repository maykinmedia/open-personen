import factory

from openpersonen.api.demo_models import Partnerschap
from openpersonen.api.tests.utils import get_a_nummer, get_bsn

from .persoon import PersoonFactory

a_nummer_generator = get_a_nummer()
bsn_generator = get_bsn()


class PartnerschapFactory(factory.django.DjangoModelFactory):

    persoon = factory.SubFactory(PersoonFactory)
    a_nummer_echtgenoot_geregistreerd_partner = factory.Sequence(
        lambda n: next(a_nummer_generator)
    )
    burgerservicenummer_echtgenoot_geregistreerd_partner = factory.Sequence(
        lambda n: next(bsn_generator)
    )
    voornamen_echtgenoot_geregistreerd_partner = "Partner"
    adellijke_titel_predikaat_echtgenoot_geregistreerd_partner = "mvr"
    voorvoegsel_geslachtsnaam_echtgenoot_geregistreerd_partner = "den"
    geslachtsnaam_echtgenoot_geregistreerd_partner = "MaykinMedia"
    geboortedatum_echtgenoot_geregistreerd_partner = 19500101
    geboorteplaats_echtgenoot_geregistreerd_partner = 947
    geboorteland_echtgenoot_geregistreerd_partner = 5007
    geslachtsaanduiding_echtgenoot_geregistreerd_partner = "V"
    datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap = 20050819
    plaats_huwelijkssluiting_aangaan_geregistreerd_partnerschap = 772
    land_huwelijkssluiting_aangaan_geregistreerd_partnerschap = 6030
    datum_ontbinding_huwelijk_geregistreerd_partnerschap = 20000308
    plaats_ontbinding_huwelijk_geregistreerd_partnerschap = 518
    land_ontbinding_huwelijk_geregistreerd_partnerschap = 6030
    reden_ontbinding_huwelijk_geregistreerd_partnerschap = "S"
    soort_verbintenis = "P"
    registergemeente_akte_waaraan_gegevens = 518
    aktenummer_van_de_akte_waaraan_gegevens = "5 B0040"
    gemeente_waar_de_gegevens_over_huwelijk = 599
    datum_van_de_ontlening_van_de_gegevens = 19940930
    beschrijving_van_het_document_waaraan_de_gegevens = "PK"
    aanduiding_gegevens_in_onderzoek = 550000
    datum_ingang_onderzoek = 19970228
    datum_einde_onderzoek = 20000228
    indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde = "O"
    ingangsdatum_geldigheid_met_betrekking = 19980628
    datum_van_opneming_met_betrekking = 20010628

    class Meta:
        model = Partnerschap
