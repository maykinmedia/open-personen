import factory

from openpersonen.api.demo_models import Reisdocument

from .persoon import PersoonFactory


class ReisdocumentFactory(factory.django.DjangoModelFactory):

    persoon = factory.SubFactory(PersoonFactory)
    soort_nederlands_reisdocument = "PN"
    nummer_nederlands_reisdocument = "IVJ854032"
    datum_uitgifte_nederlands_reisdocument = 20090227
    autoriteit_van_afgifte_nederlands_reisdocument = "B0599"
    datum_einde_geldigheid_nederlands_reisdocument = 20110128
    datum_inhouding_dan_wel_vermissing_nederlands_reisdocument = 20110128
    aanduiding_inhouding_dan_wel_vermissing_nederlands_reisdocument = "I"
    signalering_met_betrekking = 1
    gemeente_waar_het_paspoortdossier_zich_bevindt = 599
    datum_van_opname_in_het_paspoortdossier = 20200212
    beschrijving_dossier = "Aanvraagformulier reisdocument"
    aanduiding_gegevens_in_onderzoek = ""
    datum_ingang_onderzoek = ""
    datum_einde_onderzoek = ""
    datum_van_ingang_geldigheid_met_betrekking = 20200306
    datum_van_opneming_met_betrekking = 20200306

    class Meta:
        model = Reisdocument
