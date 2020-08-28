ouder_retrieve_data = {
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
            "geslachtsnaam": "Maykin Ouder",
            "voorletters": "O",
            "voornamen": "Media Ouder",
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
        "datumIngangFamilierechtelijkeBetrekking": {
            "dag": 4,
            "datum": "19700604",
            "jaar": 1970,
            "maand": 6,
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
            "datumIngangFamilierechtelijkeBetrekking": True,
            "geslachtsaanduiding": True,
        },
    },
    "burgerservicenummer": "789123456",
    "geheimhoudingPersoonsgegevens": True,
    "geslachtsaanduiding": "man",
    "ouderAanduiding": "ouder1",
}
