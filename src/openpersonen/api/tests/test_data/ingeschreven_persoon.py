INGESCHREVEN_PERSOON_RETRIEVE_DATA = {
    "_links": {
        "self": {"href": "http://testserver/api/ingeschrevenpersonen/123456789"},
        "kinderen": [
            {
                "_links": {
                    "self": {
                        "href": "http://testserver/api/ingeschrevenpersonen/123456789/kinderen/string"
                    }
                }
            }
        ],
        "ouders": [
            {
                "_links": {
                    "self": {
                        "href": "http://testserver/api/ingeschrevenpersonen/123456789/ouders/string"
                    }
                }
            }
        ],
        "partners": [
            {
                "_links": {
                    "self": {
                        "href": "http://testserver/api/ingeschrevenpersonen/123456789/partners/string"
                    }
                }
            }
        ],
    },
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
            "geslachtsnaam": "Maykin",
            "voorletters": "M.",
            "voornamen": "Media",
            "voorvoegsel": "van",
            "aanhef": "Geachte heer Van Maykin",
            "aanschrijfwijze": "M. van Maykin",
            "gebruikInLopendeTekst": "de heer Van Maykin",
            "aanduidingNaamgebruik": "E",
        },
        "geboorte": {
            "_embedded": {
                "datum": {"dag": 15, "datum": "19800915", "jaar": 1980, "maand": 9},
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
        "datumEersteInschrijvingGBA": {
            "dag": 16,
            "datum": "20051216",
            "jaar": 2005,
            "maand": 12,
        },
        "kiesrecht": {
            "_embedded": {
                "einddatumUitsluitingEuropeesKiesrecht": {
                    "dag": 1,
                    "datum": "01-01-1900",
                    "jaar": 1900,
                    "maand": 1,
                },
                "einddatumUitsluitingKiesrecht": {
                    "dag": 1,
                    "datum": "01-01-1900",
                    "jaar": 1900,
                    "maand": 1,
                },
            },
            "europeesKiesrecht": False,
            "uitgeslotenVanKiesrecht": False,
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
            "geslachtsaanduiding": False,
        },
        "nationaliteit": [
            {
                "_embedded": {
                    "datumIngangGeldigheid": {
                        "dag": 1,
                        "datum": "19000101",
                        "jaar": 1900,
                        "maand": 1,
                    },
                    "nationaliteit": {"code": None, "omschrijving": None},
                    "redenOpname": {"code": ".", "omschrijving": "Onbekend"},
                    "inOnderzoek": {
                        "_embedded": {
                            "datumIngangOnderzoek": {
                                "dag": 1,
                                "datum": "01-01-1900",
                                "jaar": 1900,
                                "maand": 1,
                            }
                        },
                        "aanduidingBijzonderNederlanderschap": False,
                        "nationaliteit": False,
                        "redenOpname": True,
                    },
                },
                "aanduidingBijzonderNederlanderschap": "behandeld_als_nederlander",
            }
        ],
        "opschortingBijhouding": {
            "_embedded": {
                "datum": {"dag": 1, "datum": "19000101", "jaar": 1900, "maand": 1}
            },
            "reden": "string",
        },
        "overlijden": {
            "_embedded": {
                "datum": {"dag": 1, "datum": "19000101", "jaar": 1900, "maand": 1},
                "land": {"code": "string", "omschrijving": "Onbekend"},
                "plaats": {"code": "0", "omschrijving": "string"},
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
            },
            "indicatieOverleden": False,
        },
        "verblijfplaats": {
            "_embedded": {
                "datumAanvangAdreshouding": {
                    "dag": 1,
                    "datum": "19000101",
                    "jaar": 1900,
                    "maand": 1,
                },
                "datumIngangGeldigheid": {
                    "dag": 1,
                    "datum": "19000101",
                    "jaar": 1900,
                    "maand": 1,
                },
                "datumInschrijvingInGemeente": {
                    "dag": 1,
                    "datum": "01-01-1900",
                    "jaar": 1900,
                    "maand": 1,
                },
                "datumVestigingInNederland": {
                    "dag": 1,
                    "datum": "01-01-1900",
                    "jaar": 1900,
                    "maand": 1,
                },
                "gemeenteVanInschrijving": {"code": None, "omschrijving": None},
                "landVanwaarIngeschreven": {"code": "", "omschrijving": ""},
                "verblijfBuitenland": {
                    "_embedded": {"land": {"code": None, "omschrijving": "Onbekend"}},
                    "adresRegel1": None,
                    "adresRegel2": None,
                    "adresRegel3": None,
                    "vertrokkenOnbekendWaarheen": True,
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
                    "aanduidingBijHuisnummer": True,
                    "datumAanvangAdreshouding": True,
                    "datumIngangGeldigheid": True,
                    "datumInschrijvingInGemeente": True,
                    "datumVestigingInNederland": True,
                    "functieAdres": True,
                    "gemeenteVanInschrijving": True,
                    "huisletter": False,
                    "huisnummer": False,
                    "huisnummertoevoeging": False,
                    "identificatiecodeNummeraanduiding": False,
                    "identificatiecodeAdresseerbaarObject": False,
                    "landVanwaarIngeschreven": False,
                    "locatiebeschrijving": False,
                    "naamOpenbareRuimte": False,
                    "postcode": False,
                    "straatnaam": False,
                    "verblijfBuitenland": False,
                    "woonplaatsnaam": False,
                },
            },
            "functieAdres": "woonadres",
            "huisletter": "A",
            "huisnummer": "117",
            "huisnummertoevoeging": "B",
            "aanduidingBijHuisnummer": None,
            "identificatiecodeNummeraanduiding": "string",
            "naamOpenbareRuimte": "string",
            "postcode": "2525AB",
            "woonplaatsnaam": "Amsterdam",
            "identificatiecodeAdresseerbaarObject": "string",
            "indicatieVestigingVanuitBuitenland": True,
            "locatiebeschrijving": "string",
            "straatnaam": "Straat",
            "vanuitVertrokkenOnbekendWaarheen": True,
        },
        "gezagsverhouding": {
            "_embedded": {
                "inOnderzoek": {
                    "_embedded": {
                        "datumIngangOnderzoek": {
                            "dag": 0,
                            "datum": "False",
                            "jaar": 0,
                            "maand": 0,
                        }
                    },
                    "indicatieCurateleRegister": False,
                    "indicatieGezagMinderjarige": False,
                }
            },
            "indicatieCurateleRegister": False,
            "indicatieGezagMinderjarige": False,
        },
        "verblijfstitel": {
            "_embedded": {
                "aanduiding": {"code": None, "omschrijving": "string"},
                "datumEinde": {"dag": 1, "datum": "19000101", "jaar": 1900, "maand": 1},
                "datumIngang": {
                    "dag": 1,
                    "datum": "19000101",
                    "jaar": 1900,
                    "maand": 1,
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
                    "aanduiding": False,
                    "datumEinde": True,
                    "datumIngang": True,
                },
            }
        },
        "reisdocumenten": ["string"],
    },
    "burgerservicenummer": "123456789",
    "geheimhoudingPersoonsgegevens": True,
    "geslachtsaanduiding": "M",
    "leeftijd": 39,
}


UTRECHT_INGESCHREVEN_PERSOON_RETRIEVE_DATA = {
    "_links": {
        "self": {"href": "http://testserver/api/ingeschrevenpersonen/999994177"},
        "kinderen": [
            {
                "_links": {
                    "self": {
                        "href": "http://testserver/api/ingeschrevenpersonen/999994177/kinderen/string"
                    }
                }
            }
        ],
        "ouders": [
            {
                "_links": {
                    "self": {
                        "href": "http://testserver/api/ingeschrevenpersonen/999994177/ouders/string"
                    }
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "http://testserver/api/ingeschrevenpersonen/999994177/ouders/string"
                    }
                }
            },
        ],
        "partners": [
            {
                "_links": {
                    "self": {
                        "href": "http://testserver/api/ingeschrevenpersonen/999994177/partners/string"
                    }
                }
            }
        ],
    },
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
            "geslachtsnaam": "Kik",
            "voorletters": "P.",
            "voornamen": "Peter",
            "voorvoegsel": None,
            "aanhef": "Geachte heer Kik",
            "aanschrijfwijze": "P. Kik",
            "gebruikInLopendeTekst": "de heer Kik",
            "aanduidingNaamgebruik": "E",
        },
        "geboorte": {
            "_embedded": {
                "datum": {"dag": 1, "datum": "19700101", "jaar": 1970, "maand": 1},
                "land": {"code": "6030", "omschrijving": "Nederland"},
                "plaats": {"code": "0", "omschrijving": "string"},
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
        "datumEersteInschrijvingGBA": {
            "dag": 1,
            "datum": "string",
            "jaar": 1900,
            "maand": 1,
        },
        "kiesrecht": {
            "_embedded": {
                "einddatumUitsluitingEuropeesKiesrecht": {
                    "dag": 1,
                    "datum": "01-01-1900",
                    "jaar": 1900,
                    "maand": 1,
                },
                "einddatumUitsluitingKiesrecht": {
                    "dag": 1,
                    "datum": "01-01-1900",
                    "jaar": 1900,
                    "maand": 1,
                },
            },
            "europeesKiesrecht": False,
            "uitgeslotenVanKiesrecht": False,
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
            "geslachtsaanduiding": False,
        },
        "nationaliteit": [
            {
                "_embedded": {
                    "datumIngangGeldigheid": {
                        "dag": 1,
                        "datum": "19000101",
                        "jaar": 1900,
                        "maand": 1,
                    },
                    "nationaliteit": {"code": "0001", "omschrijving": None},
                    "redenOpname": {"code": ".", "omschrijving": "Onbekend"},
                    "inOnderzoek": {
                        "_embedded": {
                            "datumIngangOnderzoek": {
                                "dag": 1,
                                "datum": "01-01-1900",
                                "jaar": 1900,
                                "maand": 1,
                            }
                        },
                        "aanduidingBijzonderNederlanderschap": False,
                        "nationaliteit": False,
                        "redenOpname": True,
                    },
                },
                "aanduidingBijzonderNederlanderschap": "string",
            }
        ],
        "opschortingBijhouding": {
            "_embedded": {
                "datum": {"dag": 1, "datum": "19000101", "jaar": 1900, "maand": 1}
            },
            "reden": "string",
        },
        "overlijden": {
            "_embedded": {
                "datum": {"dag": 0, "datum": "19000101", "jaar": 1900, "maand": 1},
                "land": {"code": "string", "omschrijving": "Onbekend"},
                "plaats": {"code": "0", "omschrijving": "string"},
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
            },
            "indicatieOverleden": False,
        },
        "verblijfplaats": {
            "_embedded": {
                "datumAanvangAdreshouding": {
                    "dag": 1,
                    "datum": "20100101",
                    "jaar": 2010,
                    "maand": 1,
                },
                "datumIngangGeldigheid": {
                    "dag": 1,
                    "datum": "19000101",
                    "jaar": 1900,
                    "maand": 1,
                },
                "datumInschrijvingInGemeente": {
                    "dag": 1,
                    "datum": "01-01-1900",
                    "jaar": 1900,
                    "maand": 1,
                },
                "datumVestigingInNederland": {
                    "dag": 1,
                    "datum": "01-01-1900",
                    "jaar": 1900,
                    "maand": 1,
                },
                "gemeenteVanInschrijving": {"code": None, "omschrijving": None},
                "landVanwaarIngeschreven": {"code": "", "omschrijving": ""},
                "verblijfBuitenland": {
                    "_embedded": {"land": {"code": None, "omschrijving": "Onbekend"}},
                    "adresRegel1": None,
                    "adresRegel2": None,
                    "adresRegel3": None,
                    "vertrokkenOnbekendWaarheen": True,
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
                    "aanduidingBijHuisnummer": True,
                    "datumAanvangAdreshouding": True,
                    "datumIngangGeldigheid": True,
                    "datumInschrijvingInGemeente": True,
                    "datumVestigingInNederland": True,
                    "functieAdres": True,
                    "gemeenteVanInschrijving": True,
                    "huisletter": False,
                    "huisnummer": False,
                    "huisnummertoevoeging": False,
                    "identificatiecodeNummeraanduiding": False,
                    "identificatiecodeAdresseerbaarObject": False,
                    "landVanwaarIngeschreven": False,
                    "locatiebeschrijving": False,
                    "naamOpenbareRuimte": False,
                    "postcode": False,
                    "straatnaam": False,
                    "verblijfBuitenland": False,
                    "woonplaatsnaam": False,
                },
            },
            "functieAdres": "woonadres",
            "huisletter": None,
            "huisnummer": "1",
            "huisnummertoevoeging": None,
            "aanduidingBijHuisnummer": None,
            "identificatiecodeNummeraanduiding": "string",
            "naamOpenbareRuimte": "string",
            "postcode": "3500AA",
            "woonplaatsnaam": None,
            "identificatiecodeAdresseerbaarObject": "string",
            "indicatieVestigingVanuitBuitenland": True,
            "locatiebeschrijving": None,
            "straatnaam": "Veldweg",
            "vanuitVertrokkenOnbekendWaarheen": True,
        },
        "gezagsverhouding": {
            "_embedded": {
                "inOnderzoek": {
                    "_embedded": {
                        "datumIngangOnderzoek": {
                            "dag": 0,
                            "datum": "False",
                            "jaar": 0,
                            "maand": 0,
                        }
                    },
                    "indicatieCurateleRegister": False,
                    "indicatieGezagMinderjarige": False,
                }
            },
            "indicatieCurateleRegister": False,
            "indicatieGezagMinderjarige": False,
        },
        "verblijfstitel": {
            "_embedded": {
                "aanduiding": {"code": None, "omschrijving": "string"},
                "datumEinde": {"dag": 1, "datum": None, "jaar": 1900, "maand": 1},
                "datumIngang": {"dag": 1, "datum": None, "jaar": 1900, "maand": 1},
                "inOnderzoek": {
                    "_embedded": {
                        "datumIngangOnderzoek": {
                            "dag": 1,
                            "datum": "01-01-1900",
                            "jaar": 1900,
                            "maand": 1,
                        }
                    },
                    "aanduiding": False,
                    "datumEinde": True,
                    "datumIngang": True,
                },
            }
        },
        "reisdocumenten": ["string"],
    },
    "burgerservicenummer": "999994177",
    "geheimhoudingPersoonsgegevens": False,
    "geslachtsaanduiding": "M",
    "leeftijd": 50,
}
