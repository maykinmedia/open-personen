from dataclasses import dataclass

from .geboorte import Geboorte
from .naam import Naam


@dataclass
class Persoon:
    burgerservicenummer: str
    geheimhoudingPersoonsgegevens: bool
    naam: Naam
    geboorte: Geboorte
