from dataclasses import dataclass

from .waarde import Waarde
from .datum import Datum
from .in_onderzoek import DatumInOnderzoek


@dataclass
class OntbindingHuwelijkPartnerschap:
    indicatieHuwelijkPartnerschapBeeindigd: bool
    datum: Datum
    land: Waarde
    plaats: Waarde
    reden: Waarde
    inOnderzoek: DatumInOnderzoek
