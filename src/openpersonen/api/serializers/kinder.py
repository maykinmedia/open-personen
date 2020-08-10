from rest_framework import serializers

from .in_onderzoek import KinderInOnderzoek
from .persoon import PersoonSerializer


class KinderSerializer(PersoonSerializer):
    leeftijd = serializers.IntegerField(max_value=999, required=False)
    inOnderzoek = KinderInOnderzoek(required=False)
