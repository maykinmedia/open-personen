kind_retrieve_data = {
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
            "geslachtsnaam": "Maykin Kind",
            "voorletters": "K",
            "voornamen": "Media Kind",
            "voorvoegsel": "van",
        },
        "geboorte": {
            "_embedded": {
                "datum": {"dag": 15, "datum": "19990615", "jaar": 1999, "maand": 6},
                "land": {"code": "string", "omschrijving": "Nederland"},
                "plaats": {"code": "string", "omschrijving": "Amsterdam"},
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
        },
    },
    "burgerservicenummer": "456789123",
    "geheimhoudingPersoonsgegevens": True,
    "leeftijd": 21,
}
