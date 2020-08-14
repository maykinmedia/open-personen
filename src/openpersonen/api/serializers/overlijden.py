from rest_framework import serializers

from .codeenomschrijving import CodeEnOmschrijvingSerializer
from .datum import DatumSerializer
from .inonderzoek import DatumInOnderzoekSerializer


class OverlijdenSerializer(serializers.Serializer):
    indicatieOverleden = serializers.BooleanField()
    datum = DatumSerializer()
    land = CodeEnOmschrijvingSerializer()
    plaats = CodeEnOmschrijvingSerializer()
    inOnderzoek = DatumInOnderzoekSerializer()
