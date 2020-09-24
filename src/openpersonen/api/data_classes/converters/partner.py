from django.conf import settings

import xmltodict

from openpersonen.api.utils import convert_empty_instances, is_valid_date_format


def _get_client_instance_dict(instance_xml_dict, prefix):
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
                        settings.DAY_START : settings.DAY_END
                    ]
                ),
                "datum": instance_xml_dict.get(f"{prefix}:geboortedatum", "string"),
                "jaar": int(
                    instance_xml_dict.get(f"{prefix}:geboortedatum", "00000000")[
                        settings.YEAR_START : settings.YEAR_END
                    ]
                ),
                "maand": int(
                    instance_xml_dict.get(f"{prefix}:geboortedatum", "00000000")[
                        settings.MONTH_START : settings.MONTH_END
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


def convert_client_response(response, id=None):
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

    if isinstance(antwoord_object, list):
        result = []
        for antwood_dict in antwoord_object:
            result_dict = _get_client_instance_dict(
                antwood_dict[f"{prefix}:gerelateerde"], prefix
            )
            if not id or id == result_dict["burgerservicenummer"]:
                result.append(result_dict)
    else:
        result = _get_client_instance_dict(
            antwoord_object[f"{prefix}:gerelateerde"], prefix
        )
        if id and result["burgerservicenummer"] != id:
            result = {}

    return result


def convert_model_instance_to_instance_dict(partner):

    partner_dict = {
        "burgerservicenummer": partner.burgerservicenummer_echtgenoot_geregistreerd_partner,
        "geslachtsaanduiding": partner.geslachtsaanduiding_echtgenoot_geregistreerd_partner,
        "soortVerbintenis": partner.soort_verbintenis,
        "naam": {
            "geslachtsnaam": partner.geslachtsnaam_echtgenoot_geregistreerd_partner,
            "voorletters": "string",
            "voornamen": partner.voornamen_echtgenoot_geregistreerd_partner,
            "voorvoegsel": partner.voorvoegsel_geslachtsnaam_echtgenoot_geregistreerd_partner,
            "inOnderzoek": {
                "geslachtsnaam": bool(
                    partner.geslachtsnaam_echtgenoot_geregistreerd_partner
                ),
                "voornamen": bool(partner.voornamen_echtgenoot_geregistreerd_partner),
                "voorvoegsel": bool(
                    partner.voorvoegsel_geslachtsnaam_echtgenoot_geregistreerd_partner,
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
                    partner.geboortedatum_echtgenoot_geregistreerd_partner[
                        settings.DAY_START : settings.DAY_END
                    ]
                    if is_valid_date_format(
                        partner.geboortedatum_echtgenoot_geregistreerd_partner
                    )
                    else 0
                ),
                "datum": partner.geboortedatum_echtgenoot_geregistreerd_partner,
                "jaar": int(
                    partner.geboortedatum_echtgenoot_geregistreerd_partner[
                        settings.YEAR_START : settings.YEAR_END
                    ]
                    if is_valid_date_format(
                        partner.geboortedatum_echtgenoot_geregistreerd_partner
                    )
                    else 0
                ),
                "maand": int(
                    partner.geboortedatum_echtgenoot_geregistreerd_partner[
                        settings.MONTH_START : settings.MONTH_END
                    ]
                    if is_valid_date_format(
                        partner.geboortedatum_echtgenoot_geregistreerd_partner
                    )
                    else 0
                ),
            },
            "land": {
                "code": "0000",
                "omschrijving": partner.geboorteland_echtgenoot_geregistreerd_partner,
            },
            "plaats": {
                "code": "0000",
                "omschrijving": partner.geboorteplaats_echtgenoot_geregistreerd_partner,
            },
            "inOnderzoek": {
                "datum": bool(partner.geboortedatum_echtgenoot_geregistreerd_partner),
                "land": bool(partner.geboorteland_echtgenoot_geregistreerd_partner),
                "plaats": bool(partner.geboorteplaats_echtgenoot_geregistreerd_partner),
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
                partner.burgerservicenummer_echtgenoot_geregistreerd_partner
            ),
            "geslachtsaanduiding": bool(
                partner.geslachtsaanduiding_echtgenoot_geregistreerd_partner
            ),
            "datumIngangOnderzoek": {
                "dag": int(
                    partner.datum_ingang_onderzoek[
                        settings.DAY_START : settings.DAY_END
                    ]
                    if is_valid_date_format(partner.datum_ingang_onderzoek)
                    else 0
                ),
                "datum": partner.datum_ingang_onderzoek,
                "jaar": int(
                    partner.datum_ingang_onderzoek[
                        settings.YEAR_START : settings.YEAR_END
                    ]
                    if is_valid_date_format(partner.datum_ingang_onderzoek)
                    else 0
                ),
                "maand": int(
                    partner.datum_ingang_onderzoek[
                        settings.MONTH_START : settings.MONTH_END
                    ]
                    if is_valid_date_format(partner.datum_ingang_onderzoek)
                    else 0
                ),
            },
        },
        "aangaanHuwelijkPartnerschap": {
            "datum": {
                "dag": int(
                    partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap[
                        settings.DAY_START : settings.DAY_END
                    ]
                    if is_valid_date_format(
                        partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap
                    )
                    else 0
                ),
                "datum": partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap,
                "jaar": int(
                    partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap[
                        settings.YEAR_START : settings.YEAR_END
                    ]
                    if is_valid_date_format(
                        partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap
                    )
                    else 0
                ),
                "maand": int(
                    partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap[
                        settings.MONTH_START : settings.MONTH_END
                    ]
                    if is_valid_date_format(
                        partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap
                    )
                    else 0
                ),
            },
            "land": {
                "code": "0000",
                "omschrijving": partner.land_huwelijkssluiting_aangaan_geregistreerd_partnerschap,
            },
            "plaats": {
                "code": "0000",
                "omschrijving": partner.plaats_huwelijkssluiting_aangaan_geregistreerd_partnerschap,
            },
            "inOnderzoek": {
                "datum": bool(
                    partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap
                ),
                "land": bool(
                    partner.land_huwelijkssluiting_aangaan_geregistreerd_partnerschap
                ),
                "plaats": bool(
                    partner.plaats_huwelijkssluiting_aangaan_geregistreerd_partnerschap
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

    return partner_dict
