from rest_framework import serializers

from .datum import DatumSerializer


class OpschortingBijhouding(serializers.Serializer):
    reden = serializers.CharField()
    datum = DatumSerializer()
