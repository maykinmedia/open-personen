KIND_RETRIEVE_DATA = {
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
            "geslachtsnaam": "Maykin Kind",
            "voorletters": "K",
            "voornamen": "Media Kind",
            "voorvoegsel": "van",
        },
        "geboorte": {
            "_embedded": {
                "datum": {"dag": 15, "datum": "19990615", "jaar": 1999, "maand": 6},
                "land": {"code": "6030", "omschrijving": "Nederland"},
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
        },
    },
    "burgerservicenummer": "456789123",
    "geheimhoudingPersoonsgegevens": True,
    "leeftijd": 21,
}
