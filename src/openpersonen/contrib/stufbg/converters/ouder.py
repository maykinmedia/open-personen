from django.conf import settings

import xmltodict

from openpersonen.api.utils import convert_empty_instances, is_valid_date_format


def _get_client_instance_dict(instance_xml_dict, prefix):
    ouder_dict = {
        "burgerservicenummer": instance_xml_dict.get(f"{prefix}:inp.bsn", "string"),
        "geslachtsaanduiding": instance_xml_dict.get(
            f"{prefix}:geslachtsaanduiding", "string"
        ),
        "ouderAanduiding": instance_xml_dict.get(f"{prefix}:ouderAanduiding", "string"),
        "datumIngangFamilierechtelijkeBetrekking": {
            "dag": int(
                instance_xml_dict.get(
                    f"{prefix}:datumIngangFamilierechtelijkeBetrekking", "00000000"
                )[settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END]
            ),
            "datum": instance_xml_dict.get(
                f"{prefix}:datumIngangFamilierechtelijkeBetrekking", "string"
            ),
            "jaar": int(
                instance_xml_dict.get(
                    f"{prefix}:datumIngangFamilierechtelijkeBetrekking", "00000000"
                )[settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END]
            ),
            "maand": int(
                instance_xml_dict.get(
                    f"{prefix}:datumIngangFamilierechtelijkeBetrekking", "00000000"
                )[settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END]
            ),
        },
        "naam": {
            "geslachtsnaam": instance_xml_dict.get(f"{prefix}:geslachtsnaam", "string"),
            "voorletters": instance_xml_dict.get(f"{prefix}:voorletters", "string"),
            "voornamen": instance_xml_dict.get(f"{prefix}:voornamen", "string"),
            "voorvoegsel": instance_xml_dict.get(
                f"{prefix}:voorvoegselGeslachtsnaam", "string"
            ),
            "inOnderzoek": {
                "geslachtsnaam": bool(
                    instance_xml_dict.get(f"{prefix}:geslachtsnaam", "string")
                ),
                "voornamen": bool(
                    instance_xml_dict.get(f"{prefix}:voornamen", "string")
                ),
                "voorvoegsel": bool(
                    instance_xml_dict.get(
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
                instance_xml_dict.get(f"{prefix}:inp.bsn", "string")
            ),
            "datumIngangFamilierechtelijkeBetrekking": bool(
                instance_xml_dict.get(
                    f"{prefix}:datumIngangFamilierechtelijkeBetrekking", "string"
                )
            ),
            "geslachtsaanduiding": bool(
                instance_xml_dict.get(f"{prefix}:geslachtsaanduiding", "string")
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
                    instance_xml_dict.get(f"{prefix}:geboortedatum", "00000000")[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                ),
                "datum": instance_xml_dict.get(f"{prefix}:geboortedatum", "string"),
                "jaar": int(
                    instance_xml_dict.get(f"{prefix}:geboortedatum", "00000000")[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                ),
                "maand": int(
                    instance_xml_dict.get(f"{prefix}:geboortedatum", "00000000")[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                ),
            },
            "land": {
                "code": "0000",
                "omschrijving": instance_xml_dict.get(
                    f"{prefix}:inp.geboorteLand", "string"
                ),
            },
            "plaats": {
                "code": "0000",
                "omschrijving": instance_xml_dict.get(
                    f"{prefix}:inp.geboorteplaats", "string"
                ),
            },
            "inOnderzoek": {
                "datum": bool(
                    instance_xml_dict.get(f"{prefix}:geboortedatum", "string")
                ),
                "land": bool(
                    instance_xml_dict.get(f"{prefix}:inp.geboorteLand", "string")
                ),
                "plaats": bool(
                    instance_xml_dict.get(f"{prefix}:inp.geboorteplaats", "string")
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


def convert_response_to_ouder_dict(response, id=None):
    dict_object = xmltodict.parse(response.content)

    try:
        antwoord_object = dict_object["soapenv:Envelope"]["soapenv:Body"]["ns:npsLa01"][
            "ns:antwoord"
        ]["ns:object"]["ns:inp.heeftAlsOuders"]
        prefix = "ns"
    except KeyError:
        antwoord_object = dict_object["env:Envelope"]["env:Body"]["npsLa01"][
            "BG:antwoord"
        ]["object"]["BG:inp.heeftAlsOuders"]
        prefix = "BG"

    result = []
    if isinstance(antwoord_object, list):
        for antwood_dict in antwoord_object:
            result_dict = _get_client_instance_dict(
                antwood_dict[f"{prefix}:gerelateerde"], prefix
            )
            if not id or id == result_dict["burgerservicenummer"]:
                result.append(result_dict)
    else:
        result.append(
            _get_client_instance_dict(antwoord_object[f"{prefix}:gerelateerde"], prefix)
        )
        if id and result[0]["burgerservicenummer"] != id:
            result = []

    return result
