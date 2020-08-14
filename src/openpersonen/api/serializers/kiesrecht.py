from rest_framework import serializers

from .datum import DatumSerializer


class KiesrechtSerializer(serializers.Serializer):
    europeesKiesrecht = serializers.CharField()
    uitgeslotenVanKiesrecht = serializers.CharField()
    einddatumUitsluitingEuropeesKiesrecht = DatumSerializer()
    einddatumUitsluitingKiesrecht = DatumSerializer()
