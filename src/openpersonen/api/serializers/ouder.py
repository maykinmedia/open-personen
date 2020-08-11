from rest_framework import serializers

from openpersonen.api.enum import GeslachtsaanduidingChoices, OuderAanduiding
from .datum import DatumSerializer
from .in_onderzoek import OuderInOnderzoekSerializer
from .persoon import PersoonSerializer


class OuderSerializer(PersoonSerializer):
    geslachtsaanduiding = serializers.ChoiceField(choices=GeslachtsaanduidingChoices.choices, required=False)
    ouderAanduiding = serializers.ChoiceField(choices=OuderAanduiding.choices, required=False)
    datumIngangFamilierechtelijkeBetrekking = DatumSerializer(required=False)
    inOnderzoek = OuderInOnderzoekSerializer(required=False)
