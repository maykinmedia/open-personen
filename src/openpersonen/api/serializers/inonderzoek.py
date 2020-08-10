from rest_framework import serializers

from .datum import DatumSerializer


class NaamInOnderzoekSerializer(serializers.Serializer):
    geslachtsnaam = serializers.BooleanField(required=False)
    voornamen = serializers.BooleanField(required=False)
    voorvoegsel = serializers.BooleanField(required=False)
    datum_ingang_onderzoek = DatumSerializer(label='datumIngangOnderzoek', required=False)


class IngeschrevenPersoonInOnderzoekSerializer(serializers.Serializer):
    burgerservicenummer = serializers.BooleanField(required=False)
    geslachtsaanduiding = serializers.BooleanField(required=False)
    datum_ingang_onderzoek = DatumSerializer(label='datumIngangOnderzoek', required=False)


class NationaliteitInOnderzoekSerializer(serializers.Serializer):
    aanduidingBijzonderNederlanderschap = serializers.BooleanField(required=False)
    nationaliteit = serializers.BooleanField(required=False)
    redenOpname = serializers.BooleanField(required=False)
    datum_ingang_onderzoek = DatumSerializer(label='datumIngangOnderzoek', required=False)


class DatumInOnderzoekSerializer(serializers.Serializer):
    datum = serializers.BooleanField(required=False)
    land = serializers.BooleanField(required=False)
    plaats = serializers.BooleanField(required=False)
    datum_ingang_onderzoek = DatumSerializer(label='datumIngangOnderzoek', required=False)


class VerblijfPlaatsInOnderzoekSerializer(serializers.Serializer):
    aanduidingBijHuisnummer = serializers.BooleanField(required=False)
    datumAanvangAdreshouding = serializers.BooleanField(required=False)
    datumIngangGeldigheid = serializers.BooleanField(required=False)
    datumInschrijvingInGemeente = serializers.BooleanField(required=False)
    datumVestigingInNederland = serializers.BooleanField(required=False)
    functieAdres = serializers.BooleanField(required=False)
    gemeenteVanInschrijving = serializers.BooleanField(required=False)
    huisletter = serializers.BooleanField(required=False)
    huisnummer = serializers.BooleanField(required=False)
    huisnummertoevoeging = serializers.BooleanField(required=False)
    identificatiecodeNummeraanduiding = serializers.BooleanField(required=False)
    identificatiecodeAdresseerbaarObject = serializers.BooleanField(required=False)
    landVanwaarIngeschreven = serializers.BooleanField(required=False)
    locatiebeschrijving = serializers.BooleanField(required=False)
    naamOpenbareRuimte = serializers.BooleanField(required=False)
    postcode = serializers.BooleanField(required=False)
    straatnaam = serializers.BooleanField(required=False)
    verblijfBuitenland = serializers.BooleanField(required=False)
    woonplaatsnaam = serializers.BooleanField(required=False)
    datum_ingang_onderzoek = DatumSerializer(label='datumIngangOnderzoek', required=False)


class GezagsVerhoudingInOnderzoekSerializer(serializers.Serializer):
    indicatieCurateleRegister = serializers.BooleanField(required=False)
    indicatieGezagMinderjarige = serializers.BooleanField(required=False)
    datum_ingang_onderzoek = DatumSerializer(label='datumIngangOnderzoek', required=False)


class VerblijfsTitelInOnderzoekSerializer(serializers.Serializer):
    aanduiding = serializers.BooleanField(required=False)
    datumEinde = serializers.BooleanField(required=False)
    datumIngang = serializers.BooleanField(required=False)
    datum_ingang_onderzoek = DatumSerializer(label='datumIngangOnderzoek', required=False)


class OuderInOnderzoekSerializer(serializers.Serializer):
    burgerservicenummer = serializers.BooleanField(required=False)
    datumIngangFamilierechtelijkeBetrekking = serializers.BooleanField(required=False)
    geslachtsaanduiding = serializers.BooleanField(required=False)
    datum_ingang_onderzoek = DatumSerializer(label='datumIngangOnderzoek', required=False)


class KinderInOnderzoek(serializers.Serializer):
    burgerservicenummer = serializers.BooleanField(required=False)
    datum_ingang_onderzoek = DatumSerializer(label='datumIngangOnderzoek', required=False)


class PartnerInOnderzoek(serializers.Serializer):
    burgerservicenummer = serializers.BooleanField(required=False)
    geslachtsaanduiding = serializers.BooleanField(required=False)
    soortVerbintenis = serializers.BooleanField(required=False)
    datum_ingang_onderzoek = DatumSerializer(label='datumIngangOnderzoek', required=False)
