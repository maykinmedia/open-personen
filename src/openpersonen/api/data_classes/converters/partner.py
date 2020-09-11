from django.conf import settings

import xmltodict

from openpersonen.api.utils import convert_empty_instances


def get_client_instance_dict(response):
    dict_object = xmltodict.parse(response.content)

    antwoord_dict_object = dict_object["soapenv:Envelope"]["soapenv:Body"][
        "ns:npsLa01"
    ]["ns:antwoord"]["ns:object"]["ns:inp.heeftAlsEchtgenootPartner"]["ns:gerelateerde"]

    partner_dict = {
        "burgerservicenummer": antwoord_dict_object["ns:inp.bsn"],
        "geslachtsaanduiding": antwoord_dict_object["ns:geslachtsaanduiding"],
        "soortVerbintenis": antwoord_dict_object["ns:soortVerbintenis"],
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
                "code": "0000",
                "omschrijving": antwoord_dict_object["ns:inp.geboorteLand"],
            },
            "plaats": {
                "code": "0000",
                "omschrijving": antwoord_dict_object["ns:inp.geboorteplaats"],
            },
            "inOnderzoek": {
                "datum": bool(antwoord_dict_object["ns:geboortedatum"]),
                "land": bool(antwoord_dict_object["ns:inp.geboorteLand"]),
                "plaats": bool(antwoord_dict_object["ns:inp.geboorteplaats"]),
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0,
                },
            },
        },
        "inOnderzoek": {
            "burgerservicenummer": bool(antwoord_dict_object["ns:inp.bsn"]),
            "geslachtsaanduiding": bool(antwoord_dict_object["ns:geslachtsaanduiding"]),
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


def get_model_instance_dict(partner):

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
                    if partner.geboortedatum_echtgenoot_geregistreerd_partner
                    else 0
                ),
                "datum": partner.geboortedatum_echtgenoot_geregistreerd_partner,
                "jaar": int(
                    partner.geboortedatum_echtgenoot_geregistreerd_partner[
                        settings.YEAR_START : settings.YEAR_END
                    ]
                    if partner.geboortedatum_echtgenoot_geregistreerd_partner
                    else 0
                ),
                "maand": int(
                    partner.geboortedatum_echtgenoot_geregistreerd_partner[
                        settings.MONTH_START : settings.MONTH_END
                    ]
                    if partner.geboortedatum_echtgenoot_geregistreerd_partner
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
                    if partner.datum_ingang_onderzoek
                    else 0
                ),
                "datum": partner.datum_ingang_onderzoek,
                "jaar": int(
                    partner.datum_ingang_onderzoek[
                        settings.YEAR_START : settings.YEAR_END
                    ]
                    if partner.datum_ingang_onderzoek
                    else 0
                ),
                "maand": int(
                    partner.datum_ingang_onderzoek[
                        settings.MONTH_START : settings.MONTH_END
                    ]
                    if partner.datum_ingang_onderzoek
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
                    if partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap
                    else 0
                ),
                "datum": partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap,
                "jaar": int(
                    partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap[
                        settings.YEAR_START : settings.YEAR_END
                    ]
                    if partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap
                    else 0
                ),
                "maand": int(
                    partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap[
                        settings.MONTH_START : settings.MONTH_END
                    ]
                    if partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap
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
