from dataclasses import dataclass
from datetime import datetime

from django.conf import settings

import xmltodict
from dateutil.relativedelta import relativedelta

from openpersonen.api.models import StufBGClient
from openpersonen.api.testing_models import Persoon, Kind
from openpersonen.api.utils import convert_empty_instances

from .in_onderzoek import KindInOnderzoek
from .persoon import Persoon


@dataclass
class Kind(Persoon):
    leeftijd: int
    inOnderzoek: KindInOnderzoek

    @staticmethod
    def get_client_instance_dict(response):
        dict_object = xmltodict.parse(response.content)

        antwoord_dict_object = dict_object["soapenv:Envelope"]["soapenv:Body"][
            "ns:npsLa01"
        ]["ns:antwoord"]["ns:object"]["ns:inp.heeftAlsKinderen"]["ns:gerelateerde"]

        kind_dict = {
            "burgerservicenummer": antwoord_dict_object["ns:inp.bsn"],
            "geheimhoudingPersoonsgegevens": True,
            "naam": {
                "geslachtsnaam": antwoord_dict_object["ns:geslachtsnaam"],
                "voorletters": antwoord_dict_object["ns:voorletters"],
                "voornamen": antwoord_dict_object["ns:voornamen"],
                "voorvoegsel": antwoord_dict_object["ns:voorvoegselGeslachtsnaam"],
                "inOnderzoek": {
                    "geslachtsnaam": bool(antwoord_dict_object["ns:geslachtsnaam"]),
                    "voornamen": bool(antwoord_dict_object["ns:voornamen"]),
                    "voorvoegsel": bool(
                        antwoord_dict_object["ns:voorvoegselGeslachtsnaam"]
                    ),
                    "datumIngangOnderzoek": {
                        "dag": 0,
                        "datum": "string",
                        "jaar": 0,
                        "maand": 0,
                    },
                },
            },
            "geboorte": {
                "datum": {
                    "dag": int(
                        antwoord_dict_object["ns:geboortedatum"][
                            settings.DAY_START : settings.DAY_END
                        ]
                    ),
                    "datum": antwoord_dict_object["ns:geboortedatum"],
                    "jaar": int(
                        antwoord_dict_object["ns:geboortedatum"][
                            settings.YEAR_START : settings.YEAR_END
                        ]
                    ),
                    "maand": int(
                        antwoord_dict_object["ns:geboortedatum"][
                            settings.MONTH_START : settings.MONTH_END
                        ]
                    ),
                },
                "land": {
                    "code": "string",
                    "omschrijving": antwoord_dict_object["ns:inp.geboorteLand"],
                },
                "plaats": {
                    "code": "string",
                    "omschrijving": antwoord_dict_object["ns:inp.geboorteplaats"],
                },
                "inOnderzoek": {
                    "datum": True,
                    "land": True,
                    "plaats": True,
                    "datumIngangOnderzoek": {
                        "dag": 0,
                        "datum": "string",
                        "jaar": 0,
                        "maand": 0,
                    },
                },
            },
            "leeftijd": relativedelta(
                datetime.now(),
                datetime.strptime(antwoord_dict_object["ns:geboortedatum"], "%Y%m%d"),
            ).years,
            "inOnderzoek": {
                "burgerservicenummer": bool(antwoord_dict_object["ns:inp.bsn"]),
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0,
                },
            },
        }

        convert_empty_instances(kind_dict)

        return kind_dict

    @staticmethod
    def get_model_instance_dict(kind):

        kind_dict = {
            "burgerservicenummer": kind.burgerservicenummer_persoon,
            "geheimhoudingPersoonsgegevens": True,
            "naam": {
                "geslachtsnaam": kind.geslachtsnaam_kind,
                "voorletters": "string",
                "voornamen": kind.voornamen_kind,
                "voorvoegsel": kind.voorvoegsel_geslachtsnaam_kind,
                "inOnderzoek": {
                    "geslachtsnaam": bool(kind.geslachtsnaam_kind),
                    "voornamen": bool(kind.voornamen_kind),
                    "voorvoegsel": bool(
                        kind.voorvoegsel_geslachtsnaam_kind
                    ),
                    "datumIngangOnderzoek": {
                        "dag": 0,
                        "datum": "string",
                        "jaar": 0,
                        "maand": 0,
                    },
                },
            },
            "geboorte": {
                "datum": {
                    "dag": int(
                        kind.geboortedatum_kind[
                        settings.DAY_START: settings.DAY_END
                        ]
                    ),
                    "datum": kind.geboortedatum_kind,
                    "jaar": int(
                        kind.geboortedatum_kind[
                        settings.YEAR_START: settings.YEAR_END
                        ]
                    ),
                    "maand": int(
                        kind.geboortedatum_kind[
                        settings.MONTH_START: settings.MONTH_END
                        ]
                    ),
                },
                "land": {
                    "code": "string",
                    "omschrijving": kind.geboorteland_kind,
                },
                "plaats": {
                    "code": "string",
                    "omschrijving": kind.geboorteplaats_kind,
                },
                "inOnderzoek": {
                    "datum": True,
                    "land": True,
                    "plaats": True,
                    "datumIngangOnderzoek": {
                        "dag": 0,
                        "datum": "string",
                        "jaar": 0,
                        "maand": 0,
                    },
                },
            },
            "leeftijd": relativedelta(
                datetime.now(),
                datetime.strptime(kind.geboortedatum_kind, "%Y%m%d"),
            ).years,
            "inOnderzoek": {
                "burgerservicenummer": bool(kind.burgerservicenummer_kind),
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0,
                },
            },
        }

        return kind_dict

    @classmethod
    def retrieve(cls, bsn, id):
        if settings.USE_STUF_BG_DATABASE:
            instance = Persoon.objects.get(burgerservicenummer_persoon=bsn).kind_set.get(burgerservicenummer_kind=id)
            instance_dict = cls.get_model_instance_dict(instance)
        else:
            response = StufBGClient.get_solo().get_kind(bsn)
            instance_dict = cls.get_client_instance_dict(response)
        return cls(**instance_dict)
