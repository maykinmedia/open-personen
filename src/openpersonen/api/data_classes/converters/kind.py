from datetime import datetime

from django.conf import settings

import xmltodict
from dateutil.relativedelta import relativedelta

from openpersonen.api.utils import convert_empty_instances


def convert_client_response_to_instance_dict(response):
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


def convert_model_instance_to_instance_dict(kind):

    kind_dict = {
        "burgerservicenummer": kind.burgerservicenummer_kind,
        "geheimhoudingPersoonsgegevens": True,
        "naam": {
            "geslachtsnaam": kind.geslachtsnaam_kind,
            "voorletters": "string",
            "voornamen": kind.voornamen_kind,
            "voorvoegsel": kind.voorvoegsel_geslachtsnaam_kind,
            "inOnderzoek": {
                "geslachtsnaam": bool(kind.geslachtsnaam_kind),
                "voornamen": bool(kind.voornamen_kind),
                "voorvoegsel": bool(kind.voorvoegsel_geslachtsnaam_kind),
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
                    kind.geboortedatum_kind[settings.DAY_START : settings.DAY_END]
                )
                if kind.geboortedatum_kind
                else 0,
                "datum": kind.geboortedatum_kind,
                "jaar": int(
                    kind.geboortedatum_kind[settings.YEAR_START : settings.YEAR_END]
                )
                if kind.geboortedatum_kind
                else 0,
                "maand": int(
                    kind.geboortedatum_kind[settings.MONTH_START : settings.MONTH_END]
                )
                if kind.geboortedatum_kind
                else 0,
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
        ).years
        if kind.geboortedatum_kind
        else 0,
        "inOnderzoek": {
            "burgerservicenummer": bool(kind.burgerservicenummer_kind),
            "datumIngangOnderzoek": {
                "dag": int(
                    kind.datum_ingang_onderzoek[settings.DAY_START : settings.DAY_END]
                )
                if kind.datum_ingang_onderzoek
                else 0,
                "datum": kind.datum_ingang_onderzoek,
                "jaar": int(
                    kind.datum_ingang_onderzoek[settings.YEAR_START : settings.YEAR_END]
                )
                if kind.datum_ingang_onderzoek
                else 0,
                "maand": int(
                    kind.datum_ingang_onderzoek[
                        settings.MONTH_START : settings.MONTH_END
                    ]
                )
                if kind.datum_ingang_onderzoek
                else 0,
            },
        },
    }

    return kind_dict
