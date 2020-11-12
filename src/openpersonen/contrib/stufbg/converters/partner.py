import xmltodict

from openpersonen.contrib.utils import convert_empty_instances
from openpersonen.features.country_code_and_omschrijving.models import (
    CountryCodeAndOmschrijving,
)
from openpersonen.features.gemeente_code_and_omschrijving.models import (
    GemeenteCodeAndOmschrijving,
)


def get_partner_instance_dict(instance_xml_dict, prefix):
    partner_dict = {
        "burgerservicenummer": instance_xml_dict.get(f"{prefix}:inp.bsn", "string"),
        "geslachtsaanduiding": instance_xml_dict.get(
            f"{prefix}:geslachtsaanduiding", "string"
        ),
        "soortVerbintenis": instance_xml_dict.get(
            f"{prefix}:inp.soortVerbintenis", "string"
        ),
        "naam": {
            "geslachtsnaam": instance_xml_dict.get(f"{prefix}:gerelateerde", {}).get(
                "geslachtsnaam"
            ),
            "voorletters": instance_xml_dict.get(f"{prefix}:gerelateerde", {}).get(
                "voorletters"
            ),
            "voornamen": instance_xml_dict.get(f"{prefix}:gerelateerde", {}).get(
                "voornamen"
            ),
            "voorvoegsel": instance_xml_dict.get(f"{prefix}:gerelateerde", {}).get(
                "voorvoegselGeslachtsnaam"
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
        "geboorte": {
            "datum": {
                "dag": int(
                    instance_xml_dict.get(f"{prefix}:geboortedatum", "19000101")[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                ),
                "datum": instance_xml_dict.get(f"{prefix}:geboortedatum", "19000101"),
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
                "omschrijving": CountryCodeAndOmschrijving.get_omschrijving_from_code(
                    instance_xml_dict.get(f"{prefix}:inp.geboorteLand", 0)
                ),
            },
            "plaats": {
                "code": instance_xml_dict.get(f"{prefix}:inp.geboorteplaats", "string"),
                "omschrijving": GemeenteCodeAndOmschrijving.get_omschrijving_from_code(
                    instance_xml_dict.get(f"{prefix}:inp.geboorteplaats", 0)
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
        "inOnderzoek": {
            "burgerservicenummer": any(
                [
                    "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                    for in_onderzoek in instance_xml_dict.get(
                        f"{prefix}:inOnderzoek", []
                    )
                ]
            ),
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
                "datum": "01-01-1900",
                "jaar": 1900,
                "maand": 1,
            },
        },
        "aangaanHuwelijkPartnerschap": {
            "datum": {
                "dag": int(
                    instance_xml_dict.get(f"{prefix}:datumSluiting", "19000101")[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                ),
                "datum": instance_xml_dict.get(f"{prefix}:datumSluiting", "19000101"),
                "jaar": int(
                    instance_xml_dict.get(f"{prefix}:datumSluiting", "19000101")[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                ),
                "maand": int(
                    instance_xml_dict.get(f"{prefix}:datumSluiting", "19000101")[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                ),
            },
            "land": {
                "code": instance_xml_dict.get(f"{prefix}:landSluiting", "string"),
                "omschrijving": CountryCodeAndOmschrijving.get_omschrijving_from_code(
                    instance_xml_dict.get(f"{prefix}:landSluiting", 0)
                ),
            },
            "plaats": {
                "code": instance_xml_dict.get(f"{prefix}:plaatsSluiting", "string"),
                "omschrijving": GemeenteCodeAndOmschrijving.get_omschrijving_from_code(
                    instance_xml_dict.get(f"{prefix}:plaatsSluiting", 0)
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
            f"{prefix}:inp.indicatieGeheim", False
        ),
    }

    convert_empty_instances(partner_dict)

    return partner_dict


def convert_response_to_partner_dict(response, id=None):
    dict_object = xmltodict.parse(response.content)

    try:
        antwoord_object = dict_object["soapenv:Envelope"]["soapenv:Body"]["ns:npsLa01"][
            "ns:antwoord"
        ]["ns:object"]["ns:inp.heeftAlsEchtgenootPartner"]
        prefix = "ns"
    except KeyError:
        antwoord_object = dict_object["env:Envelope"]["env:Body"]["npsLa01"][
            "BG:antwoord"
        ]["object"]["BG:inp.heeftAlsEchtgenootPartner"]
        prefix = "BG"

    result = []
    if isinstance(antwoord_object, list):
        for antwood_dict in antwoord_object:
            result_dict = get_partner_instance_dict(
                antwood_dict[f"{prefix}:gerelateerde"], prefix
            )
            if not id or id == result_dict["burgerservicenummer"]:
                result.append(result_dict)
    else:
        result.append(
            get_partner_instance_dict(antwoord_object[f"{prefix}:gerelateerde"], prefix)
        )
        if id and result[0]["burgerservicenummer"] != id:
            result = []

    return result
