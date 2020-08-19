from rest_framework import serializers

from .in_onderzoek import KindInOnderzoekSerializer
from .persoon import PersoonSerializer


class KindSerializer(PersoonSerializer):
    leeftijd = serializers.IntegerField(max_value=999, required=False)
    inOnderzoek = KindInOnderzoekSerializer(required=False)
