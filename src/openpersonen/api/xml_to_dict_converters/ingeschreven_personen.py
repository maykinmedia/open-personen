import xmltodict


def get_ingeschreven_persoon_dict(response):

    dict_object = xmltodict.parse(response.content)

    antwoord_dict_object = dict_object['soapenv:Envelope']['soapenv:Body']['ns:npsLa01-prs-NatuurlijkPersoon']['ns:antwoord']['ns:object']

    ingeschreven_persoon_dict =  {
        "burgerservicenummer": antwoord_dict_object['ns:inp.bsn']['#text'],
        "geheimhoudingPersoonsgegevens": True,
        "naam": {
            "geslachtsnaam": antwoord_dict_object['ns:geslachtsnaam']['#text'],
            "voorletters": antwoord_dict_object['ns:voorletters']['#text'],
            "voornamen": antwoord_dict_object['ns:voornamen']['#text'],
            "voorvoegsel": antwoord_dict_object['ns:voorvoegselGeslachtsnaam']['#text'],
            "inOnderzoek": {
                "geslachtsnaam": bool(antwoord_dict_object['ns:geslachtsnaam']['#text']),
                "voornamen": bool(antwoord_dict_object['ns:voornamen']['#text']),
                "voorvoegsel": bool(antwoord_dict_object['ns:voorvoegselGeslachtsnaam']['#text']),
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0
                }
            },
            "aanhef": antwoord_dict_object['ns:aanhefAanschrijving']['#text'],
            "aanschrijfwijze": "string",
            "gebruikInLopendeTekst": "string",
            "aanduidingNaamgebruik": antwoord_dict_object['ns:aanduidingNaamgebruik']['#text']
        },
        "geboorte": {
            "datum": {
                "dag": 0,
                "datum": "string",
                "jaar": 0,
                "maand": 0
            },
            "land": {
                "code": "string",
                "omschrijving": "string"
            },
            "plaats": {
                "code": "string",
                "omschrijving": "string"
            },
            "inOnderzoek": {
                "datum": True,
                "land": True,
                "plaats": True,
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0
                }
            }
        },
        "geslachtsaanduiding": antwoord_dict_object['ns:geslachtsaanduiding']['#text'],
        "leeftijd": 0,
        "datumEersteInschrijvingGBA": {
            "dag": 0,
            "datum": "string",
            "jaar": 0,
            "maand": 0
        },
        "kiesrecht": {
            "europeesKiesrecht": True,
            "uitgeslotenVanKiesrecht": True,
            "einddatumUitsluitingEuropeesKiesrecht": {
                "dag": 0,
                "datum": "string",
                "jaar": 0,
                "maand": 0
            },
            "einddatumUitsluitingKiesrecht": {
                "dag": 0,
                "datum": "string",
                "jaar": 0,
                "maand": 0
            }
        },
        "inOnderzoek": {
            "burgerservicenummer": bool(antwoord_dict_object['ns:inp.bsn']['#text']),
            "geslachtsaanduiding": bool(antwoord_dict_object['ns:geslachtsaanduiding']['#text']),
            "datumIngangOnderzoek": {
                "dag": 0,
                "datum": "string",
                "jaar": 0,
                "maand": 0
            }
        },
        "nationaliteit": [
            {
                "aanduidingBijzonderNederlanderschap": "behandeld_als_nederlander",
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
                    "aanduidingBijzonderNederlanderschap": True,
                    "nationaliteit": True,
                    "redenOpname": True,
                    "datumIngangOnderzoek": {
                        "dag": 0,
                        "datum": "string",
                        "jaar": 0,
                        "maand": 0
                    }
                }
            }
        ],
        "opschortingBijhouding": {
            "reden": "overlijden",
            "datum": {
                "dag": 0,
                "datum": "string",
                "jaar": 0,
                "maand": 0
            }
        },
        "overlijden": {
            "indicatieOverleden": True,
            "datum": {
                "dag": 0,
                "datum": "string",
                "jaar": 0,
                "maand": 0
            },
            "land": {
                "code": "string",
                "omschrijving": "string"
            },
            "plaats": {
                "code": "string",
                "omschrijving": "string"
            },
            "inOnderzoek": {
                "datum": True,
                "land": True,
                "plaats": True,
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0
                }
            }
        },
        "verblijfplaats": {
            "functieAdres": "woonadres",
            "huisletter": antwoord_dict_object['ns:verblijfsadres']['ns:aoa.huisletter']['#text'],
            "huisnummer": antwoord_dict_object['ns:verblijfsadres']['ns:aoa.huisnummer']['#text'],
            "huisnummertoevoeging": antwoord_dict_object['ns:verblijfsadres']['ns:aoa.huisnummertoevoeging']['#text'],
            "aanduidingBijHuisnummer": "tegenover",
            "identificatiecodeNummeraanduiding": "string",
            "naamOpenbareRuimte": "string",
            "postcode": antwoord_dict_object['ns:verblijfsadres']['ns:aoa.postcode']['#text'],
            "woonplaatsnaam": antwoord_dict_object['ns:verblijfsadres']['ns:wpl.woonplaatsNaam']['#text'],
            "identificatiecodeAdresseerbaarObject": "string",
            "indicatieVestigingVanuitBuitenland": True,
            "locatiebeschrijving": antwoord_dict_object['ns:verblijfsadres']['ns:inp.locatiebeschrijving']['#text'],
            "straatnaam": antwoord_dict_object['ns:verblijfsadres']['ns:gor.straatnaam']['#text'],
            "vanuitVertrokkenOnbekendWaarheen": True,
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
                "adresRegel1": antwoord_dict_object['ns:sub.verblijfBuitenland']['ns:sub.adresBuitenland1']['#text'],
                "adresRegel2": antwoord_dict_object['ns:sub.verblijfBuitenland']['ns:sub.adresBuitenland2']['#text'],
                "adresRegel3": antwoord_dict_object['ns:sub.verblijfBuitenland']['ns:sub.adresBuitenland3']['#text'],
                "vertrokkenOnbekendWaarheen": True,
                "land": {
                    "code": antwoord_dict_object['ns:sub.verblijfBuitenland']['ns:lnd.landcode']['#text'],
                    "omschrijving": antwoord_dict_object['ns:sub.verblijfBuitenland']['ns:lnd.landnaam']['#text']
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
                "huisletter": bool(antwoord_dict_object['ns:verblijfsadres']['ns:aoa.huisletter']['#text']),
                "huisnummer": bool(antwoord_dict_object['ns:verblijfsadres']['ns:aoa.huisnummer']['#text']),
                "huisnummertoevoeging": bool(antwoord_dict_object['ns:verblijfsadres']['ns:aoa.huisnummertoevoeging']['#text']),
                "identificatiecodeNummeraanduiding": True,
                "identificatiecodeAdresseerbaarObject": True,
                "landVanwaarIngeschreven": True,
                "locatiebeschrijving": bool(antwoord_dict_object['ns:verblijfsadres']['ns:inp.locatiebeschrijving']['#text']),
                "naamOpenbareRuimte": True,
                "postcode": bool(antwoord_dict_object['ns:verblijfsadres']['ns:aoa.postcode']['#text']),
                "straatnaam": bool(antwoord_dict_object['ns:verblijfsadres']['ns:gor.straatnaam']['#text']),
                "verblijfBuitenland": True,
                "woonplaatsnaam": bool(antwoord_dict_object['ns:verblijfsadres']['ns:wpl.woonplaatsNaam']['#text']),
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0
                }
            }
        },
        "gezagsverhouding": {
            "indicatieCurateleRegister": True,
            "indicatieGezagMinderjarige": "ouder1",
            "inOnderzoek": {
                "indicatieCurateleRegister": True,
                "indicatieGezagMinderjarige": True,
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0
                }
            }
        },
        "verblijfstitel": {
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
                "aanduiding": True,
                "datumEinde": True,
                "datumIngang": True,
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0
                }
            }
        },
        "reisdocumenten": [
            "string"
        ]
    }

    return ingeschreven_persoon_dict
