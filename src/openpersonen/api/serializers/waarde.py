from rest_framework import serializers


class WaardeSerializer(serializers.Serializer):
    code = serializers.CharField(required=False)
    omschrijving = serializers.CharField(required=False)
