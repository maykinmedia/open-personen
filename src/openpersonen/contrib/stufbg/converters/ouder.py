from django.conf import settings

import xmltodict

from openpersonen.contrib.utils import convert_empty_instances
from openpersonen.features.country_code.models import CountryCode


def get_ouder_instance_dict(instance_xml_dict, prefix):
    ouder_dict = {
        "burgerservicenummer": instance_xml_dict.get(f"{prefix}:inp.bsn", "string"),
        "geslachtsaanduiding": instance_xml_dict.get(
            f"{prefix}:geslachtsaanduiding", "string"
        ),
        "ouderAanduiding": instance_xml_dict.get(f"{prefix}:ouderAanduiding", "string"),
        "datumIngangFamilierechtelijkeBetrekking": {
            "dag": int(
                instance_xml_dict.get(
                    f"{prefix}:datumIngangFamilierechtelijkeBetrekking", "19000101"
                )[settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END]
            ),
            "datum": instance_xml_dict.get(
                f"{prefix}:datumIngangFamilierechtelijkeBetrekking", "string"
            ),
            "jaar": int(
                instance_xml_dict.get(
                    f"{prefix}:datumIngangFamilierechtelijkeBetrekking", "19000101"
                )[settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END]
            ),
            "maand": int(
                instance_xml_dict.get(
                    f"{prefix}:datumIngangFamilierechtelijkeBetrekking", "19000101"
                )[settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END]
            ),
        },
        "naam": {
            "geslachtsnaam": instance_xml_dict.get("gerelateerde", {}).get(
                f"{prefix}:geslachtsnaam", "string"
            ),
            "voorletters": instance_xml_dict.get("gerelateerde", {}).get(
                f"{prefix}:voorletters", "string"
            ),
            "voornamen": instance_xml_dict.get("gerelateerde", {}).get(
                f"{prefix}:voornamen", "string"
            ),
            "voorvoegsel": instance_xml_dict.get("gerelateerde", {}).get(
                f"{prefix}:voorvoegselGeslachtsnaam", "string"
            ),
            "inOnderzoek": {
                "geslachtsnaam": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get(
                            f"{prefix}:inOnderzoek", []
                        )
                    ]
                ),
                "voornamen": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get(
                            f"{prefix}:inOnderzoek", []
                        )
                    ]
                ),
                "voorvoegsel": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get(
                            f"{prefix}:inOnderzoek", []
                        )
                    ]
                ),
                "datumIngangOnderzoek": {
                    "dag": 1,
                    "datum": "01-01-1900",
                    "jaar": 1900,
                    "maand": 1,
                },
            },
        },
        "inOnderzoek": {
            "burgerservicenummer": any(
                [
                    "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                    for in_onderzoek in instance_xml_dict.get(
                        f"{prefix}:inOnderzoek", []
                    )
                ]
            ),
            "datumIngangFamilierechtelijkeBetrekking": "01-01-1990",
            "geslachtsaanduiding": any(
                [
                    "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                    for in_onderzoek in instance_xml_dict.get(
                        f"{prefix}:inOnderzoek", []
                    )
                ]
            ),
            "datumIngangOnderzoek": {
                "dag": 1,
                "datum": "01-01-1990",
                "jaar": 1900,
                "maand": 1,
            },
        },
        "geboorte": {
            "datum": {
                "dag": int(
                    instance_xml_dict.get(f"{prefix}:geboortedatum", "19000101")[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                ),
                "datum": instance_xml_dict.get(f"{prefix}:geboortedatum", "string"),
                "jaar": int(
                    instance_xml_dict.get(f"{prefix}:geboortedatum", "19000101")[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                ),
                "maand": int(
                    instance_xml_dict.get(f"{prefix}:geboortedatum", "19000101")[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                ),
            },
            "land": {
                "code": instance_xml_dict.get(f"{prefix}:inp.geboorteLand", "string"),
                "omschrijving": CountryCode.get_omschrijving_from_code(
                    instance_xml_dict.get(f"{prefix}:inp.geboorteLand", 0)
                ),
            },
            "plaats": {
                "code": instance_xml_dict.get(f"{prefix}:inp.geboorteplaats", "string"),
                "omschrijving": instance_xml_dict.get(
                    f"{prefix}:inp.geboorteplaats", "string"
                ),
            },
            "inOnderzoek": {
                "datum": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get(
                            f"{prefix}:inOnderzoek", []
                        )
                    ]
                ),
                "land": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get(
                            f"{prefix}:inOnderzoek", []
                        )
                    ]
                ),
                "plaats": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get(
                            f"{prefix}:inOnderzoek", []
                        )
                    ]
                ),
                "datumIngangOnderzoek": {
                    "dag": 1,
                    "datum": "01-01-1900",
                    "jaar": 1900,
                    "maand": 1,
                },
            },
        },
        "geheimhoudingPersoonsgegevens": instance_xml_dict.get(
            "inp.indicatieGeheim", False
        ),
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
            result_dict = get_ouder_instance_dict(
                antwood_dict[f"{prefix}:gerelateerde"], prefix
            )
            if not id or id == result_dict["burgerservicenummer"]:
                result.append(result_dict)
    else:
        result.append(
            get_ouder_instance_dict(antwoord_object[f"{prefix}:gerelateerde"], prefix)
        )
        if id and result[0]["burgerservicenummer"] != id:
            result = []

    return result
