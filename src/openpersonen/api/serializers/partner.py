from rest_framework import serializers

from openpersonen.api.enum import GeslachtsaanduidingChoices, SoortVerbintenis
from .aangaan_huwelijk_partnerschap import AangaanHuwelijkPartnerschapSerializer
from .in_onderzoek import PartnerInOnderzoek
from .persoon import PersoonSerializer


class PartnerSerializer(PersoonSerializer):
    geslachtsaanduiding = serializers.ChoiceField(choices=GeslachtsaanduidingChoices.choices, required=False)
    soortVerbintenis = serializers.ChoiceField(choices=SoortVerbintenis.choices, required=False)
    inOnderzoek = PartnerInOnderzoek(required=False)
    aangaanHuwelijkPartnerschap = AangaanHuwelijkPartnerschapSerializer(required=False)
