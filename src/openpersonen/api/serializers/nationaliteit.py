from rest_framework import serializers

from openpersonen.api.enum import AanduidingBijzonderNederlanderschapChoices

from .datum import DatumSerializer
from .in_onderzoek import NationaliteitInOnderzoekSerializer
from .waarde import WaardeSerializer


class NationaliteitSerializer(serializers.Serializer):
    aanduidingBijzonderNederlanderschap = serializers.ChoiceField(AanduidingBijzonderNederlanderschapChoices.choices,
                                                                  required=False)
    datumIngangGeldigheid = DatumSerializer(required=False)
    nationaliteit = WaardeSerializer(required=False)
    redenOpname = WaardeSerializer(required=False)
    inOnderzoek = NationaliteitInOnderzoekSerializer(required=False)
