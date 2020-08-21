import xmltodict


def get_ingeschreven_persoon_dict(response):

    dict_object = xmltodict.parse(response.content)

    antwoord_dict_object = dict_object['env:Envelope']['env:Body']['npsLa01']['BG:antwoord']['object']

    ingeschreven_persoon_dict = {
        "burgerservicenummer": antwoord_dict_object['BG:inp.bsn'],
        "geheimhoudingPersoonsgegevens": True,
        "naam": {
            "geslachtsnaam": antwoord_dict_object['BG:geslachtsnaam'],
            "voorletters": antwoord_dict_object['BG:voorletters'],
            "voornamen": antwoord_dict_object['BG:voornamen'],
            "voorvoegsel": antwoord_dict_object['BG:voorvoegselGeslachtsnaam'],
            "inOnderzoek": {
                "geslachtsnaam": bool(antwoord_dict_object['BG:geslachtsnaam']),
                "voornamen": bool(antwoord_dict_object['BG:voornamen']),
                "voorvoegsel": bool(antwoord_dict_object['BG:voorvoegselGeslachtsnaam']),
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0
                }
            },
            "aanhef": "string",
            "aanschrijfwijze": "string",
            "gebruikInLopendeTekst": "string",
            "aanduidingNaamgebruik": antwoord_dict_object['BG:aanduidingNaamgebruik']
        },
        "geboorte": {
            "datum": {
                "dag": antwoord_dict_object['BG:geboortedatum'][6:8],
                "datum": antwoord_dict_object['BG:geboortedatum'],
                "jaar": antwoord_dict_object['BG:geboortedatum'][0:4],
                "maand": antwoord_dict_object['BG:geboortedatum'][4:6]
            },
            "land": {
                "code": "string",
                "omschrijving": antwoord_dict_object['BG:inp.geboorteLand']
            },
            "plaats": {
                "code": "string",
                "omschrijving": antwoord_dict_object['BG:inp.geboorteplaats']
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
        "geslachtsaanduiding": antwoord_dict_object['BG:geslachtsaanduiding'],
        "leeftijd": 0,  # TODO Calculate this
        "datumEersteInschrijvingGBA": {
            "dag": antwoord_dict_object['BG:inp.datumInschrijving'][6:8],
            "datum": antwoord_dict_object['BG:inp.datumInschrijving'],
            "jaar": antwoord_dict_object['BG:inp.datumInschrijving'][0:4],
            "maand": antwoord_dict_object['BG:inp.datumInschrijving'][4:6]
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
            "burgerservicenummer": bool(antwoord_dict_object['BG:inp.bsn']),
            "geslachtsaanduiding": bool(antwoord_dict_object['BG:geslachtsaanduiding']),
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
            "huisletter": "string",
            "huisnummer": antwoord_dict_object['BG:verblijfsadres']['BG:aoa.huisnummer'],
            "huisnummertoevoeging": "string",
            "aanduidingBijHuisnummer": "tegenover",
            "identificatiecodeNummeraanduiding": "string",
            "naamOpenbareRuimte": "string",
            "postcode": antwoord_dict_object['BG:verblijfsadres']['BG:aoa.postcode'],
            "woonplaatsnaam": antwoord_dict_object['BG:verblijfsadres']['BG:wpl.woonplaatsNaam'],
            "identificatiecodeAdresseerbaarObject": "string",
            "indicatieVestigingVanuitBuitenland": True,
            "locatiebeschrijving": "string",
            "straatnaam": antwoord_dict_object['BG:verblijfsadres']['BG:gor.straatnaam'],
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
                "adresRegel1": "string",
                "adresRegel2": "string",
                "adresRegel3": "string",
                "vertrokkenOnbekendWaarheen": True,
                "land": {
                    "code": "string",
                    "omschrijving": "string"
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
                "huisnummer": bool(antwoord_dict_object['BG:verblijfsadres']['BG:aoa.huisnummer']),
                "huisnummertoevoeging": True,
                "identificatiecodeNummeraanduiding": True,
                "identificatiecodeAdresseerbaarObject": True,
                "landVanwaarIngeschreven": True,
                "locatiebeschrijving": True,
                "naamOpenbareRuimte": True,
                "postcode": bool(antwoord_dict_object['BG:verblijfsadres']['BG:aoa.postcode']),
                "straatnaam": bool(antwoord_dict_object['BG:verblijfsadres']['BG:gor.straatnaam']),
                "verblijfBuitenland": True,
                "woonplaatsnaam": bool(antwoord_dict_object['BG:verblijfsadres']['BG:wpl.woonplaatsNaam']),
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
