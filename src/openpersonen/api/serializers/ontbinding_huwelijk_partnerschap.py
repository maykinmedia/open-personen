from rest_framework import serializers

from .waarde import WaardeSerializer
from .datum import DatumSerializer
from .in_onderzoek import DatumInOnderzoekSerializer


class OntbindingHuwelijkPartnerschapSerializer(serializers.Serializer):
    indicatieHuwelijkPartnerschapBeeindigd = serializers.BooleanField(required=False)
    datum = DatumSerializer(required=False)
    land = WaardeSerializer(required=False)
    plaats = WaardeSerializer(required=False)
    reden = WaardeSerializer(required=False)
    inOnderzoek = DatumInOnderzoekSerializer(required=False)
