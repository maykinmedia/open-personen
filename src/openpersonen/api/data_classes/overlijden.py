from dataclasses import dataclass

from .datum import Datum
from .in_onderzoek import DatumInOnderzoek
from .waarde import Waarde


@dataclass
class Overlijden:
    indicatieOverleden: bool
    datum: Datum
    land: Waarde
    plaats: Waarde
    inOnderzoek: DatumInOnderzoek
