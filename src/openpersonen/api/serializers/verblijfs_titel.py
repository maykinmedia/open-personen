from rest_framework import serializers

from .waarde import WaardeSerializer
from .datum import DatumSerializer
from .in_onderzoek import VerblijfsTitelInOnderzoekSerializer


class VerblijfsTitelSerializer(serializers.Serializer):
    aanduiding = WaardeSerializer(required=False)
    datumEinde = DatumSerializer(required=False)
    datumIngang = DatumSerializer(required=False)
    inOnderzoek = VerblijfsTitelInOnderzoekSerializer(required=False)
