from rest_framework import serializers

from .aangaan_huwelijk_partnerschap import AangaanHuwelijkPartnerschapSerializer
from .in_onderzoek import PartnerInOnderzoek
from .persoon import PersoonSerializer


class PartnerSerializer(PersoonSerializer):
    soortVerbintenis = serializers.CharField(required=False)
    inOnderzoek = PartnerInOnderzoek(required=False)
    aangaanHuwelijkPartnerschap = AangaanHuwelijkPartnerschapSerializer(required=False)
