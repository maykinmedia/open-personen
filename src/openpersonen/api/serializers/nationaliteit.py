from rest_framework import serializers

from .codeenomschrijving import CodeEnOmschrijvingSerializer
from .datum import DatumSerializer
from .inonderzoek import NationaliteitInOnderzoekSerializer


class NationaliteitSerializer(serializers.Serializer):
    aanduidingBijzonderNederlanderschap = serializers.CharField(required=False)
    datumIngangGeldigheid = DatumSerializer(required=False)
    nationaliteit = CodeEnOmschrijvingSerializer(required=False)
    redenOpname = CodeEnOmschrijvingSerializer(required=False)
    inOnderzoek = NationaliteitInOnderzoekSerializer(required=False)
