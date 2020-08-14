from rest_framework import serializers

from .inonderzoek import NaamInOnderzoekSerializer


class NaamSerializer(serializers.Serializer):
    geslachtsnaam = serializers.CharField()
    voorletters = serializers.CharField()
    voornamen = serializers.CharField()
    voorvoegsel = serializers.CharField()
    inOnderzoek = NaamInOnderzoekSerializer()
    aanhef = serializers.CharField()
    aanschrijfwijze = serializers.CharField()
    gebruikInLopendeTekst = serializers.CharField()
    aanduidingNaamgebruik = serializers.CharField()
