from dataclasses import dataclass

from .datum import Datum
from .in_onderzoek import VerblijfsTitelInOnderzoek
from .waarde import Waarde


@dataclass
class VerblijfsTitel:
    aanduiding: Waarde
    datumEinde: Datum
    datumIngang: Datum
    inOnderzoek: VerblijfsTitelInOnderzoek
