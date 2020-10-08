from django.conf import settings

import xmltodict

from openpersonen.contrib.utils import calculate_age, convert_empty_instances


def _get_client_instance_dict(instance_xml_dict, prefix):
    ingeschreven_persoon_dict = {
        "burgerservicenummer": instance_xml_dict.get(f"{prefix}:inp.bsn", "string"),
        "geheimhoudingPersoonsgegevens": True,
        "naam": {
            "geslachtsnaam": instance_xml_dict.get(f"{prefix}:geslachtsnaam", "string"),
            "voorletters": instance_xml_dict.get(f"{prefix}:voorletters", "string"),
            "voornamen": instance_xml_dict.get(f"{prefix}:voornamen", "string"),
            "voorvoegsel": instance_xml_dict.get(
                f"{prefix}:voorvoegselGeslachtsnaam", "string"
            ),
            "inOnderzoek": {
                "geslachtsnaam": bool(
                    instance_xml_dict.get(f"{prefix}:geslachtsnaam", "string")
                ),
                "voornamen": bool(
                    instance_xml_dict.get(f"{prefix}:voornamen", "string")
                ),
                "voorvoegsel": bool(
                    instance_xml_dict.get(
                        f"{prefix}:voorvoegselGeslachtsnaam", "string"
                    )
                ),
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0,
                },
            },
            "aanhef": instance_xml_dict.get(f"{prefix}:voornamen", "string"),
            "aanschrijfwijze": "string",
            "gebruikInLopendeTekst": "string",
            "aanduidingNaamgebruik": instance_xml_dict.get(
                f"{prefix}:aanduidingNaamgebruik", "string"
            ),
        },
        "geboorte": {
            "datum": {
                "dag": int(
                    instance_xml_dict.get(f"{prefix}:geboortedatum", "00000000")[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                ),
                "datum": instance_xml_dict.get(f"{prefix}:geboortedatum", "string"),
                "jaar": int(
                    instance_xml_dict.get(f"{prefix}:geboortedatum", "00000000")[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                ),
                "maand": int(
                    instance_xml_dict.get(f"{prefix}:geboortedatum", "00000000")[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                ),
            },
            "land": {
                "code": "string",
                "omschrijving": instance_xml_dict.get(
                    f"{prefix}:inp.geboorteLand", "string"
                ),
            },
            "plaats": {
                "code": "string",
                "omschrijving": instance_xml_dict.get(
                    f"{prefix}:inp.geboorteplaats", "string"
                ),
            },
            "inOnderzoek": {
                "datum": True,
                "land": True,
                "plaats": True,
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0,
                },
            },
        },
        "geslachtsaanduiding": instance_xml_dict.get(
            f"{prefix}:geslachtsaanduiding", "string"
        ),
        "leeftijd": calculate_age(
            instance_xml_dict.get(f"{prefix}:geboortedatum", "string")
        ),
        "datumEersteInschrijvingGBA": {
            "dag": int(
                instance_xml_dict.get(f"{prefix}:inp.datumInschrijving", "00000000")[
                    settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                ]
            ),
            "datum": instance_xml_dict.get(
                f"{prefix}:inp.datumInschrijving", "00000000"
            ),
            "jaar": int(
                instance_xml_dict.get(f"{prefix}:inp.datumInschrijving", "string")[
                    settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                ]
            ),
            "maand": int(
                instance_xml_dict.get(f"{prefix}:inp.datumInschrijving", "00000000")[
                    settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                ]
            ),
        },
        "kiesrecht": {
            "europeesKiesrecht": bool(
                instance_xml_dict.get(
                    f"{prefix}:ing.aanduidingEuropeesKiesrecht", "string"
                )
            ),
            "uitgeslotenVanKiesrecht": bool(
                instance_xml_dict.get(
                    f"{prefix}:ing.aanduidingUitgeslotenKiesrecht", "string"
                )
            ),
            "einddatumUitsluitingEuropeesKiesrecht": {
                "dag": int(
                    instance_xml_dict.get(
                        f"{prefix}:ing.aanduidingEuropeesKiesrecht", "00000000"
                    )[settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END]
                ),
                "datum": instance_xml_dict.get(
                    f"{prefix}:ing.aanduidingEuropeesKiesrecht", "string"
                ),
                "jaar": int(
                    instance_xml_dict.get(
                        f"{prefix}:ing.aanduidingEuropeesKiesrecht", "00000000"
                    )[settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END]
                ),
                "maand": int(
                    instance_xml_dict.get(
                        f"{prefix}:ing.aanduidingEuropeesKiesrecht", "00000000"
                    )[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                ),
            },
            "einddatumUitsluitingKiesrecht": {
                "dag": int(
                    instance_xml_dict.get(
                        f"{prefix}:ing.aanduidingUitgeslotenKiesrecht", "00000000"
                    )[settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END]
                ),
                "datum": instance_xml_dict.get(
                    f"{prefix}:ing.aanduidingUitgeslotenKiesrecht", "string"
                ),
                "jaar": int(
                    instance_xml_dict.get(
                        f"{prefix}:ing.aanduidingUitgeslotenKiesrecht", "00000000"
                    )[settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END]
                ),
                "maand": int(
                    instance_xml_dict.get(
                        f"{prefix}:ing.aanduidingUitgeslotenKiesrecht", "00000000"
                    )[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                ),
            },
        },
        "inOnderzoek": {
            "burgerservicenummer": bool(
                instance_xml_dict.get(f"{prefix}:inp.bsn", "string")
            ),
            "geslachtsaanduiding": bool(
                instance_xml_dict.get(f"{prefix}:geslachtsaanduiding", "string")
            ),
            "datumIngangOnderzoek": {
                "dag": 0,
                "datum": "string",
                "jaar": 0,
                "maand": 0,
            },
        },
        "nationaliteit": [
            {
                "aanduidingBijzonderNederlanderschap": instance_xml_dict.get(
                    f"{prefix}:inp.aanduidingBijzonderNederlanderschap", "string"
                ),
                "datumIngangGeldigheid": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0,
                },
                "nationaliteit": {"code": "string", "omschrijving": "string"},
                "redenOpname": {"code": "string", "omschrijving": "string"},
                "inOnderzoek": {
                    "aanduidingBijzonderNederlanderschap": bool(
                        instance_xml_dict.get(
                            f"{prefix}:inp.aanduidingBijzonderNederlanderschap",
                            "string",
                        )
                    ),
                    "nationaliteit": True,
                    "redenOpname": True,
                    "datumIngangOnderzoek": {
                        "dag": 0,
                        "datum": "string",
                        "jaar": 0,
                        "maand": 0,
                    },
                },
            }
        ],
        "opschortingBijhouding": {
            "reden": "overlijden",
            "datum": {"dag": 0, "datum": "string", "jaar": 0, "maand": 0},
        },
        "overlijden": {
            "indicatieOverleden": True,
            "datum": {"dag": 0, "datum": "string", "jaar": 0, "maand": 0},
            "land": {
                "code": "string",
                "omschrijving": instance_xml_dict.get(
                    f"{prefix}:inp.overlijdenLand", "string"
                ),
            },
            "plaats": {
                "code": "string",
                "omschrijving": instance_xml_dict.get(
                    f"{prefix}:inp.overlijdenplaats", "string"
                ),
            },
            "inOnderzoek": {
                "datum": bool(
                    instance_xml_dict.get(f"{prefix}:overlijdensdatum", "string")
                ),
                "land": bool(
                    instance_xml_dict.get(f"{prefix}:inp.overlijdenLand", "string")
                ),
                "plaats": bool(
                    instance_xml_dict.get(f"{prefix}:inp.overlijdenplaats", "string")
                ),
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0,
                },
            },
        },
        "verblijfplaats": {
            "functieAdres": "woonadres",
            "huisletter": instance_xml_dict.get(f"{prefix}:verblijfsadres", {}).get(
                f"{prefix}:aoa.huisletter", "string"
            ),
            "huisnummer": instance_xml_dict.get(f"{prefix}:verblijfsadres", {}).get(
                f"{prefix}:aoa.huisnummer", "string"
            ),
            "huisnummertoevoeging": instance_xml_dict.get(
                f"{prefix}:verblijfsadres", {}
            ).get(f"{prefix}:aoa.huisnummertoevoeging", "string"),
            "aanduidingBijHuisnummer": "tegenover",
            "identificatiecodeNummeraanduiding": "string",
            "naamOpenbareRuimte": "string",
            "postcode": instance_xml_dict.get(f"{prefix}:verblijfsadres", {}).get(
                f"{prefix}:aoa.postcode", "string"
            ),
            "woonplaatsnaam": instance_xml_dict.get(f"{prefix}:verblijfsadres", {}).get(
                f"{prefix}:wpl.woonplaatsNaam", "string"
            ),
            "identificatiecodeAdresseerbaarObject": "string",
            "indicatieVestigingVanuitBuitenland": True,
            "locatiebeschrijving": "string",
            "straatnaam": instance_xml_dict.get(f"{prefix}:verblijfsadres", {}).get(
                f"{prefix}:gor.straatnaam", "string"
            ),
            "vanuitVertrokkenOnbekendWaarheen": True,
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
            "gemeenteVanInschrijving": {"code": "string", "omschrijving": "string"},
            "landVanwaarIngeschreven": {"code": "string", "omschrijving": "string"},
            "verblijfBuitenland": {
                "adresRegel1": "string",
                "adresRegel2": "string",
                "adresRegel3": "string",
                "vertrokkenOnbekendWaarheen": True,
                "land": {"code": "string", "omschrijving": "string"},
            },
            "inOnderzoek": {
                "aanduidingBijHuisnummer": True,
                "datumAanvangAdreshouding": True,
                "datumIngangGeldigheid": True,
                "datumInschrijvingInGemeente": True,
                "datumVestigingInNederland": True,
                "functieAdres": True,
                "gemeenteVanInschrijving": True,
                "huisletter": bool(
                    instance_xml_dict.get(f"{prefix}:verblijfsadres", {}).get(
                        f"{prefix}:aoa.huisletter", "string"
                    )
                ),
                "huisnummer": bool(
                    instance_xml_dict.get(f"{prefix}:verblijfsadres", {}).get(
                        f"{prefix}:aoa.huisnummer", "string"
                    )
                ),
                "huisnummertoevoeging": bool(
                    instance_xml_dict.get(f"{prefix}:verblijfsadres", {}).get(
                        f"{prefix}:aoa.huisnummertoevoeging", "string"
                    )
                ),
                "identificatiecodeNummeraanduiding": True,
                "identificatiecodeAdresseerbaarObject": True,
                "landVanwaarIngeschreven": True,
                "locatiebeschrijving": True,
                "naamOpenbareRuimte": True,
                "postcode": bool(
                    instance_xml_dict.get(f"{prefix}:verblijfsadres", {}).get(
                        f"{prefix}:aoa.postcode", "string"
                    )
                ),
                "straatnaam": bool(
                    instance_xml_dict.get(f"{prefix}:verblijfsadres", {}).get(
                        f"{prefix}:gor.straatnaam", "string"
                    )
                ),
                "verblijfBuitenland": True,
                "woonplaatsnaam": bool(
                    instance_xml_dict.get(f"{prefix}:verblijfsadres", {}).get(
                        f"{prefix}:wpl.woonplaatsNaam", "string"
                    )
                ),
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0,
                },
            },
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
                    "maand": 0,
                },
            },
        },
        "verblijfstitel": {
            "aanduiding": {"code": "string", "omschrijving": "string"},
            "datumEinde": {"dag": 0, "datum": "string", "jaar": 0, "maand": 0},
            "datumIngang": {"dag": 0, "datum": "string", "jaar": 0, "maand": 0},
            "inOnderzoek": {
                "aanduiding": True,
                "datumEinde": True,
                "datumIngang": True,
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0,
                },
            },
        },
        "reisdocumenten": ["string"],
    }

    convert_empty_instances(ingeschreven_persoon_dict)

    return ingeschreven_persoon_dict


def convert_response_to_persoon_dicts(response):
    dict_object = xmltodict.parse(response.content)

    try:
        antwoord_object = dict_object["soapenv:Envelope"]["soapenv:Body"]["ns:npsLa01"][
            "ns:antwoord"
        ]["ns:object"]
        prefix = "ns"
    except KeyError:
        antwoord_object = dict_object["env:Envelope"]["env:Body"]["npsLa01"][
            "BG:antwoord"
        ]["object"]
        prefix = "BG"

    if isinstance(antwoord_object, list):
        result = []
        for antwood_dict in antwoord_object:
            result_dict = _get_client_instance_dict(antwood_dict, prefix)
            result.append(result_dict)
    else:
        result = [_get_client_instance_dict(antwoord_object, prefix)]

    return result
