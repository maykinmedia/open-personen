from rest_framework import serializers

from .inonderzoek import KinderInOnderzoek
from .persoon import PersoonSerializer


class KinderSerializer(PersoonSerializer):
    leeftijd = serializers.IntegerField(max_value=999, required=False)
    in_onderzoek = KinderInOnderzoek(label='inOnderzoek', required=False)
