import factory

from openpersonen.api.demo_models import Kind
from openpersonen.api.tests.utils import get_bsn, get_a_nummer
from .persoon import PersoonFactory


a_nummer_generator = get_a_nummer()
bsn_generator = get_bsn()


class KindFactory(factory.django.DjangoModelFactory):

    persoon = factory.SubFactory(PersoonFactory)
    a_nummer_kind = factory.Sequence(lambda n: next(a_nummer_generator))
    burgerservicenummer_kind = factory.Sequence(lambda n: next(bsn_generator))
    voornamen_kind = 'Little'
    adellijke_titel_predikaat_kind = 'mvr'
    voorvoegsel_geslachtsnaam_kind = 'de'
    geslachtsnaam_kind = 'Jong'
    geboortedatum_kind = 19990119
    geboorteplaats_kind = 762
    geboorteland_kind = 6030
    registergemeente_akte_waaraan_gegevens_over_kind_ontleend_zijn = 530
    aktenummer_van_de_akte_waaraan_gegevens_over_kind_ontleend_zijn = '1AA0015'
    gemeente_waar_de_gegevens_over_kind = 762
    datum_van_de_ontlening_van_de_gegevens_over_kind = 20000221
    beschrijving_van_het_document = 'PK'
    aanduiding_gegevens_in_onderzoek = 90220
    datum_ingang_onderzoek = 19930910
    datum_einde_onderzoek = 19940715
    indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde = 'O'
    ingangsdatum_geldigheid_met_betrekking = 19971201
    datum_van_opneming_met_betrekking = 19930315
    registratie_betrekking = 20090101

    class Meta:
        model = Kind
