from rest_framework import serializers

from .datum import DatumSerializer


class InOnderzoekSerializer(serializers.Serializer):
    geslachtsnaam = serializers.BooleanField()
    voornamen = serializers.BooleanField()
    voorvoegsel = serializers.BooleanField()
    datumIngangOnderzoek = DatumSerializer()


class NationaliteitInOnderzoekSerializer(serializers):
    aanduidingBijzonderNederlanderschap = serializers.BooleanField()
    nationaliteit = serializers.BooleanField()
    redenOpname = serializers.BooleanField()
    datumIngangOnderzoek = DatumSerializer()


class DatumInOnderzoekSerializer(serializers):
    datum = serializers.BooleanField()
    land = serializers.BooleanField()
    plaats = serializers.BooleanField()
    datumIngangOnderzoek = DatumSerializer()


class VerblijfPlaatsInOnderzoekSerializer(serializers):
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


class GezagsVerhoudingInOnderzoekSerializer(serializers):
    indicatieCurateleRegister = serializers.BooleanField()
    indicatieGezagMinderjarige = serializers.BooleanField()
    datumIngangOnderzoek = DatumSerializer()


class VerblijfsTitelInOnderzoekSerializer(serializers):
    aanduiding = serializers.BooleanField()
    datumEinde = serializers.BooleanField()
    datumIngang = serializers.BooleanField()
    datumIngangOnderzoek = DatumSerializer()
