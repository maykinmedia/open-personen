PARTNER_RETRIEVE_DATA = {
    "_embedded": {
        "naam": {
            "_embedded": {
                "inOnderzoek": {
                    "_embedded": {
                        "datumIngangOnderzoek": {
                            "dag": 0,
                            "datum": "string",
                            "jaar": 0,
                            "maand": 0,
                        }
                    },
                    "geslachtsnaam": True,
                    "voornamen": True,
                    "voorvoegsel": True,
                }
            },
            "geslachtsnaam": "Maykin Partner",
            "voorletters": "P",
            "voornamen": "Media Partner",
            "voorvoegsel": "de",
        },
        "geboorte": {
            "_embedded": {
                "datum": {"dag": 7, "datum": "19690507", "jaar": 1969, "maand": 5},
                "land": {"code": "0000", "omschrijving": "Nederland"},
                "plaats": {"code": "0000", "omschrijving": "Amsterdam"},
                "inOnderzoek": {
                    "_embedded": {
                        "datumIngangOnderzoek": {
                            "dag": 0,
                            "datum": "string",
                            "jaar": 0,
                            "maand": 0,
                        }
                    },
                    "datum": True,
                    "land": True,
                    "plaats": True,
                },
            }
        },
        "inOnderzoek": {
            "_embedded": {
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0,
                }
            },
            "burgerservicenummer": True,
            "geslachtsaanduiding": True,
        },
        "aangaanHuwelijkPartnerschap": {
            "_embedded": {
                "datum": {"dag": 0, "datum": "string", "jaar": 0, "maand": 0},
                "land": {"code": "0000", "omschrijving": "string"},
                "plaats": {"code": "0000", "omschrijving": "string"},
                "inOnderzoek": {
                    "_embedded": {
                        "datumIngangOnderzoek": {
                            "dag": 0,
                            "datum": "string",
                            "jaar": 0,
                            "maand": 0,
                        }
                    },
                    "datum": True,
                    "land": True,
                    "plaats": True,
                },
            }
        },
    },
    "burgerservicenummer": "987654321",
    "geheimhoudingPersoonsgegevens": True,
    "geslachtsaanduiding": "man",
    "soortVerbintenis": "huwelijk",
}
