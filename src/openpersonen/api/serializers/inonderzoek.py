from rest_framework import serializers

from .datum import DatumSerializer


class NaamInOnderzoekSerializer(serializers.Serializer):
    geslachtsnaam = serializers.BooleanField()
    voornamen = serializers.BooleanField()
    voorvoegsel = serializers.BooleanField()
    datumIngangOnderzoek = DatumSerializer()


class IngeschrevenPersoonInOnderzoekSerializer(serializers.Serializer):
    burgerservicenummer = serializers.BooleanField()
    geslachtsaanduiding = serializers.BooleanField()
    datumIngangOnderzoek = DatumSerializer()


class NationaliteitInOnderzoekSerializer(serializers.Serializer):
    aanduidingBijzonderNederlanderschap = serializers.BooleanField()
    nationaliteit = serializers.BooleanField()
    redenOpname = serializers.BooleanField()
    datumIngangOnderzoek = DatumSerializer()


class DatumInOnderzoekSerializer(serializers.Serializer):
    datum = serializers.BooleanField()
    land = serializers.BooleanField()
    plaats = serializers.BooleanField()
    datumIngangOnderzoek = DatumSerializer()


class VerblijfPlaatsInOnderzoekSerializer(serializers.Serializer):
    aanduidingBijHuisnummer = serializers.BooleanField()
    datumAanvangAdreshouding = serializers.BooleanField()
    datumIngangGeldigheid = serializers.BooleanField()
    datumInschrijvingInGemeente = serializers.BooleanField()
    datumVestigingInNederland = serializers.BooleanField()
    functieAdres = serializers.BooleanField()
    gemeenteVanInschrijving = serializers.BooleanField()
    huisletter = serializers.BooleanField()
    huisnummer = serializers.BooleanField()
    huisnummertoevoeging = serializers.BooleanField()
    identificatiecodeNummeraanduiding = serializers.BooleanField()
    identificatiecodeAdresseerbaarObject = serializers.BooleanField()
    landVanwaarIngeschreven = serializers.BooleanField()
    locatiebeschrijving = serializers.BooleanField()
    naamOpenbareRuimte = serializers.BooleanField()
    postcode = serializers.BooleanField()
    straatnaam = serializers.BooleanField()
    verblijfBuitenland = serializers.BooleanField()
    woonplaatsnaam = serializers.BooleanField()
    datumIngangOnderzoek = DatumSerializer()


class GezagsVerhoudingInOnderzoekSerializer(serializers.Serializer):
    indicatieCurateleRegister = serializers.BooleanField()
    indicatieGezagMinderjarige = serializers.BooleanField()
    datumIngangOnderzoek = DatumSerializer()


class VerblijfsTitelInOnderzoekSerializer(serializers.Serializer):
    aanduiding = serializers.BooleanField()
    datumEinde = serializers.BooleanField()
    datumIngang = serializers.BooleanField()
    datumIngangOnderzoek = DatumSerializer()


class OuderInOnderzoekSerializer(serializers.Serializer):
    burgerservicenummer = serializers.BooleanField()
    datumIngangFamilierechtelijkeBetrekking = serializers.BooleanField()
    geslachtsaanduiding = serializers.BooleanField()
    datumIngangOnderzoek = DatumSerializer()


class KinderInOnderzoek(serializers.Serializer):
    burgerservicenummer = serializers.BooleanField()
    datumIngangOnderzoek = DatumSerializer()


class PartnerInOnderzoek(serializers.Serializer):
    burgerservicenummer = serializers.BooleanField()
    geslachtsaanduiding = serializers.BooleanField()
    soortVerbintenis = serializers.BooleanField()
    datumIngangOnderzoek = DatumSerializer()
