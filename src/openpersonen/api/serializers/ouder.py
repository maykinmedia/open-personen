from rest_framework import serializers

from .datum import DatumSerializer
from .inonderzoek import OuderInOnderzoekSerializer
from .persoon import PersoonSerializer


class OuderSerializer(PersoonSerializer):
    ouderAanduiding = serializers.CharField()
    datumIngangFamilierechtelijkeBetrekking = DatumSerializer()
    inOnderzoek = OuderInOnderzoekSerializer()
