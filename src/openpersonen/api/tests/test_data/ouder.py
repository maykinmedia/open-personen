OUDER_RETRIEVE_DATA = {
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
            "geslachtsnaam": "string",
            "voorletters": "string",
            "voornamen": "string",
            "voorvoegsel": "string",
        },
        "geboorte": {
            "_embedded": {
                "datum": {"dag": 7, "datum": "19690507", "jaar": 1969, "maand": 5},
                "land": {"code": "6030", "omschrijving": "Nederland"},
                "plaats": {"code": "624", "omschrijving": "Amsterdam"},
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
        "datumIngangFamilierechtelijkeBetrekking": {
            "dag": 4,
            "datum": "19700604",
            "jaar": 1970,
            "maand": 6,
        },
        "inOnderzoek": {
            "_embedded": {
                "datumIngangOnderzoek": {
                    "dag": 1,
                    "datum": "01-01-1990",
                    "jaar": 1900,
                    "maand": 1,
                }
            },
            "burgerservicenummer": False,
            "datumIngangFamilierechtelijkeBetrekking": True,
            "geslachtsaanduiding": False,
        },
    },
    "burgerservicenummer": "789123456",
    "geheimhoudingPersoonsgegevens": False,
    "geslachtsaanduiding": "man",
    "ouderAanduiding": "ouder1",
}
