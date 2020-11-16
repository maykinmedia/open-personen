PARTNER_RETRIEVE_DATA = {
    "_embedded": {
        "naam": {
            "_embedded": {
                "inOnderzoek": {
                    "_embedded": {
                        "datumIngangOnderzoek": {
                            "dag": 1,
                            "datum": "01-01-1900",
                            "jaar": 1900,
                            "maand": 1,
                        }
                    },
                    "geslachtsnaam": False,
                    "voornamen": False,
                    "voorvoegsel": False,
                }
            },
            "geslachtsnaam": None,
            "voorletters": None,
            "voornamen": None,
            "voorvoegsel": None,
        },
        "geboorte": {
            "_embedded": {
                "datum": {"dag": 7, "datum": "19690507", "jaar": 1969, "maand": 5},
                "land": {"code": "Nederland", "omschrijving": "Nederland"},
                "plaats": {"code": "Amsterdam", "omschrijving": "Amsterdam"},
                "inOnderzoek": {
                    "_embedded": {
                        "datumIngangOnderzoek": {
                            "dag": 1,
                            "datum": "01-01-1900",
                            "jaar": 1900,
                            "maand": 1,
                        }
                    },
                    "datum": False,
                    "land": False,
                    "plaats": False,
                },
            }
        },
        "inOnderzoek": {
            "_embedded": {
                "datumIngangOnderzoek": {
                    "dag": 1,
                    "datum": "01-01-1900",
                    "jaar": 1900,
                    "maand": 1,
                }
            },
            "burgerservicenummer": False,
            "geslachtsaanduiding": False,
        },
        "aangaanHuwelijkPartnerschap": {
            "_embedded": {
                "datum": {"dag": 1, "datum": "19000101", "jaar": 1900, "maand": 1},
                "land": {"code": "string", "omschrijving": "string"},
                "plaats": {"code": "string", "omschrijving": "string"},
                "inOnderzoek": {
                    "_embedded": {
                        "datumIngangOnderzoek": {
                            "dag": 1,
                            "datum": "01-01-1900",
                            "jaar": 1900,
                            "maand": 1,
                        }
                    },
                    "datum": False,
                    "land": False,
                    "plaats": False,
                },
            }
        },
    },
    "burgerservicenummer": "987654321",
    "geheimhoudingPersoonsgegevens": False,
    "geslachtsaanduiding": "man",
    "soortVerbintenis": "string",
}
