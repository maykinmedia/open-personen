test_data = [
    {
        "burgerservicenummer": "555555021",
        "geheimhoudingPersoonsgegevens": True,
        "geslachtsaanduiding": "man",
        "leeftijd": 34,
        "datumEersteInschrijvingGBA": {
            "dag": 3,
            "datum": "1989-05-03",
            "jaar": 1989,
            "maand": 5
        },
        "kiesrecht": {
            "europeesKiesrecht": "true",
            "uitgeslotenVanKiesrecht": "true",
            "einddatumUitsluitingEuropeesKiesrecht": {
                "dag": 3,
                "datum": "1989-05-03",
                "jaar": 1989,
                "maand": 5
            },
            "einddatumUitsluitingKiesrecht": {
                "dag": 3,
                "datum": "1989-05-03",
                "jaar": 1989,
                "maand": 5
            }
        },
        "naam": {
            "geslachtsnaam": "Vries",
            "voorletters": "string",
            "voornamen": "Pieter Jan",
            "voorvoegsel": "de",
            "inOnderzoek": {
                "geslachtsnaam": True,
                "voornamen": True,
                "voorvoegsel": True,
                "datumIngangOnderzoek": {
                    "dag": 3,
                    "datum": "1989-05-03",
                    "jaar": 1989,
                    "maand": 5
                }
            },
            "aanhef": "Geachte heer In het Veld ",
            "aanschrijfwijze": "H. in het Veld",
            "gebruikInLopendeTekst": "de heer In het Veld",
            "aanduidingNaamgebruik": "eigen"
        },
        "inOnderzoek": {
            "burgerservicenummer": True,
            "geslachtsaanduiding": True,
            "datumIngangOnderzoek": {
                "dag": 3,
                "datum": "1989-05-03",
                "jaar": 1989,
                "maand": 5
            }
        },
        "nationaliteit": [
            {
                "aanduidingBijzonderNederlanderschap": "behandeld_als_nederlander",
                "datumIngangGeldigheid": {
                    "dag": 3,
                    "datum": "1989-05-03",
                    "jaar": 1989,
                    "maand": 5
                },
                "nationaliteit": {
                    "code": "6030",
                    "omschrijving": "Nederland"
                },
                "redenOpname": {
                    "code": "6030",
                    "omschrijving": "Nederland"
                },
                "inOnderzoek": {
                    "aanduidingBijzonderNederlanderschap": True,
                    "nationaliteit": True,
                    "redenOpname": True,
                    "datumIngangOnderzoek": {
                        "dag": 3,
                        "datum": "1989-05-03",
                        "jaar": 1989,
                        "maand": 5
                    }
                }
            }
        ],
        "geboorte": {
            "datum": {
                "dag": 3,
                "datum": "1989-05-03",
                "jaar": 1989,
                "maand": 5
            },
            "land": {
                "code": "6030",
                "omschrijving": "Nederland"
            },
            "plaats": {
                "code": "6030",
                "omschrijving": "Nederland"
            },
            "inOnderzoek": {
                "datum": True,
                "land": True,
                "plaats": True,
                "datumIngangOnderzoek": {
                    "dag": 3,
                    "datum": "1989-05-03",
                    "jaar": 1989,
                    "maand": 5
                }
            }
        },
        "opschortingBijhouding": {
            "reden": "overlijden",
            "datum": {
                "dag": 3,
                "datum": "1989-05-03",
                "jaar": 1989,
                "maand": 5
            }
        },
        "overlijden": {
            "indicatieOverleden": True,
            "datum": {
                "dag": 3,
                "datum": "1989-05-03",
                "jaar": 1989,
                "maand": 5
            },
            "land": {
                "code": "6030",
                "omschrijving": "Nederland"
            },
            "plaats": {
                "code": "6030",
                "omschrijving": "Nederland"
            },
            "inOnderzoek": {
                "datum": True,
                "land": True,
                "plaats": True,
                "datumIngangOnderzoek": {
                    "dag": 3,
                    "datum": "1989-05-03",
                    "jaar": 1989,
                    "maand": 5
                }
            }
        },
        "verblijfplaats": {
            "functieAdres": "woonadres",
            "huisletter": "B",
            "huisnummer": 23,
            "huisnummertoevoeging": "IV",
            "aanduidingBijHuisnummer": "tegenover",
            "identificatiecodeNummeraanduiding": "0518200000366054",
            "naamOpenbareRuimte": "Loosduinsekade",
            "postcode": "2571CC",
            "woonplaatsnaam": "Utrecht",
            "identificatiecodeAdresseerbaarObject": "0518200000366054",
            "indicatieVestigingVanuitBuitenland": True,
            "locatiebeschrijving": "Naast de derde brug",
            "straatnaam": "string",
            "vanuitVertrokkenOnbekendWaarheen": "false",
            "datumAanvangAdreshouding": {
                "dag": 3,
                "datum": "1989-05-03",
                "jaar": 1989,
                "maand": 5
            },
            "datumIngangGeldigheid": {
                "dag": 3,
                "datum": "1989-05-03",
                "jaar": 1989,
                "maand": 5
            },
            "datumInschrijvingInGemeente": {
                "dag": 3,
                "datum": "1989-05-03",
                "jaar": 1989,
                "maand": 5
            },
            "datumVestigingInNederland": {
                "dag": 3,
                "datum": "1989-05-03",
                "jaar": 1989,
                "maand": 5
            },
            "gemeenteVanInschrijving": {
                "code": "6030",
                "omschrijving": "Nederland"
            },
            "landVanwaarIngeschreven": {
                "code": "6030",
                "omschrijving": "Nederland"
            },
            "verblijfBuitenland": {
                "adresRegel1": "string",
                "adresRegel2": "string",
                "adresRegel3": "string",
                "vertrokkenOnbekendWaarheen": True,
                "land": {
                    "code": "6030",
                    "omschrijving": "Nederland"
                }
            },
            "inOnderzoek": {
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
                "datumIngangOnderzoek": {
                    "dag": 3,
                    "datum": "1989-05-03",
                    "jaar": 1989,
                    "maand": 5
                }
            }
        },
        "gezagsverhouding": {
            "indicatieCurateleRegister": "true",
            "indicatieGezagMinderjarige": "ouder1",
            "inOnderzoek": {
                "indicatieCurateleRegister": True,
                "indicatieGezagMinderjarige": True,
                "datumIngangOnderzoek": {
                    "dag": 3,
                    "datum": "1989-05-03",
                    "jaar": 1989,
                    "maand": 5
                }
            }
        },
        "verblijfstitel": {
            "aanduiding": {
                "code": "6030",
                "omschrijving": "Nederland"
            },
            "datumEinde": {
                "dag": 3,
                "datum": "1989-05-03",
                "jaar": 1989,
                "maand": 5
            },
            "datumIngang": {
                "dag": 3,
                "datum": "1989-05-03",
                "jaar": 1989,
                "maand": 5
            },
            "inOnderzoek": {
                "aanduiding": True,
                "datumEinde": True,
                "datumIngang": True,
                "datumIngangOnderzoek": {
                    "dag": 3,
                    "datum": "1989-05-03",
                    "jaar": 1989,
                    "maand": 5
                }
            }
        },
        "reisdocumenten": [
            "546376728"
        ],
    }
]
