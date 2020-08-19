from dataclasses import dataclass

from .waarde import Waarde
from .datum import Datum
from .in_onderzoek import DatumInOnderzoek


@dataclass
class Geboorte:
    datum: Datum
    land: Waarde
    plaats: Waarde
    inOnderzoek: DatumInOnderzoek
