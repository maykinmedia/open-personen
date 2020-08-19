from dataclasses import dataclass

from .waarde import Waarde
from .datum import Datum
from .in_onderzoek import VerblijfsTitelInOnderzoek


@dataclass
class VerblijfsTitel:
    aanduiding: Waarde
    datumEinde: Datum
    datumIngang: Datum
    inOnderzoek: VerblijfsTitelInOnderzoek
