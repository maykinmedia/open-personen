from django.conf import settings

from openpersonen.utils.helpers import convert_empty_instances


def get_partner_instance_dict(instance_xml_dict, prefix):
    partner_dict = {
        "burgerservicenummer": instance_xml_dict.get(f"{prefix}:inp.bsn", "string"),
        "geslachtsaanduiding": instance_xml_dict.get(
            f"{prefix}:geslachtsaanduiding", "string"
        ),
        "soortVerbintenis": instance_xml_dict.get(
            f"{prefix}:soortVerbintenis", "string"
        ),
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
        "inOnderzoek": {
            "burgerservicenummer": bool(
                instance_xml_dict.get(f"{prefix}:inp.bsn", "string")
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
        "aangaanHuwelijkPartnerschap": {
            "datum": {"dag": 0, "datum": "string", "jaar": 0, "maand": 0},
            "land": {"code": "0000", "omschrijving": "string"},
            "plaats": {"code": "0000", "omschrijving": "string"},
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
        "geheimhoudingPersoonsgegevens": True,
    }

    convert_empty_instances(partner_dict)

    return partner_dict
