from dataclasses import dataclass

from .datum import Datum


@dataclass
class NaamInOnderzoek:
    geslachtsnaam: bool
    voornamen: bool
    voorvoegsel: bool
    datumIngangOnderzoek: Datum


@dataclass
class IngeschrevenPersoonInOnderzoek:
    burgerservicenummer: bool
    geslachtsaanduiding: bool
    datumIngangOnderzoek: Datum


@dataclass
class NationaliteitInOnderzoek:
    aanduidingBijzonderNederlanderschap: bool
    nationaliteit: bool
    redenOpname: bool
    datumIngangOnderzoek: Datum


@dataclass
class DatumInOnderzoek:
    datum: bool
    land: bool
    plaats: bool
    datumIngangOnderzoek: Datum


@dataclass
class VerblijfPlaatsInOnderzoek:
    aanduidingBijHuisnummer: bool
    datumAanvangAdreshouding: bool
    datumIngangGeldigheid: bool
    datumInschrijvingInGemeente: bool
    datumVestigingInNederland: bool
    functieAdres: bool
    gemeenteVanInschrijving: bool
    huisletter: bool
    huisnummer: bool
    huisnummertoevoeging: bool
    identificatiecodeNummeraanduiding: bool
    identificatiecodeAdresseerbaarObject: bool
    landVanwaarIngeschreven: bool
    locatiebeschrijving: bool
    naamOpenbareRuimte: bool
    postcode: bool
    straatnaam: bool
    verblijfBuitenland: bool
    woonplaatsnaam: bool
    datumIngangOnderzoek: Datum


@dataclass
class GezagsVerhoudingInOnderzoek:
    indicatieCurateleRegister: bool
    indicatieGezagMinderjarige: bool
    datumIngangOnderzoek: Datum


@dataclass
class VerblijfsTitelInOnderzoek:
    aanduiding: bool
    datumEinde: bool
    datumIngang: bool
    datumIngangOnderzoek: Datum


@dataclass
class OuderInOnderzoek:
    burgerservicenummer: bool
    datumIngangFamilierechtelijkeBetrekking: bool
    geslachtsaanduiding: bool
    datumIngangOnderzoek: Datum


@dataclass
class KindInOnderzoek:
    burgerservicenummer: bool
    datumIngangOnderzoek: Datum


@dataclass
class PartnerInOnderzoek:
    burgerservicenummer: bool
    geslachtsaanduiding: bool
    soortVerbintenis: bool
    datumIngangOnderzoek: Datum
