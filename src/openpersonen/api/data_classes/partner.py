from dataclasses import dataclass

from django.conf import settings
from django.utils.module_loading import import_string

from openpersonen.api.enum import GeslachtsaanduidingChoices, SoortVerbintenis

from .aangaan_huwelijk_partnerschap import AangaanHuwelijkPartnerschap
from .in_onderzoek import PartnerInOnderzoek
from .persoon import Persoon


@dataclass
class Partner(Persoon):
    geslachtsaanduiding: str
    soortVerbintenis: str
    inOnderzoek: PartnerInOnderzoek
    aangaanHuwelijkPartnerschap: AangaanHuwelijkPartnerschap

    backend_function_name = "get_partner"

    def get_geslachtsaanduiding_display(self):
        return GeslachtsaanduidingChoices.values[self.geslachtsaanduiding]

    def get_soortVerbintenis_display(self):
        return SoortVerbintenis.values[self.soortVerbintenis]
