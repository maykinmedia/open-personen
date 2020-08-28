from rest_framework import serializers

from openpersonen.api.enum import IndicatieGezagMinderjarigeChoices

from .in_onderzoek import GezagsVerhoudingInOnderzoekSerializer


class GezagsVerhoudingSerializer(serializers.Serializer):
    indicatieCurateleRegister = serializers.BooleanField(required=False)
    indicatieGezagMinderjarige = serializers.ChoiceField(
        choices=IndicatieGezagMinderjarigeChoices.choices, required=False
    )
    inOnderzoek = GezagsVerhoudingInOnderzoekSerializer(required=False)
