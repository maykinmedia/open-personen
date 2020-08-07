from rest_framework import serializers

from .inonderzoek import KinderInOnderzoek
from .persoon import PersoonSerializer


class KinderSerializers(PersoonSerializer):
    leeftijd = serializers.IntegerField()
    inOnderzoek = KinderInOnderzoek()