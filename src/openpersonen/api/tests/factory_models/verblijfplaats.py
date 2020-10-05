import factory

from openpersonen.contrib.demo.models import Verblijfplaats

from .persoon import PersoonFactory


class VerblijfplaatsFactory(factory.django.DjangoModelFactory):

    persoon = factory.SubFactory(PersoonFactory)
    gemeente_van_inschrijving = 599
    datum_inschrijving_in_de_gemeente = 20131102
    functie_adres = "W"
    gemeentedeel = "Oud-Zuid"
    datum_aanvang_adreshouding = 20150808
    straatnaam = "Boterdiep"
    naam_openbare_ruimte = "Boterdiep"
    huisnummer = 31
    huisletter = "c"
    huisnummertoevoeging = "III"
    aanduiding_bij_huisnummer = "by"
    postcode = "3077AW"
    woonplaatsnaam = "Rotterdam"
    identificatiecode_verblijfplaats = "0599010000208579"
    identificatiecode_nummeraanduiding = "0599200000219678"
    locatiebeschrijving = "1e Exloermond t/o de molen"
    land_adres_buitenland = 5010
    datum_aanvang_adres_buitenland = 20140702
    regel_1_adres_buitenland = "Rue du pomme 25"
    regel_2_adres_buitenland = "Bruxelles"
    regel_3_adres_buitenland = "Anasari and Ghissassudin Watt"
    land_vanwaar_ingeschreven = 5002
    datum_vestiging_in_nederland = 20131102
    omschrijving_van_de_aangifte_adreshouding = "I"
    indicatie_document = ""
    aanduiding_gegevens_in_onderzoek = 581100
    datum_ingang_onderzoek = 19920102
    datum_einde_onderzoek = 19920102
    indicatie_onjuist = "O"
    ingangsdatum_geldigheid_met_betrekking = 19980401
    datum_van_opneming_met_betrekking = 19980401
    rni_deelnemer = ""
    omschrijving_verdrag = ""

    class Meta:
        model = Verblijfplaats
