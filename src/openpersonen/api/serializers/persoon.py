from rest_framework import serializers

from .geboorte import GeboorteSerializer
from .naam import NaamSerializer


class PersoonSerializer(serializers.Serializer):
    burgerservicenummer = serializers.RegexField(
        "^[0-9]*$", required=False, min_length=9, max_length=9
    )
    geheimhoudingPersoonsgegevens = serializers.BooleanField(required=False)
    naam = NaamSerializer(required=False)
    geboorte = GeboorteSerializer(required=False)
