from rest_framework import serializers

from .in_onderzoek import GezagsVerhoudingInOnderzoekSerializer
from openpersonen.api.enum import IndicatieGezagMinderjarigeChoices


class GezagsVerhoudingSerializer(serializers.Serializer):
    indicatieCurateleRegister = serializers.CharField(required=False)
    indicatieGezagMinderjarige = serializers.ChoiceField(choices=IndicatieGezagMinderjarigeChoices.choices,
                                                         required=False)
    inOnderzoek = GezagsVerhoudingInOnderzoekSerializer(required=False)