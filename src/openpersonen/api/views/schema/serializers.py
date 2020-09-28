from rest_framework import serializers


class SchemaFieldValidationErrorSerializer(serializers.Serializer):
    """
    Formaat van validatiefouten.
    """

    name = serializers.CharField(
        help_text="Naam van het veld met ongeldige gegevens", required=False
    )
    code = serializers.CharField(
        help_text="Systeemcode die het type fout aangeeft", required=False
    )
    reason = serializers.CharField(
        help_text="Uitleg wat er precies fout is met de gegevens", required=False
    )


class SchemaFoutSerializer(serializers.Serializer):
    """
    Formaat van HTTP 4xx en 5xx fouten.
    """

    type = serializers.CharField(
        help_text="URI referentie naar het type fout, bedoeld voor developers",
        required=False,
        allow_blank=True,
    )
    # not according to DSO, but possible for programmatic checking
    code = serializers.CharField(
        help_text="Systeemcode die het type fout aangeeft", required=False
    )
    title = serializers.CharField(
        help_text="Generieke titel voor het type fout", required=False
    )
    status = serializers.IntegerField(help_text="De HTTP status code", required=False)
    detail = serializers.CharField(
        help_text="Extra informatie bij de fout, indien beschikbaar", required=False
    )
    instance = serializers.CharField(
        help_text="URI met referentie naar dit specifiek voorkomen van de fout. Deze kan "
        "gebruikt worden in combinatie met server logs, bijvoorbeeld.",
        required=False,
    )


class SchemaValidatieFoutSerializer(SchemaFoutSerializer):
    invalid_params = SchemaFieldValidationErrorSerializer(many=True, required=False)
