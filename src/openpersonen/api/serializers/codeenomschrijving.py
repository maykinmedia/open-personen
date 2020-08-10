from rest_framework import serializers


class CodeEnOmschrijvingSerializer(serializers.Serializer):
    code = serializers.CharField(required=False)
    omschrijving = serializers.CharField(required=False)
