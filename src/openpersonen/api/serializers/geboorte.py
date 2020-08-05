from rest_framework import serializers

from .codeenomschrijving import CodeEnOmschrijvingSerializer
from .datum import DatumSerializer
from .inonderzoek import DatumInOnderzoekSerializer


class GeboorteSerializers(serializers.Serializer):
    datum = DatumSerializer()
    land = CodeEnOmschrijvingSerializer()
    plaats = CodeEnOmschrijvingSerializer()
    inOnderzoek = DatumInOnderzoekSerializer()
