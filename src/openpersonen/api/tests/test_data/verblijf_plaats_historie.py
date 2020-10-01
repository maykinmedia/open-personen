VERBLIJF_PLAATS_HISTORIE_DATA = {
    "_embedded": {
        "verblijfplaatshistorie": [
            {
                "_embedded": {
                    "datumAanvangAdreshouding": {
                        "dag": 0,
                        "datum": "string",
                        "jaar": 0,
                        "maand": 0,
                    },
                    "datumIngangGeldigheid": {
                        "dag": 0,
                        "datum": "string",
                        "jaar": 0,
                        "maand": 0,
                    },
                    "datumInschrijvingInGemeente": {
                        "dag": 0,
                        "datum": "string",
                        "jaar": 0,
                        "maand": 0,
                    },
                    "datumVestigingInNederland": {
                        "dag": 0,
                        "datum": "string",
                        "jaar": 0,
                        "maand": 0,
                    },
                    "gemeenteVanInschrijving": {
                        "code": "0000",
                        "omschrijving": "Nederland",
                    },
                    "landVanwaarIngeschreven": {
                        "code": "0000",
                        "omschrijving": "Nederland",
                    },
                    "verblijfBuitenland": {
                        "_embedded": {
                            "land": {"code": "0000", "omschrijving": "Nederland"}
                        },
                        "adresRegel1": "string",
                        "adresRegel2": "string",
                        "adresRegel3": "string",
                        "vertrokkenOnbekendWaarheen": True,
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
                        "aanduidingBijHuisnummer": True,
                        "datumAanvangAdreshouding": True,
                        "datumIngangGeldigheid": True,
                        "datumInschrijvingInGemeente": True,
                        "datumVestigingInNederland": True,
                        "functieAdres": True,
                        "gemeenteVanInschrijving": True,
                        "huisletter": True,
                        "huisnummer": True,
                        "huisnummertoevoeging": True,
                        "identificatiecodeNummeraanduiding": True,
                        "identificatiecodeAdresseerbaarObject": True,
                        "landVanwaarIngeschreven": True,
                        "locatiebeschrijving": True,
                        "naamOpenbareRuimte": True,
                        "postcode": True,
                        "straatnaam": True,
                        "verblijfBuitenland": True,
                        "woonplaatsnaam": True,
                    },
                    "datumTot": {
                        "dag": 0,
                        "datum": "string",
                        "jaar": 0,
                        "maand": 0,
                    },
                },
                "functieAdres": "woonadres",
                "huisletter": "B",
                "huisnummer": "117",
                "huisnummertoevoeging": "IV",
                "aanduidingBijHuisnummer": "tegenover",
                "identificatiecodeNummeraanduiding": "0518200000366054",
                "naamOpenbareRuimte": "Jordaan",
                "postcode": "1015CJ",
                "woonplaatsnaam": "Amsterdam",
                "identificatiecodeAdresseerbaarObject": "0518200000366054",
                "indicatieVestigingVanuitBuitenland": True,
                "locatiebeschrijving": "Naast de derde brug",
                "straatnaam": "string",
                "vanuitVertrokkenOnbekendWaarheen": True,
                "geheimhoudingPersoonsgegevens": True,
            }
        ]
    },
    "url": "http://testserver/ingeschrevenpersonen/123456789/verblijfplaatshistorie",
}
