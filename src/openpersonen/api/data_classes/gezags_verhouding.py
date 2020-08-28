from dataclasses import dataclass

from openpersonen.api.enum import IndicatieGezagMinderjarigeChoices

from .in_onderzoek import GezagsVerhoudingInOnderzoek


@dataclass
class GezagsVerhouding:
    indicatieCurateleRegister: bool
    indicatieGezagMinderjarige: str
    inOnderzoek: GezagsVerhoudingInOnderzoek

    def get_indicatieGezagMinderjarige_display(self):
        return IndicatieGezagMinderjarigeChoices.values[self.indicatieGezagMinderjarige]
