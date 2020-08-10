from rest_framework import serializers

from .inonderzoek import NaamInOnderzoekSerializer


class NaamSerializer(serializers.Serializer):
    geslachtsnaam = serializers.CharField(max_length=200, required=False)
    voorletters = serializers.CharField(max_length=20, required=False)
    voornamen = serializers.CharField(max_length=200, required=False)
    voorvoegsel = serializers.CharField(max_length=10, required=False)
    in_onderzoek = NaamInOnderzoekSerializer(label='inOnderzoek', required=False)
    aanhef = serializers.CharField(required=False)
    aanschrijfwijze = serializers.CharField(required=False)
    gebruik_in_lopende_tekst = serializers.CharField(label='gebruikInLopendeTekst', required=False)
    aanduiding_naamgebruik = serializers.CharField(label='aanduidingNaamgebruik', required=False)
