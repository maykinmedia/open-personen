from dataclasses import dataclass

from openpersonen.api.enum import AanduidginBijHuisnummerChoices, FunctieAdresChoices

from .datum import Datum
from .in_onderzoek import VerblijfPlaatsInOnderzoek
from .verblijf_buitenland import VerblijfBuitenland
from .waarde import Waarde


@dataclass
class VerblijfPlaats:
    functieAdres: str
    huisletter: str
    huisnummer: int
    huisnummertoevoeging: str
    aanduidingBijHuisnummer: str
    identificatiecodeNummeraanduiding: str
    naamOpenbareRuimte: str
    postcode: str
    woonplaatsnaam: str
    identificatiecodeAdresseerbaarObject: str
    indicatieVestigingVanuitBuitenland: bool
    locatiebeschrijving: str
    straatnaam: str
    vanuitVertrokkenOnbekendWaarheen: bool
    datumAanvangAdreshouding: Datum
    datumIngangGeldigheid: Datum
    datumInschrijvingInGemeente: Datum
    datumVestigingInNederland: Datum
    gemeenteVanInschrijving: Waarde
    landVanwaarIngeschreven: Waarde
    verblijfBuitenland: VerblijfBuitenland
    inOnderzoek: VerblijfPlaatsInOnderzoek

    def get_aanduidingBijHuisnummer_display(self):
        return AanduidginBijHuisnummerChoices.values[self.aanduidingBijHuisnummer]

    def get_functieAdres_display(self):
        return FunctieAdresChoices.values[self.functieAdres]
