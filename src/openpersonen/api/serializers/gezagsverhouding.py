from rest_framework import serializers

from .inonderzoek import GezagsVerhoudingInOnderzoekSerializer


class GezagsVerhoudingSerializer(serializers.Serializer):
    indicatieCurateleRegister = serializers.CharField(required=False)
    indicatieGezagMinderjarige = serializers.CharField(required=False)
    inOnderzoek = GezagsVerhoudingInOnderzoekSerializer(required=False)
