import factory

from openpersonen.api.demo_models import Nationaliteit

from .persoon import PersoonFactory


class NationaliteitFactory(factory.django.DjangoModelFactory):

    persoon = factory.SubFactory(PersoonFactory)
    nationaliteit = 1
    reden_opname_nationaliteit = 1
    reden_beeindigen_nationaliteit = 401
    aanduiding_bijzonder_nederlanderschap = "V"
    eu_persoonsummer = 90120113511
    gemeente_waar_de_gegevens_over_nationaliteit = 599
    datum_van_de_ontlening = 19940310
    beschrijving_van_het_document = "PK"
    aanduiding_gegevens_in_onderzoek = 40000
    datum_ingang_onderzoek = 20100822
    datum_einde_onderzoek = 20200923
    indicatie_onjuist = "O"
    datum_van_ingang_geldigheid_met_betrekking = 19580706
    datum_van_opneming_met_betrekking = 19940930
    rni_deelnemer = 201
    omschrijving_verdrag = ""

    class Meta:
        model = Nationaliteit
