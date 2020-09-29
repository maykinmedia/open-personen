VERBLIJFS_TITEL_HISTORIE = {
    "_embedded": {
        "verblijfstitelhistorie": [
            {
                "_embedded": {
                    "aanduiding": {"code": "0000", "omschrijving": "Nederland"},
                    "datumEinde": {
                        "dag": 15,
                        "datum": "20160615",
                        "jaar": 2016,
                        "maand": 6,
                    },
                    "datumIngang": {
                        "dag": 31,
                        "datum": "20160831",
                        "jaar": 2016,
                        "maand": 8,
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
                        "aanduiding": True,
                        "datumEinde": True,
                        "datumIngang": True,
                    },
                },
                "geheimhoudingPersoonsgegevens": True,
            }
        ]
    },
    "url": "http://testserver/ingeschrevenpersonen/123456789/verblijfstitelhistorie",
}
