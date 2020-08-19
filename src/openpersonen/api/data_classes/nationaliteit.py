from dataclasses import dataclass

from .waarde import Waarde
from .datum import Datum
from .in_onderzoek import NationaliteitInOnderzoek


@dataclass
class Nationaliteit:
    aanduidingBijzonderNederlanderschap: str
    datumIngangGeldigheid: Datum
    nationaliteit: Waarde
    redenOpname: Waarde
    inOnderzoek: NationaliteitInOnderzoek
