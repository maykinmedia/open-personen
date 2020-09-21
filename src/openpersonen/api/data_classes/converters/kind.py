from django.conf import settings

import xmltodict

from openpersonen.api.utils import (
    calculate_age,
    convert_empty_instances,
    is_valid_date_format,
)


def convert_client_response_to_instance_dict(response):
    dict_object = xmltodict.parse(response.content)

    try:
        antwoord_dict_object = dict_object["soapenv:Envelope"]["soapenv:Body"][
            "ns:npsLa01"
        ]["ns:antwoord"]["ns:object"]
        prefix = "ns"
    except KeyError:
        antwoord_dict_object = dict_object["env:Envelope"]["env:Body"]["npsLa01"][
            "BG:antwoord"
        ]["BG:object"]["BG:inp.heeftAlsKinderen"]["BG:gerelateerde"]
        prefix = "BG"

    kind_dict = {
        "burgerservicenummer": antwoord_dict_object.get(f"{prefix}:inp.bsn", "string"),
        "geheimhoudingPersoonsgegevens": True,
        "naam": {
            "geslachtsnaam": antwoord_dict_object.get(
                f"{prefix}:geslachtsnaam", "string"
            ),
            "voorletters": antwoord_dict_object.get(f"{prefix}:voorletters", "string"),
            "voornamen": antwoord_dict_object.get(f"{prefix}:voornamen", "string"),
            "voorvoegsel": antwoord_dict_object.get(
                f"{prefix}:voorvoegselGeslachtsnaam", "string"
            ),
            "inOnderzoek": {
                "geslachtsnaam": bool(
                    antwoord_dict_object.get(f"{prefix}:geslachtsnaam", "string")
                ),
                "voornamen": bool(
                    antwoord_dict_object.get(f"{prefix}:voornamen", "string")
                ),
                "voorvoegsel": bool(
                    antwoord_dict_object.get(
                        f"{prefix}:voorvoegselGeslachtsnaam", "string"
                    )
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
                    antwoord_dict_object.get(f"{prefix}:geboortedatum", "00000000")[
                        settings.DAY_START : settings.DAY_END
                    ]
                ),
                "datum": antwoord_dict_object.get(f"{prefix}:geboortedatum", "string"),
                "jaar": int(
                    antwoord_dict_object.get(f"{prefix}:geboortedatum", "00000000")[
                        settings.YEAR_START : settings.YEAR_END
                    ]
                ),
                "maand": int(
                    antwoord_dict_object.get(f"{prefix}:geboortedatum", "00000000")[
                        settings.MONTH_START : settings.MONTH_END
                    ]
                ),
            },
            "land": {
                "code": "string",
                "omschrijving": antwoord_dict_object.get(
                    f"{prefix}:inp.geboorteLand", "string"
                ),
            },
            "plaats": {
                "code": "string",
                "omschrijving": antwoord_dict_object.get(
                    f"{prefix}:inp.geboorteplaats", "string"
                ),
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
        "leeftijd": calculate_age(antwoord_dict_object.get(f"{prefix}:geboortedatum", "string")),
        "inOnderzoek": {
            "burgerservicenummer": bool(
                antwoord_dict_object.get(f"{prefix}:inp.bsn", "string")
            ),
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
                if is_valid_date_format(kind.geboortedatum_kind)
                else 0,
                "datum": kind.geboortedatum_kind,
                "jaar": int(
                    kind.geboortedatum_kind[settings.YEAR_START : settings.YEAR_END]
                )
                if is_valid_date_format(kind.geboortedatum_kind)
                else 0,
                "maand": int(
                    kind.geboortedatum_kind[settings.MONTH_START : settings.MONTH_END]
                )
                if is_valid_date_format(kind.geboortedatum_kind)
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
        "leeftijd": calculate_age(kind.geboortedatum_kind),
        "inOnderzoek": {
            "burgerservicenummer": bool(kind.burgerservicenummer_kind),
            "datumIngangOnderzoek": {
                "dag": int(
                    kind.datum_ingang_onderzoek[settings.DAY_START : settings.DAY_END]
                )
                if is_valid_date_format(kind.datum_ingang_onderzoek)
                else 0,
                "datum": kind.datum_ingang_onderzoek,
                "jaar": int(
                    kind.datum_ingang_onderzoek[settings.YEAR_START : settings.YEAR_END]
                )
                if is_valid_date_format(kind.datum_ingang_onderzoek)
                else 0,
                "maand": int(
                    kind.datum_ingang_onderzoek[
                        settings.MONTH_START : settings.MONTH_END
                    ]
                )
                if is_valid_date_format(kind.datum_ingang_onderzoek)
                else 0,
            },
        },
    }

    return kind_dict
