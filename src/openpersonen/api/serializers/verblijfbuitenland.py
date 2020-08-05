from rest_framework import serializers

from .codeenomschrijving import CodeEnOmschrijvingSerializer


class VerblijfBuitenlandSerializer(serializers.Serializer):
    adresRegel1 = serializers.CharField()
    adresRegel2 = serializers.CharField()
    adresRegel3 = serializers.CharField()
    vertrokkenOnbekendWaarheen = serializers.BooleanField()
    land = CodeEnOmschrijvingSerializer()
