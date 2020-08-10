from rest_framework import serializers

from .in_onderzoek import NaamInOnderzoekSerializer


class NaamSerializer(serializers.Serializer):
    geslachtsnaam = serializers.CharField(max_length=200, required=False)
    voorletters = serializers.CharField(max_length=20, required=False)
    voornamen = serializers.CharField(max_length=200, required=False)
    voorvoegsel = serializers.CharField(max_length=10, required=False)
    inOnderzoek = NaamInOnderzoekSerializer(required=False)
    aanhef = serializers.CharField(min_length=1, required=False)
    aanschrijfwijze = serializers.CharField(min_length=1, required=False)
    gebruikInLopendeTekst = serializers.CharField(min_length=1, required=False)
    aanduidingNaamgebruik = serializers.CharField(min_length=1, required=False)
