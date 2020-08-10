from rest_framework import serializers


class CodeEnOmschrijvingSerializer(serializers.Serializer):
    code = serializers.CharField(min_length=1, required=False)
    omschrijving = serializers.CharField(min_length=1, required=False)
