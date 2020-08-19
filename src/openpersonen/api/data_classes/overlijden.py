from dataclasses import dataclass

from .waarde import Waarde
from .datum import Datum
from .in_onderzoek import DatumInOnderzoek


@dataclass
class Overlijden:
    indicatieOverleden: bool
    datum: Datum
    land: Waarde
    plaats: Waarde
    inOnderzoek: DatumInOnderzoek
