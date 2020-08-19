from dataclasses import dataclass

from .in_onderzoek import GezagsVerhoudingInOnderzoek


@dataclass
class GezagsVerhouding:
    indicatieCurateleRegister: bool
    indicatieGezagMinderjarige: str
    inOnderzoek: GezagsVerhoudingInOnderzoek
