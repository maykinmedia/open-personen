from rest_framework import serializers

from .inonderzoek import GezagsVerhoudingInOnderzoekSerializer
from openpersonen.api.enum.indicatie_gezag_minderjarige import IndicatieGezagMinderjarigeChoices


class GezagsVerhoudingSerializer(serializers.Serializer):
    indicatieCurateleRegister = serializers.CharField(required=False)
    indicatieGezagMinderjarige = serializers.ChoiceField(choices=IndicatieGezagMinderjarigeChoices.choices,
                                                         required=False)
    inOnderzoek = GezagsVerhoudingInOnderzoekSerializer(required=False)
