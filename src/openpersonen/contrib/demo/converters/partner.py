from django.conf import settings

from openpersonen.features.country_code_and_omschrijving.models import (
    CountryCodeAndOmschrijving,
)
from openpersonen.features.gemeente_code_and_omschrijving.models import (
    GemeenteCodeAndOmschrijving,
)
from openpersonen.utils.helpers import is_valid_date_format


def convert_partner_instance_to_dict(partner):

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
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                    if is_valid_date_format(
                        partner.geboortedatum_echtgenoot_geregistreerd_partner
                    )
                    else 0
                ),
                "datum": partner.geboortedatum_echtgenoot_geregistreerd_partner,
                "jaar": int(
                    partner.geboortedatum_echtgenoot_geregistreerd_partner[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                    if is_valid_date_format(
                        partner.geboortedatum_echtgenoot_geregistreerd_partner
                    )
                    else 0
                ),
                "maand": int(
                    partner.geboortedatum_echtgenoot_geregistreerd_partner[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                    if is_valid_date_format(
                        partner.geboortedatum_echtgenoot_geregistreerd_partner
                    )
                    else 0
                ),
            },
            "land": {
                "code": partner.geboorteland_echtgenoot_geregistreerd_partner,
                "omschrijving": CountryCodeAndOmschrijving.get_omschrijving_from_code(
                    partner.geboorteland_echtgenoot_geregistreerd_partner
                ),
            },
            "plaats": {
                "code": partner.geboorteplaats_echtgenoot_geregistreerd_partner,
                "omschrijving": GemeenteCodeAndOmschrijving.get_omschrijving_from_code(
                    partner.geboorteplaats_echtgenoot_geregistreerd_partner
                ),
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
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                    if is_valid_date_format(partner.datum_ingang_onderzoek)
                    else 0
                ),
                "datum": partner.datum_ingang_onderzoek,
                "jaar": int(
                    partner.datum_ingang_onderzoek[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                    if is_valid_date_format(partner.datum_ingang_onderzoek)
                    else 0
                ),
                "maand": int(
                    partner.datum_ingang_onderzoek[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
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
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                    if is_valid_date_format(
                        partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap
                    )
                    else 0
                ),
                "datum": partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap,
                "jaar": int(
                    partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                    if is_valid_date_format(
                        partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap
                    )
                    else 0
                ),
                "maand": int(
                    partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                    if is_valid_date_format(
                        partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap
                    )
                    else 0
                ),
            },
            "land": {
                "code": partner.land_huwelijkssluiting_aangaan_geregistreerd_partnerschap,
                "omschrijving": CountryCodeAndOmschrijving.get_omschrijving_from_code(
                    partner.land_huwelijkssluiting_aangaan_geregistreerd_partnerschap
                ),
            },
            "plaats": {
                "code": partner.plaats_huwelijkssluiting_aangaan_geregistreerd_partnerschap,
                "omschrijving": GemeenteCodeAndOmschrijving.get_omschrijving_from_code(
                    partner.plaats_huwelijkssluiting_aangaan_geregistreerd_partnerschap
                ),
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
