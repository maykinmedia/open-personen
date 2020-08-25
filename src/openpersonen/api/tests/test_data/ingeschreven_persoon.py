ingeschreven_persoon_retrieve_data = {
    "_embedded": {
        "naam": {
            "_embedded": {
                "inOnderzoek": {
                    "_embedded": {
                        "datumIngangOnderzoek": {
                            "dag": 0,
                            "datum": "string",
                            "jaar": 0,
                            "maand": 0
                        }
                    },
                    "geslachtsnaam": True,
                    "voornamen": True,
                    "voorvoegsel": True
                }
            },
            "geslachtsnaam": "Maykin",
            "voorletters": "M.",
            "voornamen": "Media",
            "voorvoegsel": "van",
            "aanhef": "Media",
            "aanschrijfwijze": "string",
            "gebruikInLopendeTekst": "string",
            "aanduidingNaamgebruik": "E"
        },
        "geboorte": {
            "_embedded": {
                "datum": {
                    "dag": 15,
                    "datum": "19800915",
                    "jaar": 1980,
                    "maand": 9
                },
                "land": {
                    "code": "string",
                    "omschrijving": "Nederland"
                },
                "plaats": {
                    "code": "string",
                    "omschrijving": "Amsterdam"
                },
                "inOnderzoek": {
                    "_embedded": {
                        "datumIngangOnderzoek": {
                            "dag": 0,
                            "datum": "string",
                            "jaar": 0,
                            "maand": 0
                        }
                    },
                    "datum": True,
                    "land": True,
                    "plaats": True
                }
            }
        },
        "datumEersteInschrijvingGBA": {
            "dag": 16,
            "datum": "20051216",
            "jaar": 2005,
            "maand": 12
        },
        "kiesrecht": {
            "_embedded": {
                "einddatumUitsluitingEuropeesKiesrecht": {
                    "dag": 24,
                    "datum": "20200924",
                    "jaar": 2020,
                    "maand": 9
                },
                "einddatumUitsluitingKiesrecht": {
                    "dag": 24,
                    "datum": "20200924",
                    "jaar": 2020,
                    "maand": 9
                }
            },
            "europeesKiesrecht": True,
            "uitgeslotenVanKiesrecht": True
        },
        "inOnderzoek": {
            "_embedded": {
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0
                }
            },
            "burgerservicenummer": True,
            "geslachtsaanduiding": True
        },
        "nationaliteit": [
            {
                "_embedded": {
                    "datumIngangGeldigheid": {
                        "dag": 0,
                        "datum": "string",
                        "jaar": 0,
                        "maand": 0
                    },
                    "nationaliteit": {
                        "code": "string",
                        "omschrijving": "string"
                    },
                    "redenOpname": {
                        "code": "string",
                        "omschrijving": "string"
                    },
                    "inOnderzoek": {
                        "_embedded": {
                            "datumIngangOnderzoek": {
                                "dag": 0,
                                "datum": "string",
                                "jaar": 0,
                                "maand": 0
                            }
                        },
                        "aanduidingBijzonderNederlanderschap": True,
                        "nationaliteit": True,
                        "redenOpname": True
                    }
                },
                "aanduidingBijzonderNederlanderschap": "behandeld_als_nederlander"
            }
        ],
        "opschortingBijhouding": {
            "_embedded": {
                "datum": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0
                }
            },
            "reden": "overlijden"
        },
        "overlijden": {
            "_embedded": {
                "datum": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0
                },
                "land": {
                    "code": "string",
                    "omschrijving": None
                },
                "plaats": {
                    "code": "string",
                    "omschrijving": None
                },
                "inOnderzoek": {
                    "_embedded": {
                        "datumIngangOnderzoek": {
                            "dag": 0,
                            "datum": "string",
                            "jaar": 0,
                            "maand": 0
                        }
                    },
                    "datum": True,
                    "land": True,
                    "plaats": True
                }
            },
            "indicatieOverleden": True
        },
        "verblijfplaats": {
            "_embedded": {
                "datumAanvangAdreshouding": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0
                },
                "datumIngangGeldigheid": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0
                },
                "datumInschrijvingInGemeente": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0
                },
                "datumVestigingInNederland": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0
                },
                "gemeenteVanInschrijving": {
                    "code": "string",
                    "omschrijving": "string"
                },
                "landVanwaarIngeschreven": {
                    "code": "string",
                    "omschrijving": "string"
                },
                "verblijfBuitenland": {
                    "_embedded": {
                        "land": {
                            "code": "string",
                            "omschrijving": "string"
                        }
                    },
                    "adresRegel1": "string",
                    "adresRegel2": "string",
                    "adresRegel3": "string",
                    "vertrokkenOnbekendWaarheen": True
                },
                "inOnderzoek": {
                    "_embedded": {
                        "datumIngangOnderzoek": {
                            "dag": 0,
                            "datum": "string",
                            "jaar": 0,
                            "maand": 0
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
                    "woonplaatsnaam": True
                }
            },
            "functieAdres": "woonadres",
            "huisletter": "A",
            "huisnummer": 117,
            "huisnummertoevoeging": "B",
            "aanduidingBijHuisnummer": "tegenover",
            "identificatiecodeNummeraanduiding": "string",
            "naamOpenbareRuimte": "string",
            "postcode": "2525AB",
            "woonplaatsnaam": "Amsterdam",
            "identificatiecodeAdresseerbaarObject": "string",
            "indicatieVestigingVanuitBuitenland": True,
            "locatiebeschrijving": "string",
            "straatnaam": "Straat",
            "vanuitVertrokkenOnbekendWaarheen": True
        },
        "gezagsverhouding": {
            "_embedded": {
                "inOnderzoek": {
                    "_embedded": {
                        "datumIngangOnderzoek": {
                            "dag": 0,
                            "datum": "string",
                            "jaar": 0,
                            "maand": 0
                        }
                    },
                    "indicatieCurateleRegister": True,
                    "indicatieGezagMinderjarige": True
                }
            },
            "indicatieCurateleRegister": True,
            "indicatieGezagMinderjarige": "ouder1"
        },
        "verblijfstitel": {
            "_embedded": {
                "aanduiding": {
                    "code": "string",
                    "omschrijving": "string"
                },
                "datumEinde": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0
                },
                "datumIngang": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0
                },
                "inOnderzoek": {
                    "_embedded": {
                        "datumIngangOnderzoek": {
                            "dag": 0,
                            "datum": "string",
                            "jaar": 0,
                            "maand": 0
                        }
                    },
                    "aanduiding": True,
                    "datumEinde": True,
                    "datumIngang": True
                }
            }
        },
        "reisdocumenten": [
            "string"
        ]
    },
    "burgerservicenummer": "123456789",
    "geheimhoudingPersoonsgegevens": True,
    "geslachtsaanduiding": "M",
    "leeftijd": 39
}
