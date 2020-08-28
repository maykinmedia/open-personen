from rest_framework import serializers

from .datum import DatumSerializer
from .in_onderzoek import DatumInOnderzoekSerializer
from .waarde import WaardeSerializer


class GeboorteSerializer(serializers.Serializer):
    datum = DatumSerializer(required=False)
    land = WaardeSerializer(required=False)
    plaats = WaardeSerializer(required=False)
    inOnderzoek = DatumInOnderzoekSerializer(required=False)
