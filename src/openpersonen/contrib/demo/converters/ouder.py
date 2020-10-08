from django.conf import settings

from openpersonen.contrib.utils import is_valid_date_format


def convert_ouder_instance_to_dict(ouder):
    ouder_dict = {
        "burgerservicenummer": ouder.burgerservicenummer_ouder,
        "geslachtsaanduiding": ouder.geslachtsaanduiding_ouder,
        "ouderAanduiding": ouder.geslachtsaanduiding_ouder,
        "datumIngangFamilierechtelijkeBetrekking": {
            "dag": int(
                ouder.datum_ingang_familierechtelijke_betrekking_ouder[
                    settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                ]
                if is_valid_date_format(
                    ouder.datum_ingang_familierechtelijke_betrekking_ouder
                )
                else 0
            ),
            "datum": ouder.datum_ingang_familierechtelijke_betrekking_ouder,
            "jaar": int(
                ouder.datum_ingang_familierechtelijke_betrekking_ouder[
                    settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                ]
                if is_valid_date_format(
                    ouder.datum_ingang_familierechtelijke_betrekking_ouder
                )
                else 0
            ),
            "maand": int(
                ouder.datum_ingang_familierechtelijke_betrekking_ouder[
                    settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
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
                    ouder.datum_ingang_onderzoek[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                    if is_valid_date_format(ouder.datum_ingang_onderzoek)
                    else 0
                ),
                "datum": ouder.datum_ingang_onderzoek,
                "jaar": int(
                    ouder.datum_ingang_onderzoek[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                    if is_valid_date_format(ouder.datum_ingang_onderzoek)
                    else 0
                ),
                "maand": int(
                    ouder.datum_ingang_onderzoek[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                    if is_valid_date_format(ouder.datum_ingang_onderzoek)
                    else 0
                ),
            },
        },
        "geboorte": {
            "datum": {
                "dag": int(
                    ouder.geboortedatum_ouder[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                )
                if is_valid_date_format(ouder.geboortedatum_ouder)
                else 0,
                "datum": ouder.geboortedatum_ouder,
                "jaar": int(
                    ouder.geboortedatum_ouder[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                )
                if is_valid_date_format(ouder.geboortedatum_ouder)
                else 0,
                "maand": int(
                    ouder.geboortedatum_ouder[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
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
