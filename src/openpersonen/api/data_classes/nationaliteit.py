from dataclasses import dataclass

from openpersonen.api.enum import AanduidingBijzonderNederlanderschapChoices

from .datum import Datum
from .in_onderzoek import NationaliteitInOnderzoek
from .waarde import Waarde


@dataclass
class Nationaliteit:
    aanduidingBijzonderNederlanderschap: str
    datumIngangGeldigheid: Datum
    nationaliteit: Waarde
    redenOpname: Waarde
    inOnderzoek: NationaliteitInOnderzoek

    def get_aanduidingBijzonderNederlanderschap_display(self):
        return AanduidingBijzonderNederlanderschapChoices.values[
            self.aanduidingBijzonderNederlanderschap
        ]
