import factory

from openpersonen.api.demo_models import Persoon
from openpersonen.api.tests.utils import get_bsn, get_a_nummer


a_nummer_generator = get_a_nummer()
bsn_generator = get_bsn()


class PersoonFactory(factory.django.DjangoModelFactory):

    a_nummer_persoon = factory.Sequence(lambda n: next(a_nummer_generator))
    burgerservicenummer_persoon = factory.Sequence(lambda n: next(bsn_generator))
    voornamen_persoon = 'Maykin'
    adellijke_titel_predikaat_persoon = 'Dhr'
    voorvoegsel_geslachtsnaam_persoon = 'van'
    geslachtsnaam_persoon = 'Media'
    geboortedatum_persoon = 20121123
    geboorteplaats_persoon = 1157
    geboorteland_persoon = 6030
    geslachtsaanduiding = 'M'
    vorig_a_nummer = ''
    volgend_a_nummer = ''
    aanduiding_naamgebruik = 'E'
    registergemeente_akte_waaraan_gegevens = 1904
    aktenummer_van_de_akte = '10A1112'
    gemeente_waar_de_gegevens_over_persoon = 518
    datum_van_de_ontlening_van_de_gegevens_over_persoon = 19940310
    beschrijving_van_het_document = 'PKA'
    aanduiding_gegevens_in_onderzoek = 10310
    datum_ingang_onderzoek = 20040204
    datum_einde_onderzoek = 20050305
    indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde = 'O'
    ingangsdatum_geldigheid_met_betrekking = 19961115
    datum_van_opneming_met_betrekking = 19991025
    rni_deelnemer = ''

    class Meta:
        model = Persoon
