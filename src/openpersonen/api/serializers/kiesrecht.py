from rest_framework import serializers

from .datum import DatumSerializer


class KiesrechtSerializer(serializers.Serializer):
    europeesKiesrecht = serializers.BooleanField(required=False)
    uitgeslotenVanKiesrecht = serializers.BooleanField(required=False)
    einddatumUitsluitingEuropeesKiesrecht = DatumSerializer(required=False)
    einddatumUitsluitingKiesrecht = DatumSerializer(required=False)
