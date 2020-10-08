from dataclasses import dataclass

from openpersonen.backends import backend

from .ontbinding_huwelijk_partnerschap import OntbindingHuwelijkPartnerschap
from .partner import Partner


@dataclass
class PartnerHistorie(Partner):
    ontbindingHuwelijkPartnerschap: OntbindingHuwelijkPartnerschap

    @classmethod
    def list(cls, bsn, filters):
        instance_dict = backend.get_partner_historie(bsn, filters)
        return [cls(**instance_dict)]
