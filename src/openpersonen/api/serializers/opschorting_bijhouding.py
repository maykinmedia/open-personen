from rest_framework import serializers

from openpersonen.api.enum import RedenOpschortingBijhoudingChoices

from .datum import DatumSerializer


class OpschortingBijhoudingSerializer(serializers.Serializer):
    reden = serializers.ChoiceField(RedenOpschortingBijhoudingChoices.choices, required=False)
    datum = DatumSerializer(required=False)
