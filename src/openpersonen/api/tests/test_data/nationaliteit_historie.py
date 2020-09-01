nationaliteit_historie_data = {
    "_embedded": {
        "nationaliteithistorie": [
            {
                "_embedded": {
                    "datumIngangGeldigheid": {
                        "dag": 25,
                        "datum": "20160525",
                        "jaar": 2016,
                        "maand": 5,
                    },
                    "nationaliteit": {"code": "0000", "omschrijving": "Nederland"},
                    "redenOpname": {"code": "0000", "omschrijving": "Nederland"},
                    "inOnderzoek": {
                        "_embedded": {
                            "datumIngangOnderzoek": {
                                "dag": 0,
                                "datum": "string",
                                "jaar": 0,
                                "maand": 0,
                            }
                        },
                        "aanduidingBijzonderNederlanderschap": True,
                        "nationaliteit": True,
                        "redenOpname": True,
                    },
                    "datumEindeGeldigheid": {
                        "dag": 26,
                        "datum": "20170626",
                        "jaar": 2017,
                        "maand": 6,
                    },
                    "redenBeeindigen": {"code": "0000", "omschrijving": "Nederland"},
                },
                "aanduidingBijzonderNederlanderschap": "nederlander_behandeld",
                "geheimhoudingPersoonsgegevens": True,
                "indicatieNationaliteitBeeindigd": True,
            }
        ]
    },
    "url": "http://testserver/openpersonen/api/ingeschrevenpersonen/0/nationaliteithistorie",
}
