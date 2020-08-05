from rest_framework import serializers

from .codeenomschrijving import CodeEnOmschrijvingSerializer
from .datum import DatumSerializer
from .inonderzoek import NationaliteitInOnderzoekSerializer


class NationaliteitSerializer(serializers.Serializer):
    aanduidingBijzonderNederlanderschap = serializers.CharField()
    datumIngangGeldigheid = DatumSerializer()
    nationaliteit = CodeEnOmschrijvingSerializer()
    redenOpname = CodeEnOmschrijvingSerializer()
    inOnderzoek = NationaliteitInOnderzoekSerializer()
