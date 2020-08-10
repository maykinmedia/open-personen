from rest_framework import serializers

from .codeenomschrijving import CodeEnOmschrijvingSerializer
from .datum import DatumSerializer
from .inonderzoek import DatumInOnderzoekSerializer


class OverlijdenSerializer(serializers.Serializer):
    indicatieOverleden = serializers.BooleanField(required=False)
    datum = DatumSerializer(required=False)
    land = CodeEnOmschrijvingSerializer(required=False)
    plaats = CodeEnOmschrijvingSerializer(required=False)
    inOnderzoek = DatumInOnderzoekSerializer(required=False)
