from rest_framework import serializers


class CodeEnOmschrijvingSerializer(serializers.Serializer):
    code = serializers.CharField()
    omschrijving = serializers.CharField()
