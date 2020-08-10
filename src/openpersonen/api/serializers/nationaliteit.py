from rest_framework import serializers

from .codeenomschrijving import CodeEnOmschrijvingSerializer
from .datum import DatumSerializer
from .inonderzoek import NationaliteitInOnderzoekSerializer
from openpersonen.api.enum.aanduiding_bijzonder_nederlanderschap import AanduidingBijzonderNederlanderschapChoices


class NationaliteitSerializer(serializers.Serializer):
    aanduidingBijzonderNederlanderschap = serializers.ChoiceField(AanduidingBijzonderNederlanderschapChoices.choices,
                                                                  required=False)
    datumIngangGeldigheid = DatumSerializer(required=False)
    nationaliteit = CodeEnOmschrijvingSerializer(required=False)
    redenOpname = CodeEnOmschrijvingSerializer(required=False)
    inOnderzoek = NationaliteitInOnderzoekSerializer(required=False)
