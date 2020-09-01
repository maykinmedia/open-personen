from .ontbinding_huwelijk_partnerschap import OntbindingHuwelijkPartnerschapSerializer
from .partner import PartnerSerializer


class PartnerHistorieSerializer(PartnerSerializer):
    ontbindingHuwelijkPartnerschap = OntbindingHuwelijkPartnerschapSerializer(
        required=False
    )
