from dataclasses import dataclass

from openpersonen.api.enum import AanduidingNaamgebruikChoices

from .in_onderzoek import NaamInOnderzoek


@dataclass
class Naam:
    geslachtsnaam: str
    voorletters: str
    voornamen: str
    voorvoegsel: str
    inOnderzoek: NaamInOnderzoek


@dataclass
class IngeschrevenPersoonNaam(Naam):
    aanhef: str
    aanschrijfwijze: str
    gebruikInLopendeTekst: str
    aanduidingNaamgebruik: str

    def get_aanduidingNaamgebruik_display(self):
        return AanduidingNaamgebruikChoices.values[self.aanduidingNaamgebruik]
