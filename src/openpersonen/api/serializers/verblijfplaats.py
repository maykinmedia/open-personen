from rest_framework import serializers

from .codeenomschrijving import CodeEnOmschrijvingSerializer
from .datum import DatumSerializer
from .inonderzoek import VerblijfPlaatsInOnderzoekSerializer
from .verblijfbuitenland import VerblijfBuitenlandSerializer


class VerblijfPlaatsSerializer(serializers.Serializer):
    functieAdres = serializers.CharField(required=False)
    huisletter = serializers.CharField(required=False)
    huisnummer = serializers.IntegerField(required=False)
    huisnummertoevoeging = serializers.CharField(required=False)
    aanduidingBijHuisnummer = serializers.CharField(required=False)
    identificatiecodeNummeraanduiding = serializers.CharField(required=False)
    naamOpenbareRuimte = serializers.CharField(required=False)
    postcode = serializers.CharField(required=False)
    woonplaatsnaam = serializers.CharField(required=False)
    identificatiecodeAdresseerbaarObject = serializers.CharField(required=False)
    indicatieVestigingVanuitBuitenland = serializers.BooleanField(required=False)
    locatiebeschrijving = serializers.CharField(required=False)
    straatnaam = serializers.CharField(required=False)
    vanuitVertrokkenOnbekendWaarheen = serializers.CharField(required=False)
    datumAanvangAdreshouding = DatumSerializer(required=False)
    datumIngangGeldigheid = DatumSerializer(required=False)
    datumInschrijvingInGemeente = DatumSerializer(required=False)
    datumVestigingInNederland = DatumSerializer(required=False)
    gemeenteVanInschrijving = CodeEnOmschrijvingSerializer(required=False)
    landVanwaarIngeschreven = CodeEnOmschrijvingSerializer(required=False)
    verblijfBuitenland = VerblijfBuitenlandSerializer(required=False)
    inOnderzoek = VerblijfPlaatsInOnderzoekSerializer(required=False)
