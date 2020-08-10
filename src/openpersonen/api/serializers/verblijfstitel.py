from rest_framework import serializers

from .codeenomschrijving import CodeEnOmschrijvingSerializer
from .datum import DatumSerializer
from .inonderzoek import VerblijfsTitelInOnderzoekSerializer


class VerblijfsTitelSerializer(serializers.Serializer):
    aanduiding = CodeEnOmschrijvingSerializer(required=False)
    datumEinde = DatumSerializer(required=False)
    datumIngang = DatumSerializer(required=False)
    inOnderzoek = VerblijfsTitelInOnderzoekSerializer(required=False)
