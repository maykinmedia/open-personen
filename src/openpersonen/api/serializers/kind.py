from rest_framework import serializers

from .inonderzoek import KinderInOnderzoek
from .persoon import PersoonSerializer


class KindSerializer(PersoonSerializer):
    leeftijd = serializers.IntegerField()
    inOnderzoek = KinderInOnderzoek()
