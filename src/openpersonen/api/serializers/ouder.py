from rest_framework import serializers

from .datum import DatumSerializer
from .inonderzoek import OuderInOnderzoekSerializer
from .persoon import PersoonSerializer


class OuderSerializer(PersoonSerializer):
    ouderAanduiding = serializers.CharField(required=False)
    datumIngangFamilierechtelijkeBetrekking = DatumSerializer(required=False)
    inOnderzoek = OuderInOnderzoekSerializer(required=False)
