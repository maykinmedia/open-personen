from rest_framework import serializers

from .datum import DatumSerializer
from .nationaliteit import NationaliteitSerializer
from .waarde import WaardeSerializer


class NationaliteitHistorieSerializer(NationaliteitSerializer):
    geheimhoudingPersoonsgegevens = serializers.BooleanField(required=False)
    datumEindeGeldigheid = DatumSerializer(required=False)
    redenBeeindigen = WaardeSerializer(required=False)
    indicatieNationaliteitBeeindigd = serializers.BooleanField(required=False)
