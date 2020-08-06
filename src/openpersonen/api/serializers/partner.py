from rest_framework import serializers

from .aangaanhuwelijkpartnerschap import AangaanHuwelijkPartnerschapSerializer
from .inonderzoek import PartnerInOnderzoek
from .persoon import PersoonSerializer


class PartnerSerializer(PersoonSerializer):
    soortVerbintenis = serializers.CharField()
    inOnderzoek = PartnerInOnderzoek()
    aangaanHuwelijkPartnerschap = AangaanHuwelijkPartnerschapSerializer()
