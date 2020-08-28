from rest_framework import serializers

from openpersonen.api.enum import AanduidingNaamgebruikChoices

from .in_onderzoek import NaamInOnderzoekSerializer


class NaamSerializer(serializers.Serializer):
    geslachtsnaam = serializers.CharField(max_length=200, required=False)
    voorletters = serializers.CharField(max_length=20, required=False)
    voornamen = serializers.CharField(max_length=200, required=False)
    voorvoegsel = serializers.CharField(max_length=10, required=False)
    inOnderzoek = NaamInOnderzoekSerializer(required=False)


class IngeschrevenPersoonNaamSerializer(NaamSerializer):
    aanhef = serializers.CharField(required=False)
    aanschrijfwijze = serializers.CharField(required=False)
    gebruikInLopendeTekst = serializers.CharField(required=False)
    aanduidingNaamgebruik = serializers.ChoiceField(choices=AanduidingNaamgebruikChoices.choices,
                                                    required=False)
