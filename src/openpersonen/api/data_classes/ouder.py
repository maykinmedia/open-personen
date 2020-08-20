from dataclasses import dataclass

from openpersonen.api.enum import GeslachtsaanduidingChoices, OuderAanduiding
from .datum import Datum
from .in_onderzoek import OuderInOnderzoek
from .persoon import Persoon


@dataclass
class Ouder(Persoon):
    geslachtsaanduiding: str
    ouderAanduiding: str
    datumIngangFamilierechtelijkeBetrekking: Datum
    inOnderzoek: OuderInOnderzoek

    def get_geslachtsaanduiding_display(self):
        return GeslachtsaanduidingChoices.values[self.geslachtsaanduiding]

    def get_ouderAanduiding_display(self):
        return OuderAanduiding.values[self.ouderAanduiding]
