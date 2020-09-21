from django.conf import settings

import xmltodict

from openpersonen.api.utils import convert_empty_instances, is_valid_date_format


def convert_client_response_to_instance_dict(response):
    dict_object = xmltodict.parse(response.content)

    try:
        antwoord_dict_object = dict_object["soapenv:Envelope"]["soapenv:Body"][
            "ns:npsLa01"
        ]["ns:antwoord"]["ns:object"]["ns:inp.heeftAlsOuders"]["ns:gerelateerde"]
        prefix = "ns"
    except KeyError:
        antwoord_dict_object = dict_object["env:Envelope"]["env:Body"]["npsLa01"][
            "BG:antwoord"
        ]["BG:object"]["BG:inp.heeftAlsOuders"]["BG:gerelateerde"]
        prefix = "BG"

    ouder_dict = {
        "burgerservicenummer": antwoord_dict_object.get(f"{prefix}:inp.bsn", "string"),
        "geslachtsaanduiding": antwoord_dict_object.get(
            f"{prefix}:geslachtsaanduiding", "string"
        ),
        "ouderAanduiding": antwoord_dict_object.get(
            f"{prefix}:ouderAanduiding", "string"
        ),
        "datumIngangFamilierechtelijkeBetrekking": {
            "dag": int(
                antwoord_dict_object.get(
                    f"{prefix}:datumIngangFamilierechtelijkeBetrekking", "00000000"
                )[settings.DAY_START : settings.DAY_END]
            ),
            "datum": antwoord_dict_object.get(
                f"{prefix}:datumIngangFamilierechtelijkeBetrekking", "string"
            ),
            "jaar": int(
                antwoord_dict_object.get(
                    f"{prefix}:datumIngangFamilierechtelijkeBetrekking", "00000000"
                )[settings.YEAR_START : settings.YEAR_END]
            ),
            "maand": int(
                antwoord_dict_object.get(
                    f"{prefix}:datumIngangFamilierechtelijkeBetrekking", "00000000"
                )[settings.MONTH_START : settings.MONTH_END]
            ),
        },
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
        "inOnderzoek": {
            "burgerservicenummer": bool(
                antwoord_dict_object.get(f"{prefix}:inp.bsn", "string")
            ),
            "datumIngangFamilierechtelijkeBetrekking": bool(
                antwoord_dict_object.get(
                    f"{prefix}:datumIngangFamilierechtelijkeBetrekking", "string"
                )
            ),
            "geslachtsaanduiding": bool(
                antwoord_dict_object.get(f"{prefix}:geslachtsaanduiding", "string")
            ),
            "datumIngangOnderzoek": {
                "dag": 0,
                "datum": "string",
                "jaar": 0,
                "maand": 0,
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
                "code": "0000",
                "omschrijving": antwoord_dict_object.get(
                    f"{prefix}:inp.geboorteLand", "string"
                ),
            },
            "plaats": {
                "code": "0000",
                "omschrijving": antwoord_dict_object.get(
                    f"{prefix}:inp.geboorteplaats", "string"
                ),
            },
            "inOnderzoek": {
                "datum": bool(
                    antwoord_dict_object.get(f"{prefix}:geboortedatum", "string")
                ),
                "land": bool(
                    antwoord_dict_object.get(f"{prefix}:inp.geboorteLand", "string")
                ),
                "plaats": bool(
                    antwoord_dict_object.get(f"{prefix}:inp.geboorteplaats", "string")
                ),
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0,
                },
            },
        },
        "geheimhoudingPersoonsgegevens": True,
    }

    convert_empty_instances(ouder_dict)

    return ouder_dict


def convert_model_instance_to_instance_dict(ouder):
    ouder_dict = {
        "burgerservicenummer": ouder.burgerservicenummer_ouder,
        "geslachtsaanduiding": ouder.geslachtsaanduiding_ouder,
        "ouderAanduiding": ouder.geslachtsaanduiding_ouder,
        "datumIngangFamilierechtelijkeBetrekking": {
            "dag": int(
                ouder.datum_ingang_familierechtelijke_betrekking_ouder[
                    settings.DAY_START : settings.DAY_END
                ]
                if is_valid_date_format(
                    ouder.datum_ingang_familierechtelijke_betrekking_ouder
                )
                else 0
            ),
            "datum": ouder.datum_ingang_familierechtelijke_betrekking_ouder,
            "jaar": int(
                ouder.datum_ingang_familierechtelijke_betrekking_ouder[
                    settings.YEAR_START : settings.YEAR_END
                ]
                if is_valid_date_format(
                    ouder.datum_ingang_familierechtelijke_betrekking_ouder
                )
                else 0
            ),
            "maand": int(
                ouder.datum_ingang_familierechtelijke_betrekking_ouder[
                    settings.MONTH_START : settings.MONTH_END
                ]
                if is_valid_date_format(
                    ouder.datum_ingang_familierechtelijke_betrekking_ouder
                )
                else 0
            ),
        },
        "naam": {
            "geslachtsnaam": ouder.geslachtsnaam_ouder,
            "voorletters": "string",
            "voornamen": ouder.voornamen_ouder,
            "voorvoegsel": ouder.voorvoegsel_geslachtsnaam_ouder,
            "inOnderzoek": {
                "geslachtsnaam": bool(ouder.geslachtsnaam_ouder),
                "voornamen": bool(ouder.voornamen_ouder),
                "voorvoegsel": bool(ouder.voorvoegsel_geslachtsnaam_ouder),
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0,
                },
            },
        },
        "inOnderzoek": {
            "burgerservicenummer": bool(ouder.burgerservicenummer_ouder),
            "datumIngangFamilierechtelijkeBetrekking": bool(
                ouder.datum_ingang_familierechtelijke_betrekking_ouder
            ),
            "geslachtsaanduiding": bool(ouder.geslachtsaanduiding_ouder),
            "datumIngangOnderzoek": {
                "dag": int(
                    ouder.datum_ingang_onderzoek[settings.DAY_START : settings.DAY_END]
                    if is_valid_date_format(ouder.datum_ingang_onderzoek)
                    else 0
                ),
                "datum": ouder.datum_ingang_onderzoek,
                "jaar": int(
                    ouder.datum_ingang_onderzoek[
                        settings.YEAR_START : settings.YEAR_END
                    ]
                    if is_valid_date_format(ouder.datum_ingang_onderzoek)
                    else 0
                ),
                "maand": int(
                    ouder.datum_ingang_onderzoek[
                        settings.MONTH_START : settings.MONTH_END
                    ]
                    if is_valid_date_format(ouder.datum_ingang_onderzoek)
                    else 0
                ),
            },
        },
        "geboorte": {
            "datum": {
                "dag": int(
                    ouder.geboortedatum_ouder[settings.DAY_START : settings.DAY_END]
                )
                if is_valid_date_format(ouder.geboortedatum_ouder)
                else 0,
                "datum": ouder.geboortedatum_ouder,
                "jaar": int(
                    ouder.geboortedatum_ouder[settings.YEAR_START : settings.YEAR_END]
                )
                if is_valid_date_format(ouder.geboortedatum_ouder)
                else 0,
                "maand": int(
                    ouder.geboortedatum_ouder[settings.MONTH_START : settings.MONTH_END]
                )
                if is_valid_date_format(ouder.geboortedatum_ouder)
                else 0,
            },
            "land": {
                "code": "0000",
                "omschrijving": ouder.geboorteland_ouder,
            },
            "plaats": {
                "code": "0000",
                "omschrijving": ouder.geboorteplaats_ouder,
            },
            "inOnderzoek": {
                "datum": bool(ouder.geboortedatum_ouder),
                "land": bool(ouder.geboorteland_ouder),
                "plaats": bool(ouder.geboorteplaats_ouder),
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0,
                },
            },
        },
        "geheimhoudingPersoonsgegevens": True,
    }

    return ouder_dict
