from django.conf import settings

from openpersonen.api.utils import calculate_age, is_valid_date_format


def convert_kind_to_instance_dict(kind):

    kind_dict = {
        "burgerservicenummer": kind.burgerservicenummer_kind,
        "geheimhoudingPersoonsgegevens": True,
        "naam": {
            "geslachtsnaam": kind.geslachtsnaam_kind,
            "voorletters": "string",
            "voornamen": kind.voornamen_kind,
            "voorvoegsel": kind.voorvoegsel_geslachtsnaam_kind,
            "inOnderzoek": {
                "geslachtsnaam": bool(kind.geslachtsnaam_kind),
                "voornamen": bool(kind.voornamen_kind),
                "voorvoegsel": bool(kind.voorvoegsel_geslachtsnaam_kind),
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
                    kind.geboortedatum_kind[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                )
                if is_valid_date_format(kind.geboortedatum_kind)
                else 0,
                "datum": kind.geboortedatum_kind,
                "jaar": int(
                    kind.geboortedatum_kind[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                )
                if is_valid_date_format(kind.geboortedatum_kind)
                else 0,
                "maand": int(
                    kind.geboortedatum_kind[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                )
                if is_valid_date_format(kind.geboortedatum_kind)
                else 0,
            },
            "land": {
                "code": "string",
                "omschrijving": kind.geboorteland_kind,
            },
            "plaats": {
                "code": "string",
                "omschrijving": kind.geboorteplaats_kind,
            },
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
        "leeftijd": calculate_age(kind.geboortedatum_kind),
        "inOnderzoek": {
            "burgerservicenummer": bool(kind.burgerservicenummer_kind),
            "datumIngangOnderzoek": {
                "dag": int(
                    kind.datum_ingang_onderzoek[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                )
                if is_valid_date_format(kind.datum_ingang_onderzoek)
                else 0,
                "datum": kind.datum_ingang_onderzoek,
                "jaar": int(
                    kind.datum_ingang_onderzoek[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                )
                if is_valid_date_format(kind.datum_ingang_onderzoek)
                else 0,
                "maand": int(
                    kind.datum_ingang_onderzoek[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                )
                if is_valid_date_format(kind.datum_ingang_onderzoek)
                else 0,
            },
        },
    }

    return kind_dict
