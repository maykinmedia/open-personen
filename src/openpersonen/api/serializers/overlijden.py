from rest_framework import serializers

from .waarde import WaardeSerializer
from .datum import DatumSerializer
from .in_onderzoek import DatumInOnderzoekSerializer


class OverlijdenSerializer(serializers.Serializer):
    indicatieOverleden = serializers.BooleanField(required=False)
    datum = DatumSerializer(required=False)
    land = WaardeSerializer(required=False)
    plaats = WaardeSerializer(required=False)
    inOnderzoek = DatumInOnderzoekSerializer(required=False)
