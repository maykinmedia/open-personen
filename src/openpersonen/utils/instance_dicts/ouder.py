from django.conf import settings

from openpersonen.features.country_code_and_omschrijving.models import (
    CountryCodeAndOmschrijving,
)
from openpersonen.features.gemeente_code_and_omschrijving.models import (
    GemeenteCodeAndOmschrijving,
)
from openpersonen.utils.converters import convert_xml_to_dict
from openpersonen.utils.helpers import convert_empty_instances


def get_ouder_instance_dict(instance_xml_dict):
    ouder_dict = {
        "burgerservicenummer": instance_xml_dict.get("inp.bsn", "string"),
        "geslachtsaanduiding": instance_xml_dict.get("geslachtsaanduiding", "string"),
        "ouderAanduiding": instance_xml_dict.get("ouderAanduiding", "string"),
        "datumIngangFamilierechtelijkeBetrekking": {
            "dag": int(
                instance_xml_dict.get(
                    "datumIngangFamilierechtelijkeBetrekking", "19000101"
                )[settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END]
            )
            if not isinstance(
                instance_xml_dict.get(
                    "datumIngangFamilierechtelijkeBetrekking"
                ),
                dict,
            )
            else 1,
            "datum": instance_xml_dict.get(
                "datumIngangFamilierechtelijkeBetrekking", "string"
            ),
            "jaar": int(
                instance_xml_dict.get(
                    "datumIngangFamilierechtelijkeBetrekking", "19000101"
                )[settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END]
            )
            if not isinstance(
                instance_xml_dict.get(
                    "datumIngangFamilierechtelijkeBetrekking"
                ),
                dict,
            )
            else 1900,
            "maand": int(
                instance_xml_dict.get(
                    "datumIngangFamilierechtelijkeBetrekking", "19000101"
                )[settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END]
            )
            if not isinstance(
                instance_xml_dict.get(
                    "datumIngangFamilierechtelijkeBetrekking"
                ),
                dict,
            )
            else 1,
        },
        "naam": {
            "geslachtsnaam": instance_xml_dict.get("gerelateerde", {}).get(
                "geslachtsnaam", "string"
            ),
            "voorletters": instance_xml_dict.get("gerelateerde", {}).get(
                "voorletters", "string"
            ),
            "voornamen": instance_xml_dict.get("gerelateerde", {}).get(
                "voornamen", "string"
            ),
            "voorvoegsel": instance_xml_dict.get("gerelateerde", {}).get(
                "voorvoegselGeslachtsnaam", "string"
            ),
            "inOnderzoek": {
                "geslachtsnaam": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "voornamen": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "voorvoegsel": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
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
                    if isinstance(in_onderzoek, dict)
                ]
            ),
            "datumIngangFamilierechtelijkeBetrekking": "01-01-1990",
            "geslachtsaanduiding": any(
                [
                    "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                    for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                    if isinstance(in_onderzoek, dict)
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
                    instance_xml_dict.get("geboortedatum", "19000101")[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                ),
                "datum": instance_xml_dict.get("geboortedatum", "string")
                if not isinstance(
                    instance_xml_dict.get("geboortedatum"), dict
                )
                else 1
                ,
                "jaar": int(
                    instance_xml_dict.get("geboortedatum", "19000101")[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                )
                if not isinstance(
                    instance_xml_dict.get("geboortedatum"), dict
                )
                else 1900,
                "maand": int(
                    instance_xml_dict.get("geboortedatum", "19000101")[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                )
                if not isinstance(
                    instance_xml_dict.get("geboortedatum"), dict
                )
                else 1,
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
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "land": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "plaats": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
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


def convert_xml_to_ouder_dict(xml, id=None):
    dict_object = convert_xml_to_dict(xml)

    antwoord_object = dict_object["Envelope"]["Body"]["npsLa01"]["antwoord"]["object"][
        "inp.heeftAlsOuders"
    ]

    result = []
    if isinstance(antwoord_object, list):
        for antwood_dict in antwoord_object:
            result_dict = get_ouder_instance_dict(antwood_dict["gerelateerde"])
            if not id or id == result_dict["burgerservicenummer"]:
                result.append(result_dict)
    else:
        result.append(get_ouder_instance_dict(antwoord_object["gerelateerde"]))
        if id and result[0]["burgerservicenummer"] != id:
            result = []

    return result
