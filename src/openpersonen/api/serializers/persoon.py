from rest_framework import serializers

from .geboorte import GeboorteSerializer
from .naam import NaamSerializer


class PersoonSerializer(serializers.Serializer):
    burgerservicenummer = serializers.CharField()
    geheimhoudingPersoonsgegevens = serializers.BooleanField()
    geslachtsaanduiding = serializers.CharField()
    naam = NaamSerializer()
    geboorte = GeboorteSerializer()
