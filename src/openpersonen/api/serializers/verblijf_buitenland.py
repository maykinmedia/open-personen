from rest_framework import serializers

from .waarde import WaardeSerializer


class VerblijfBuitenlandSerializer(serializers.Serializer):
    adresRegel1 = serializers.CharField(max_length=35, required=False)
    adresRegel2 = serializers.CharField(max_length=35, required=False)
    adresRegel3 = serializers.CharField(max_length=35, required=False)
    vertrokkenOnbekendWaarheen = serializers.BooleanField(required=False)
    land = WaardeSerializer(required=False)
