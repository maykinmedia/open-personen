from rest_framework import serializers

from .datum import DatumSerializer
from .verblijf_plaats import VerblijfPlaatsSerializer


class VerblijfPlaatsHistorieSerializer(VerblijfPlaatsSerializer):
    datumTot = DatumSerializer(required=False)
    geheimhoudingPersoonsgegevens = serializers.BooleanField(required=False)
