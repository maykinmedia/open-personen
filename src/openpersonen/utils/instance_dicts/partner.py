from django.conf import settings

import xmltodict

from openpersonen.features.country_code_and_omschrijving.models import (
    CountryCodeAndOmschrijving,
)
from openpersonen.features.gemeente_code_and_omschrijving.models import (
    GemeenteCodeAndOmschrijving,
)
from openpersonen.utils.helpers import convert_empty_instances


def get_partner_instance_dict(instance_xml_dict):
    partner_dict = {
        "burgerservicenummer": instance_xml_dict.get("inp.bsn", "string"),
        "geslachtsaanduiding": instance_xml_dict.get("geslachtsaanduiding", "string"),
        "soortVerbintenis": instance_xml_dict.get("inp.soortVerbintenis", "string"),
        "naam": {
            "geslachtsnaam": instance_xml_dict.get("gerelateerde", {}).get(
                "geslachtsnaam"
            ),
            "voorletters": instance_xml_dict.get("gerelateerde", {}).get("voorletters"),
            "voornamen": instance_xml_dict.get("gerelateerde", {}).get("voornamen"),
            "voorvoegsel": instance_xml_dict.get("gerelateerde", {}).get(
                "voorvoegselGeslachtsnaam"
            ),
            "inOnderzoek": {
                "geslachtsnaam": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                    ]
                ),
                "voornamen": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                    ]
                ),
                "voorvoegsel": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
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
                    instance_xml_dict.get("geboortedatum", "19000101")[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                ),
                "datum": instance_xml_dict.get("geboortedatum", "19000101"),
                "jaar": int(
                    instance_xml_dict.get("geboortedatum", "19000101")[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                ),
                "maand": int(
                    instance_xml_dict.get("geboortedatum", "19000101")[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                ),
            },
            "land": {
                "code": instance_xml_dict.get("inp.geboorteLand", "string"),
                "omschrijving": CountryCodeAndOmschrijving.get_omschrijving_from_code(
                    instance_xml_dict.get("inp.geboorteLand", 0)
                ),
            },
            "plaats": {
                "code": instance_xml_dict.get("inp.geboorteplaats", "string"),
                "omschrijving": GemeenteCodeAndOmschrijving.get_omschrijving_from_code(
                    instance_xml_dict.get("inp.geboorteplaats", 0)
                ),
            },
            "inOnderzoek": {
                "datum": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                    ]
                ),
                "land": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                    ]
                ),
                "plaats": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
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
                    for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                ]
            ),
            "geslachtsaanduiding": any(
                [
                    "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                    for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
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
                    instance_xml_dict.get("datumSluiting", "19000101")[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                ),
                "datum": instance_xml_dict.get("datumSluiting", "19000101"),
                "jaar": int(
                    instance_xml_dict.get("datumSluiting", "19000101")[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                ),
                "maand": int(
                    instance_xml_dict.get("datumSluiting", "19000101")[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                ),
            },
            "land": {
                "code": instance_xml_dict.get("landSluiting", "string"),
                "omschrijving": CountryCodeAndOmschrijving.get_omschrijving_from_code(
                    instance_xml_dict.get("landSluiting", 0)
                ),
            },
            "plaats": {
                "code": instance_xml_dict.get("plaatsSluiting", "string"),
                "omschrijving": GemeenteCodeAndOmschrijving.get_omschrijving_from_code(
                    instance_xml_dict.get("plaatsSluiting", 0)
                ),
            },
            "inOnderzoek": {
                "datum": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                    ]
                ),
                "land": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                    ]
                ),
                "plaats": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
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

    convert_empty_instances(partner_dict)

    return partner_dict


def convert_xml_to_partner_dict(xml, id=None):
    dict_object = xmltodict.parse(
        xml,
        process_namespaces=True,
        namespaces={
            "http://schemas.xmlsoap.org/soap/envelope/": None,
            "http://www.egem.nl/StUF/sector/bg/0310": None,
        },
    )

    antwoord_object = dict_object["Envelope"]["Body"]["npsLa01"]["antwoord"]["object"][
        "inp.heeftAlsEchtgenootPartner"
    ]

    result = []
    if isinstance(antwoord_object, list):
        for antwood_dict in antwoord_object:
            result_dict = get_partner_instance_dict(antwood_dict["gerelateerde"])
            if not id or id == result_dict["burgerservicenummer"]:
                result.append(result_dict)
    else:
        result.append(get_partner_instance_dict(antwoord_object["gerelateerde"]))
        if id and result[0]["burgerservicenummer"] != id:
            result = []

    return result
