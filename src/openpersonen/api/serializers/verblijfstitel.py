from rest_framework import serializers

from .codeenomschrijving import CodeEnOmschrijvingSerializer
from .datum import DatumSerializer
from .inonderzoek import VerblijfsTitelInOnderzoekSerializer


class VerblijfsTitelSerializer(serializers.Serializer):
    aanduiding = CodeEnOmschrijvingSerializer()
    datumEinde = DatumSerializer()
    datumIngang = DatumSerializer()
    inOnderzoek = VerblijfsTitelInOnderzoekSerializer()
