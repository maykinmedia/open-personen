from rest_framework import serializers

from .codeenomschrijving import CodeEnOmschrijvingSerializer
from .datum import DatumSerializer
from .inonderzoek import VerblijfPlaatsInOnderzoekSerializer
from .verblijfbuitenland import VerblijfBuitenlandSerializer


class VerblijfPlaatsSerializer(serializers.Serializer):
    functieAdres = serializers.CharField()
    huisletter = serializers.CharField()
    huisnummer = serializers.IntegerField()
    huisnummertoevoeging = serializers.CharField()
    aanduidingBijHuisnummer = serializers.CharField()
    identificatiecodeNummeraanduiding = serializers.CharField()
    naamOpenbareRuimte = serializers.CharField()
    postcode = serializers.CharField()
    woonplaatsnaam = serializers.CharField()
    identificatiecodeAdresseerbaarObject = serializers.CharField()
    indicatieVestigingVanuitBuitenland = serializers.BooleanField()
    locatiebeschrijving = serializers.CharField()
    straatnaam = serializers.CharField()
    vanuitVertrokkenOnbekendWaarheen = serializers.CharField()
    datumAanvangAdreshouding = DatumSerializer()
    datumIngangGeldigheid = DatumSerializer()
    datumInschrijvingInGemeente = DatumSerializer()
    datumVestigingInNederland = DatumSerializer()
    gemeenteVanInschrijving = CodeEnOmschrijvingSerializer()
    landVanwaarIngeschreven = CodeEnOmschrijvingSerializer()
    verblijfBuitenland = VerblijfBuitenlandSerializer()
    inOnderzoek = VerblijfPlaatsInOnderzoekSerializer()
