from rest_framework import serializers

from .datum import DatumSerializer
from openpersonen.api.enum import RedenOpschortingBijhoudingChoices


class OpschortingBijhoudingSerializer(serializers.Serializer):
    reden = serializers.ChoiceField(RedenOpschortingBijhoudingChoices.choices, required=False)
    datum = DatumSerializer(required=False)
