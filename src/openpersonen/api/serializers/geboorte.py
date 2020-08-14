from rest_framework import serializers

from .codeenomschrijving import CodeEnOmschrijvingSerializer
from .datum import DatumSerializer
from .inonderzoek import DatumInOnderzoekSerializer


class GeboorteSerializer(serializers.Serializer):
    datum = DatumSerializer()
    land = CodeEnOmschrijvingSerializer()
    plaats = CodeEnOmschrijvingSerializer()
    inOnderzoek = DatumInOnderzoekSerializer()
