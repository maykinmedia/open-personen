from dataclasses import dataclass

from .waarde import Waarde
from .datum import Datum
from .in_onderzoek import VerblijfPlaatsInOnderzoek
from .verblijf_buitenland import VerblijfBuitenland


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
