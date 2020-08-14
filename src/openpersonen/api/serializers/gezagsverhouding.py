from rest_framework import serializers

from .inonderzoek import GezagsVerhoudingInOnderzoekSerializer


class GezagsVerhoudingSerializer(serializers.Serializer):
    indicatieCurateleRegister = serializers.CharField()
    indicatieGezagMinderjarige = serializers.CharField()
    inOnderzoek = GezagsVerhoudingInOnderzoekSerializer()
