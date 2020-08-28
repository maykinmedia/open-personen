from dataclasses import dataclass
from datetime import datetime
from dateutil.relativedelta import relativedelta

import xmltodict
from django.conf import settings

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

        antwoord_dict_object = dict_object['soapenv:Envelope']['soapenv:Body']['ns:npsLa01']['ns:antwoord']['ns:object']['ns:inp.heeftAlsKinderen']['ns:gerelateerde']

        kind_dict = {
            "burgerservicenummer": antwoord_dict_object['ns:inp.bsn'],
            "geheimhoudingPersoonsgegevens": True,
            "naam": {
                "geslachtsnaam": antwoord_dict_object['ns:geslachtsnaam'],
                "voorletters": antwoord_dict_object['ns:voorletters'],
                "voornamen": antwoord_dict_object['ns:voornamen'],
                "voorvoegsel": antwoord_dict_object['ns:voorvoegselGeslachtsnaam'],
                "inOnderzoek": {
                    "geslachtsnaam": bool(antwoord_dict_object['ns:geslachtsnaam']),
                    "voornamen": bool(antwoord_dict_object['ns:voornamen']),
                    "voorvoegsel": bool(antwoord_dict_object['ns:voorvoegselGeslachtsnaam']),
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
                    "dag": int(antwoord_dict_object['ns:geboortedatum'][settings.DAY_START: settings.DAY_END]),
                    "datum": antwoord_dict_object['ns:geboortedatum'],
                    "jaar": int(antwoord_dict_object['ns:geboortedatum'][settings.YEAR_START: settings.YEAR_END]),
                    "maand": int(antwoord_dict_object['ns:geboortedatum'][settings.MONTH_START: settings.MONTH_END]),
                },
                "land": {
                    "code": "string",
                    "omschrijving": antwoord_dict_object['ns:inp.geboorteLand']
                },
                "plaats": {
                    "code": "string",
                    "omschrijving": antwoord_dict_object['ns:inp.geboorteplaats']
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
                                      datetime.strptime(antwoord_dict_object['ns:geboortedatum'], '%Y%m%d')).years,
            "inOnderzoek": {
                "burgerservicenummer": bool(antwoord_dict_object['ns:inp.bsn']),
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
        response = client.get_kind(bsn)
        instance_dict = cls.get_instance_dict(response)
        return cls(**instance_dict)
