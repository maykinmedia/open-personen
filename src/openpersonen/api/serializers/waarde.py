from rest_framework import serializers


class WaardeSerializer(serializers.Serializer):
    code = serializers.CharField(min_length=1, required=False)
    omschrijving = serializers.CharField(min_length=1, required=False)
