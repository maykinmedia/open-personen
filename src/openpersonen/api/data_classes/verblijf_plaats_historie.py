from dataclasses import dataclass

import xmltodict

from openpersonen.api.client import client
from openpersonen.api.utils import convert_empty_instances

from .datum import Datum
from .verblijf_plaats import VerblijfPlaats


@dataclass
class VerblijfPlaatsHistorie(VerblijfPlaats):
    datumTot: Datum
    geheimhoudingPersoonsgegevens: bool

    @staticmethod
    def get_instance_dict(response):
        dict_object = xmltodict.parse(response.content)

        antwoord_dict_object = dict_object["soapenv:Envelope"]["soapenv:Body"][
            "ns:npsLa01"
        ]["ns:antwoord"]["ns:object"]["ns:inp.verblijftIn"][
            "ns:historieFormeelRelatie"
        ][
            "ns:gerelateerde"
        ][
            "ns:adresAanduidingGrp"
        ]

        verblijf_plaats_dict = {
            "functieAdres": "woonadres",
            "huisletter": antwoord_dict_object["ns:aoa.huisletter"],
            "huisnummer": antwoord_dict_object["ns:aoa.huisnummer"],
            "huisnummertoevoeging": antwoord_dict_object["ns:aoa.huisnummertoevoeging"],
            "aanduidingBijHuisnummer": "tegenover",
            "identificatiecodeNummeraanduiding": "0518200000366054",
            "naamOpenbareRuimte": antwoord_dict_object["ns:gor.openbareRuimteNaam"],
            "postcode": antwoord_dict_object["ns:aoa.postcode"],
            "woonplaatsnaam": antwoord_dict_object["ns:wpl.woonplaatsNaam"],
            "identificatiecodeAdresseerbaarObject": "0518200000366054",
            "indicatieVestigingVanuitBuitenland": True,
            "locatiebeschrijving": "Naast de derde brug",
            "straatnaam": "string",
            "vanuitVertrokkenOnbekendWaarheen": True,
            "datumAanvangAdreshouding": {
                "dag": 3,
                "datum": "1989-05-03",
                "jaar": 1989,
                "maand": 5,
            },
            "datumIngangGeldigheid": {
                "dag": 3,
                "datum": "1989-05-03",
                "jaar": 1989,
                "maand": 5,
            },
            "datumInschrijvingInGemeente": {
                "dag": 3,
                "datum": "1989-05-03",
                "jaar": 1989,
                "maand": 5,
            },
            "datumVestigingInNederland": {
                "dag": 3,
                "datum": "1989-05-03",
                "jaar": 1989,
                "maand": 5,
            },
            "gemeenteVanInschrijving": {"code": "6030", "omschrijving": "Nederland"},
            "landVanwaarIngeschreven": {"code": "6030", "omschrijving": "Nederland"},
            "verblijfBuitenland": {
                "adresRegel1": "string",
                "adresRegel2": "string",
                "adresRegel3": "string",
                "vertrokkenOnbekendWaarheen": True,
                "land": {"code": "6030", "omschrijving": "Nederland"},
            },
            "inOnderzoek": {
                "aanduidingBijHuisnummer": True,
                "datumAanvangAdreshouding": True,
                "datumIngangGeldigheid": True,
                "datumInschrijvingInGemeente": True,
                "datumVestigingInNederland": True,
                "functieAdres": True,
                "gemeenteVanInschrijving": True,
                "huisletter": bool(antwoord_dict_object["ns:aoa.huisletter"]),
                "huisnummer": bool(antwoord_dict_object["ns:aoa.huisnummer"]),
                "huisnummertoevoeging": bool(
                    antwoord_dict_object["ns:aoa.huisnummertoevoeging"]
                ),
                "identificatiecodeNummeraanduiding": True,
                "identificatiecodeAdresseerbaarObject": True,
                "landVanwaarIngeschreven": True,
                "locatiebeschrijving": True,
                "naamOpenbareRuimte": bool(
                    antwoord_dict_object["ns:gor.openbareRuimteNaam"]
                ),
                "postcode": bool(antwoord_dict_object["ns:aoa.postcode"]),
                "straatnaam": True,
                "verblijfBuitenland": True,
                "woonplaatsnaam": bool(antwoord_dict_object["ns:wpl.woonplaatsNaam"]),
                "datumIngangOnderzoek": {
                    "dag": 3,
                    "datum": "1989-05-03",
                    "jaar": 1989,
                    "maand": 5,
                },
            },
            "datumTot": {"dag": 3, "datum": "1989-05-03", "jaar": 1989, "maand": 5},
            "geheimhoudingPersoonsgegevens": True,
        }

        convert_empty_instances(verblijf_plaats_dict)

        return verblijf_plaats_dict

    @classmethod
    def list(cls, bsn, filters):
        response = client.get_verblijf_plaats_historie(bsn, filters)
        instance_dict = cls.get_instance_dict(response)
        return [cls(**instance_dict)]
