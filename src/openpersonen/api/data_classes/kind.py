from dataclasses import dataclass
from datetime import datetime
from dateutil.relativedelta import relativedelta

import xmltodict

from openpersonen.api.client import client
from openpersonen.api.utils import convert_empty_instances
from .in_onderzoek import KindInOnderzoek
from .persoon import Persoon


@dataclass
class Kind(Persoon):
    leeftijd: int
    inOnderzoek: KindInOnderzoek

    @staticmethod
    def get_instance_dict(response):
        dict_object = xmltodict.parse(response.content)

        antwoord_dict_object = dict_object['env:Envelope']['env:Body']['npsLa01']['BG:antwoord']['object']

        kind_dict = {
            "burgerservicenummer": antwoord_dict_object['BG:inp.bsn'],
            "geheimhoudingPersoonsgegevens": True,
            "naam": {
                "geslachtsnaam": antwoord_dict_object['BG:geslachtsnaam'],
                "voorletters": antwoord_dict_object['BG:voorletters'],
                "voornamen": antwoord_dict_object['BG:voornamen'],
                "voorvoegsel": antwoord_dict_object['BG:voorvoegselGeslachtsnaam'],
                "inOnderzoek": {
                    "geslachtsnaam": bool(antwoord_dict_object['BG:geslachtsnaam']),
                    "voornamen": bool(antwoord_dict_object['BG:voornamen']),
                    "voorvoegsel": bool(antwoord_dict_object['BG:voorvoegselGeslachtsnaam']),
                    "datumIngangOnderzoek": {
                        "dag": 0,
                        "datum": "string",
                        "jaar": 0,
                        "maand": 0
                    }
                }
            },
            "geboorte": {
                "datum": {
                    "dag": antwoord_dict_object['BG:geboortedatum'][6:8],
                    "datum": antwoord_dict_object['BG:geboortedatum'],
                    "jaar": antwoord_dict_object['BG:geboortedatum'][0:4],
                    "maand": antwoord_dict_object['BG:geboortedatum'][4:6]
                },
                "land": {
                    "code": "string",
                    "omschrijving": antwoord_dict_object['BG:inp.geboorteLand']
                },
                "plaats": {
                    "code": "string",
                    "omschrijving": antwoord_dict_object['BG:inp.geboorteplaats']
                },
                "inOnderzoek": {
                    "datum": True,
                    "land": True,
                    "plaats": True,
                    "datumIngangOnderzoek": {
                        "dag": 0,
                        "datum": "string",
                        "jaar": 0,
                        "maand": 0
                    }
                }
            },
            "leeftijd": relativedelta(datetime.now(),
                                      datetime.strptime(antwoord_dict_object['BG:geboortedatum'], '%Y%m%d')).years,
            "inOnderzoek": {
                "burgerservicenummer": True,
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0
                }
            }
        }

        convert_empty_instances(kind_dict)

        return kind_dict

    @classmethod
    def retrieve(cls, bsn):
        response = client.get_kinderen_van_aanvrager(bsn)
        instance_dict = cls.get_instance_dict(response)
        return cls(**instance_dict)
