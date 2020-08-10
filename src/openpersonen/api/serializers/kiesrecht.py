from rest_framework import serializers

from .datum import DatumSerializer


class KiesrechtSerializer(serializers.Serializer):
    europeesKiesrecht = serializers.CharField(required=False)
    uitgeslotenVanKiesrecht = serializers.CharField(required=False)
    einddatumUitsluitingEuropeesKiesrecht = DatumSerializer(required=False)
    einddatumUitsluitingKiesrecht = DatumSerializer(required=False)
