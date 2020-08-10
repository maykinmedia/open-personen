from rest_framework import serializers

from .codeenomschrijving import CodeEnOmschrijvingSerializer
from .datum import DatumSerializer
from .inonderzoek import VerblijfPlaatsInOnderzoekSerializer
from .verblijfbuitenland import VerblijfBuitenlandSerializer
from openpersonen.api.enum.functie_adres import FunctieAdresChoices
from ..enum.aanduiding_bij_huisnummer import AanduidginBijHuisnummerChoices


class VerblijfPlaatsSerializer(serializers.Serializer):
    functieAdres = serializers.ChoiceField(choices=FunctieAdresChoices.choices, required=False)
    huisletter = serializers.RegexField('^[A-Z,a-z]$', max_length=1, required=False)
    huisnummer = serializers.IntegerField(max_value=99999, required=False)
    huisnummertoevoeging = serializers.RegexField('^[a-zA-Z0-9]{1,4}$', max_length=4, required=False)
    aanduidingBijHuisnummer = serializers.ChoiceField(choices=AanduidginBijHuisnummerChoices.choices, required=False)
    identificatiecodeNummeraanduiding = serializers.CharField(max_length=16, required=False)
    naamOpenbareRuimte = serializers.CharField(max_length=80, required=False)
    postcode = serializers.RegexField('^[1-9]{1}[0-9]{3}[A-Z]{2}$', required=False)
    woonplaatsnaam = serializers.CharField(max_length=80, required=False)
    identificatiecodeAdresseerbaarObject = serializers.CharField(max_length=16, required=False)
    indicatieVestigingVanuitBuitenland = serializers.BooleanField(required=False)
    locatiebeschrijving = serializers.CharField(max_length=35, required=False)
    straatnaam = serializers.CharField(max_length=24, required=False)
    vanuitVertrokkenOnbekendWaarheen = serializers.CharField(required=False)
    datumAanvangAdreshouding = DatumSerializer(required=False)
    datumIngangGeldigheid = DatumSerializer(required=False)
    datumInschrijvingInGemeente = DatumSerializer(required=False)
    datumVestigingInNederland = DatumSerializer(required=False)
    gemeenteVanInschrijving = CodeEnOmschrijvingSerializer(required=False)
    landVanwaarIngeschreven = CodeEnOmschrijvingSerializer(required=False)
    verblijfBuitenland = VerblijfBuitenlandSerializer(required=False)
    inOnderzoek = VerblijfPlaatsInOnderzoekSerializer(required=False)
