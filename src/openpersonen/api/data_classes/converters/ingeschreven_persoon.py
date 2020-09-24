from django.conf import settings

import xmltodict

from openpersonen.api.utils import (
    calculate_age,
    convert_empty_instances,
    is_valid_date_format,
)


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
                        settings.DAY_START : settings.DAY_END
                    ]
                ),
                "datum": instance_xml_dict.get(f"{prefix}:geboortedatum", "string"),
                "jaar": int(
                    instance_xml_dict.get(f"{prefix}:geboortedatum", "00000000")[
                        settings.YEAR_START : settings.YEAR_END
                    ]
                ),
                "maand": int(
                    instance_xml_dict.get(f"{prefix}:geboortedatum", "00000000")[
                        settings.MONTH_START : settings.MONTH_END
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
                    settings.DAY_START : settings.DAY_END
                ]
            ),
            "datum": instance_xml_dict.get(
                f"{prefix}:inp.datumInschrijving", "00000000"
            ),
            "jaar": int(
                instance_xml_dict.get(f"{prefix}:inp.datumInschrijving", "string")[
                    settings.YEAR_START : settings.YEAR_END
                ]
            ),
            "maand": int(
                instance_xml_dict.get(f"{prefix}:inp.datumInschrijving", "00000000")[
                    settings.MONTH_START : settings.MONTH_END
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
                    )[settings.DAY_START : settings.DAY_END]
                ),
                "datum": instance_xml_dict.get(
                    f"{prefix}:ing.aanduidingEuropeesKiesrecht", "string"
                ),
                "jaar": int(
                    instance_xml_dict.get(
                        f"{prefix}:ing.aanduidingEuropeesKiesrecht", "00000000"
                    )[settings.YEAR_START : settings.YEAR_END]
                ),
                "maand": int(
                    instance_xml_dict.get(
                        f"{prefix}:ing.aanduidingEuropeesKiesrecht", "00000000"
                    )[settings.MONTH_START : settings.MONTH_END]
                ),
            },
            "einddatumUitsluitingKiesrecht": {
                "dag": int(
                    instance_xml_dict.get(
                        f"{prefix}:ing.aanduidingUitgeslotenKiesrecht", "00000000"
                    )[settings.DAY_START : settings.DAY_END]
                ),
                "datum": instance_xml_dict.get(
                    f"{prefix}:ing.aanduidingUitgeslotenKiesrecht", "string"
                ),
                "jaar": int(
                    instance_xml_dict.get(
                        f"{prefix}:ing.aanduidingUitgeslotenKiesrecht", "00000000"
                    )[settings.YEAR_START : settings.YEAR_END]
                ),
                "maand": int(
                    instance_xml_dict.get(
                        f"{prefix}:ing.aanduidingUitgeslotenKiesrecht", "00000000"
                    )[settings.MONTH_START : settings.MONTH_END]
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


def convert_client_response(response):
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
        result = _get_client_instance_dict(antwoord_object, prefix)

    return result


def convert_model_instance_to_instance_dict(persoon):

    ingeschreven_persoon_dict = {
        "burgerservicenummer": persoon.burgerservicenummer_persoon,
        "geheimhoudingPersoonsgegevens": True,
        "naam": {
            "geslachtsnaam": persoon.geslachtsnaam_persoon,
            "voorletters": "string",
            "voornamen": persoon.voornamen_persoon,
            "voorvoegsel": persoon.voorvoegsel_geslachtsnaam_persoon,
            "inOnderzoek": {
                "geslachtsnaam": bool(persoon.geslachtsnaam_persoon),
                "voornamen": bool(persoon.voornamen_persoon),
                "voorvoegsel": bool(persoon.voorvoegsel_geslachtsnaam_persoon),
                "datumIngangOnderzoek": {
                    "dag": int(
                        persoon.datum_ingang_onderzoek[
                            settings.DAY_START : settings.DAY_END
                        ]
                    )
                    if is_valid_date_format(persoon.datum_ingang_onderzoek)
                    else 0,
                    "datum": persoon.datum_ingang_onderzoek,
                    "jaar": int(
                        persoon.datum_ingang_onderzoek[
                            settings.YEAR_START : settings.YEAR_END
                        ]
                    )
                    if is_valid_date_format(persoon.datum_ingang_onderzoek)
                    else 0,
                    "maand": int(
                        persoon.datum_ingang_onderzoek[
                            settings.MONTH_START : settings.MONTH_END
                        ]
                    )
                    if is_valid_date_format(persoon.datum_ingang_onderzoek)
                    else 0,
                },
            },
            "aanhef": "string",
            "aanschrijfwijze": "string",
            "gebruikInLopendeTekst": "string",
            "aanduidingNaamgebruik": persoon.aanduiding_naamgebruik,
        },
        "geboorte": {
            "datum": {
                "dag": int(
                    persoon.geboortedatum_persoon[settings.DAY_START : settings.DAY_END]
                )
                if is_valid_date_format(persoon.geboortedatum_persoon)
                else 0,
                "datum": persoon.geboortedatum_persoon,
                "jaar": int(
                    persoon.geboortedatum_persoon[
                        settings.YEAR_START : settings.YEAR_END
                    ]
                )
                if is_valid_date_format(persoon.geboortedatum_persoon)
                else 0,
                "maand": int(
                    persoon.geboortedatum_persoon[
                        settings.MONTH_START : settings.MONTH_END
                    ]
                )
                if is_valid_date_format(persoon.geboortedatum_persoon)
                else 0,
            },
            "land": {
                "code": "string",
                "omschrijving": persoon.geboorteland_persoon,
            },
            "plaats": {
                "code": "string",
                "omschrijving": persoon.geboorteplaats_persoon,
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
        "geslachtsaanduiding": persoon.geslachtsaanduiding,
        "leeftijd": calculate_age(persoon.geboortedatum_persoon),
        "datumEersteInschrijvingGBA": {
            "dag": 0,
            "datum": "string",
            "jaar": 0,
            "maand": 0,
        },
        "inOnderzoek": {
            "burgerservicenummer": bool(persoon.burgerservicenummer_persoon),
            "geslachtsaanduiding": bool(persoon.geslachtsaanduiding),
            "datumIngangOnderzoek": {
                "dag": 0,
                "datum": "string",
                "jaar": 0,
                "maand": 0,
            },
        },
        "opschortingBijhouding": {
            "reden": "overlijden",
            "datum": {"dag": 0, "datum": "string", "jaar": 0, "maand": 0},
        },
    }

    ingeschreven_persoon_dict["kiesrecht"] = dict()
    kiesrecht = persoon.kiesrecht_set.first()
    if kiesrecht:
        ingeschreven_persoon_dict["kiesrecht"] = {
            "europeesKiesrecht": bool(kiesrecht.aanduiding_europees_kiesrecht),
            "uitgeslotenVanKiesrecht": bool(kiesrecht.aanduiding_uitgesloten_kiesrecht),
            "einddatumUitsluitingEuropeesKiesrecht": {
                "dag": int(
                    kiesrecht.einddatum_uitsluiting_europees_kiesrecht[
                        settings.DAY_START : settings.DAY_END
                    ]
                )
                if is_valid_date_format(
                    kiesrecht.einddatum_uitsluiting_europees_kiesrecht
                )
                else 0,
                "datum": kiesrecht.einddatum_uitsluiting_europees_kiesrecht,
                "jaar": int(
                    kiesrecht.einddatum_uitsluiting_europees_kiesrecht[
                        settings.YEAR_START : settings.YEAR_END
                    ]
                )
                if is_valid_date_format(
                    kiesrecht.einddatum_uitsluiting_europees_kiesrecht
                )
                else 0,
                "maand": int(
                    kiesrecht.einddatum_uitsluiting_europees_kiesrecht[
                        settings.MONTH_START : settings.MONTH_END
                    ]
                )
                if is_valid_date_format(
                    kiesrecht.einddatum_uitsluiting_europees_kiesrecht
                )
                else 0,
            },
            "einddatumUitsluitingKiesrecht": {
                "dag": int(
                    kiesrecht.einddatum_uitsluiting_kiesrecht[
                        settings.DAY_START : settings.DAY_END
                    ]
                )
                if is_valid_date_format(kiesrecht.einddatum_uitsluiting_kiesrecht)
                else 0,
                "datum": kiesrecht.einddatum_uitsluiting_kiesrecht,
                "jaar": int(
                    kiesrecht.einddatum_uitsluiting_kiesrecht[
                        settings.YEAR_START : settings.YEAR_END
                    ]
                )
                if is_valid_date_format(kiesrecht.einddatum_uitsluiting_kiesrecht)
                else 0,
                "maand": int(
                    kiesrecht.einddatum_uitsluiting_kiesrecht[
                        settings.MONTH_START : settings.MONTH_END
                    ]
                )
                if is_valid_date_format(kiesrecht.einddatum_uitsluiting_kiesrecht)
                else 0,
            },
        }

    ingeschreven_persoon_dict["overlijden"] = dict()
    overlijden = persoon.overlijden_set.first()
    if overlijden:
        ingeschreven_persoon_dict["overlijden"] = {
            "indicatieOverleden": True,
            "datum": {
                "dag": int(
                    overlijden.datum_overlijden[settings.DAY_START : settings.DAY_END]
                )
                if is_valid_date_format(overlijden.datum_overlijden)
                else 0,
                "datum": overlijden.datum_overlijden,
                "jaar": int(
                    overlijden.datum_overlijden[settings.YEAR_START : settings.YEAR_END]
                )
                if is_valid_date_format(overlijden.datum_overlijden)
                else 0,
                "maand": int(
                    overlijden.datum_overlijden[
                        settings.MONTH_START : settings.MONTH_END
                    ]
                )
                if is_valid_date_format(overlijden.datum_overlijden)
                else 0,
            },
            "land": {
                "code": "string",
                "omschrijving": overlijden.land_overlijden,
            },
            "plaats": {
                "code": "string",
                "omschrijving": overlijden.plaats_overlijden,
            },
            "inOnderzoek": {
                "datum": bool(overlijden.datum_overlijden),
                "land": bool(overlijden.land_overlijden),
                "plaats": bool(overlijden.plaats_overlijden),
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0,
                },
            },
        }

    ingeschreven_persoon_dict["verblijfplaats"] = dict()
    verblijfplaats = persoon.verblijfplaats_set.first()
    if verblijfplaats:
        ingeschreven_persoon_dict["verblijfplaats"] = {
            "functieAdres": verblijfplaats.functie_adres,
            "huisletter": verblijfplaats.huisletter,
            "huisnummer": verblijfplaats.huisnummer,
            "huisnummertoevoeging": verblijfplaats.huisnummertoevoeging,
            "aanduidingBijHuisnummer": verblijfplaats.aanduiding_bij_huisnummer,
            "identificatiecodeNummeraanduiding": verblijfplaats.identificatiecode_nummeraanduiding,
            "naamOpenbareRuimte": verblijfplaats.naam_openbare_ruimte,
            "postcode": verblijfplaats.postcode,
            "woonplaatsnaam": verblijfplaats.woonplaatsnaam,
            "identificatiecodeAdresseerbaarObject": "string",
            "indicatieVestigingVanuitBuitenland": True,
            "locatiebeschrijving": verblijfplaats.locatiebeschrijving,
            "straatnaam": verblijfplaats.straatnaam,
            "vanuitVertrokkenOnbekendWaarheen": True,
            "datumAanvangAdreshouding": {
                "dag": int(
                    verblijfplaats.datum_aanvang_adres_buitenland[
                        settings.DAY_START : settings.DAY_END
                    ]
                )
                if is_valid_date_format(verblijfplaats.datum_aanvang_adres_buitenland)
                else 0,
                "datum": verblijfplaats.datum_aanvang_adres_buitenland,
                "jaar": int(
                    verblijfplaats.datum_aanvang_adres_buitenland[
                        settings.YEAR_START : settings.YEAR_END
                    ]
                )
                if is_valid_date_format(verblijfplaats.datum_aanvang_adres_buitenland)
                else 0,
                "maand": int(
                    verblijfplaats.datum_aanvang_adres_buitenland[
                        settings.MONTH_START : settings.MONTH_END
                    ]
                )
                if is_valid_date_format(verblijfplaats.datum_aanvang_adres_buitenland)
                else 0,
            },
            "datumIngangGeldigheid": {
                "dag": int(
                    verblijfplaats.ingangsdatum_geldigheid_met_betrekking[
                        settings.DAY_START : settings.DAY_END
                    ]
                )
                if is_valid_date_format(
                    verblijfplaats.ingangsdatum_geldigheid_met_betrekking
                )
                else 0,
                "datum": verblijfplaats.ingangsdatum_geldigheid_met_betrekking,
                "jaar": int(
                    verblijfplaats.ingangsdatum_geldigheid_met_betrekking[
                        settings.YEAR_START : settings.YEAR_END
                    ]
                )
                if is_valid_date_format(
                    verblijfplaats.ingangsdatum_geldigheid_met_betrekking
                )
                else 0,
                "maand": int(
                    verblijfplaats.ingangsdatum_geldigheid_met_betrekking[
                        settings.MONTH_START : settings.MONTH_END
                    ]
                )
                if is_valid_date_format(
                    verblijfplaats.ingangsdatum_geldigheid_met_betrekking
                )
                else 0,
            },
            "datumInschrijvingInGemeente": {
                "dag": int(
                    verblijfplaats.datum_inschrijving_in_de_gemeente[
                        settings.DAY_START : settings.DAY_END
                    ]
                )
                if is_valid_date_format(
                    verblijfplaats.datum_inschrijving_in_de_gemeente
                )
                else 0,
                "datum": verblijfplaats.datum_inschrijving_in_de_gemeente,
                "jaar": int(
                    verblijfplaats.datum_inschrijving_in_de_gemeente[
                        settings.YEAR_START : settings.YEAR_END
                    ]
                )
                if is_valid_date_format(
                    verblijfplaats.datum_inschrijving_in_de_gemeente
                )
                else 0,
                "maand": int(
                    verblijfplaats.datum_inschrijving_in_de_gemeente[
                        settings.MONTH_START : settings.MONTH_END
                    ]
                )
                if is_valid_date_format(
                    verblijfplaats.datum_inschrijving_in_de_gemeente
                )
                else 0,
            },
            "datumVestigingInNederland": {
                "dag": int(
                    verblijfplaats.datum_vestiging_in_nederland[
                        settings.DAY_START : settings.DAY_END
                    ]
                )
                if is_valid_date_format(verblijfplaats.datum_vestiging_in_nederland)
                else 0,
                "datum": verblijfplaats.datum_vestiging_in_nederland,
                "jaar": int(
                    verblijfplaats.datum_vestiging_in_nederland[
                        settings.YEAR_START : settings.YEAR_END
                    ]
                )
                if is_valid_date_format(verblijfplaats.datum_vestiging_in_nederland)
                else 0,
                "maand": int(
                    verblijfplaats.datum_vestiging_in_nederland[
                        settings.MONTH_START : settings.MONTH_END
                    ]
                )
                if is_valid_date_format(verblijfplaats.datum_vestiging_in_nederland)
                else 0,
            },
            "gemeenteVanInschrijving": {
                "code": "string",
                "omschrijving": verblijfplaats.gemeente_van_inschrijving,
            },
            "landVanwaarIngeschreven": {
                "code": "string",
                "omschrijving": verblijfplaats.land_vanwaar_ingeschreven,
            },
            "verblijfBuitenland": {
                "adresRegel1": verblijfplaats.regel_1_adres_buitenland,
                "adresRegel2": verblijfplaats.regel_2_adres_buitenland,
                "adresRegel3": verblijfplaats.regel_3_adres_buitenland,
                "vertrokkenOnbekendWaarheen": True,
                "land": {"code": "string", "omschrijving": "string"},
            },
            "inOnderzoek": {
                "aanduidingBijHuisnummer": bool(
                    verblijfplaats.aanduiding_bij_huisnummer
                ),
                "datumAanvangAdreshouding": bool(
                    verblijfplaats.datum_aanvang_adreshouding
                ),
                "datumIngangGeldigheid": True,
                "datumInschrijvingInGemeente": bool(
                    verblijfplaats.datum_inschrijving_in_de_gemeente
                ),
                "datumVestigingInNederland": bool(
                    verblijfplaats.datum_vestiging_in_nederland
                ),
                "functieAdres": True,
                "gemeenteVanInschrijving": bool(
                    verblijfplaats.gemeente_van_inschrijving
                ),
                "huisletter": bool(verblijfplaats.huisletter),
                "huisnummer": bool(verblijfplaats.huisnummer),
                "huisnummertoevoeging": bool(verblijfplaats.huisnummertoevoeging),
                "identificatiecodeNummeraanduiding": bool(
                    verblijfplaats.identificatiecode_nummeraanduiding
                ),
                "identificatiecodeAdresseerbaarObject": True,
                "landVanwaarIngeschreven": bool(
                    verblijfplaats.land_vanwaar_ingeschreven
                ),
                "locatiebeschrijving": bool(verblijfplaats.locatiebeschrijving),
                "naamOpenbareRuimte": bool(verblijfplaats.naam_openbare_ruimte),
                "postcode": bool(verblijfplaats.postcode),
                "straatnaam": bool(verblijfplaats.straatnaam),
                "verblijfBuitenland": True,
                "woonplaatsnaam": bool(verblijfplaats.woonplaatsnaam),
                "datumIngangOnderzoek": {
                    "dag": int(
                        verblijfplaats.datum_ingang_onderzoek[
                            settings.DAY_START : settings.DAY_END
                        ]
                    )
                    if is_valid_date_format(verblijfplaats.datum_ingang_onderzoek)
                    else 0,
                    "datum": verblijfplaats.datum_ingang_onderzoek,
                    "jaar": int(
                        verblijfplaats.datum_ingang_onderzoek[
                            settings.YEAR_START : settings.YEAR_END
                        ]
                    )
                    if is_valid_date_format(verblijfplaats.datum_ingang_onderzoek)
                    else 0,
                    "maand": int(
                        verblijfplaats.datum_ingang_onderzoek[
                            settings.MONTH_START : settings.MONTH_END
                        ]
                    )
                    if is_valid_date_format(verblijfplaats.datum_ingang_onderzoek)
                    else 0,
                },
            },
        }

    ingeschreven_persoon_dict["gezagsverhouding"] = dict()
    gezagsverhouding = persoon.gezagsverhouding_set.first()
    if gezagsverhouding:
        ingeschreven_persoon_dict["gezagsverhouding"] = {
            "indicatieCurateleRegister": gezagsverhouding.indicatie_curateleregister,
            "indicatieGezagMinderjarige": gezagsverhouding.indicatie_gezag_minderjarige,
            "inOnderzoek": {
                "indicatieCurateleRegister": bool(
                    gezagsverhouding.indicatie_curateleregister
                ),
                "indicatieGezagMinderjarige": bool(
                    gezagsverhouding.indicatie_gezag_minderjarige
                ),
                "datumIngangOnderzoek": {
                    "dag": int(
                        gezagsverhouding.datum_ingang_onderzoek[
                            settings.DAY_START : settings.DAY_END
                        ]
                    )
                    if is_valid_date_format(gezagsverhouding.datum_ingang_onderzoek)
                    else 0,
                    "datum": gezagsverhouding.datum_ingang_onderzoek,
                    "jaar": int(
                        gezagsverhouding.datum_ingang_onderzoek[
                            settings.YEAR_START : settings.YEAR_END
                        ]
                    )
                    if is_valid_date_format(gezagsverhouding.datum_ingang_onderzoek)
                    else 0,
                    "maand": int(
                        gezagsverhouding.datum_ingang_onderzoek[
                            settings.MONTH_START : settings.MONTH_END
                        ]
                    )
                    if is_valid_date_format(gezagsverhouding.datum_ingang_onderzoek)
                    else 0,
                },
            },
        }

    ingeschreven_persoon_dict["verblijfstitel"] = dict()
    verblijfstitel = persoon.verblijfstitel_set.first()
    if verblijfstitel:
        ingeschreven_persoon_dict["verblijfstitel"] = {
            "aanduiding": {
                "code": "string",
                "omschrijving": verblijfstitel.aanduiding_verblijfstitel,
            },
            "datumEinde": {
                "dag": int(
                    verblijfstitel.datum_einde_verblijfstitel[
                        settings.DAY_START : settings.DAY_END
                    ]
                )
                if is_valid_date_format(verblijfstitel.datum_einde_verblijfstitel)
                else 0,
                "datum": verblijfstitel.datum_einde_verblijfstitel,
                "jaar": int(
                    verblijfstitel.datum_einde_verblijfstitel[
                        settings.YEAR_START : settings.YEAR_END
                    ]
                )
                if is_valid_date_format(verblijfstitel.datum_einde_verblijfstitel)
                else 0,
                "maand": int(
                    verblijfstitel.datum_einde_verblijfstitel[
                        settings.MONTH_START : settings.MONTH_END
                    ]
                )
                if is_valid_date_format(verblijfstitel.datum_einde_verblijfstitel)
                else 0,
            },
            "datumIngang": {
                "dag": int(
                    verblijfstitel.ingangsdatum_verblijfstitel[
                        settings.DAY_START : settings.DAY_END
                    ]
                )
                if is_valid_date_format(verblijfstitel.ingangsdatum_verblijfstitel)
                else 0,
                "datum": verblijfstitel.ingangsdatum_verblijfstitel,
                "jaar": int(
                    verblijfstitel.ingangsdatum_verblijfstitel[
                        settings.YEAR_START : settings.YEAR_END
                    ]
                )
                if is_valid_date_format(verblijfstitel.ingangsdatum_verblijfstitel)
                else 0,
                "maand": int(
                    verblijfstitel.ingangsdatum_verblijfstitel[
                        settings.MONTH_START : settings.MONTH_END
                    ]
                )
                if is_valid_date_format(verblijfstitel.ingangsdatum_verblijfstitel)
                else 0,
            },
            "inOnderzoek": {
                "aanduiding": bool(verblijfstitel.aanduiding_verblijfstitel),
                "datumEinde": bool(verblijfstitel.datum_einde_verblijfstitel),
                "datumIngang": bool(verblijfstitel.ingangsdatum_verblijfstitel),
                "datumIngangOnderzoek": {
                    "dag": int(
                        verblijfstitel.datum_ingang_onderzoek[
                            settings.DAY_START : settings.DAY_END
                        ]
                    )
                    if is_valid_date_format(verblijfstitel.datum_ingang_onderzoek)
                    else 0,
                    "datum": verblijfstitel.datum_ingang_onderzoek,
                    "jaar": int(
                        verblijfstitel.datum_ingang_onderzoek[
                            settings.YEAR_START : settings.YEAR_END
                        ]
                    )
                    if is_valid_date_format(verblijfstitel.datum_ingang_onderzoek)
                    else 0,
                    "maand": int(
                        verblijfstitel.datum_ingang_onderzoek[
                            settings.MONTH_START : settings.MONTH_END
                        ]
                    )
                    if is_valid_date_format(verblijfstitel.datum_ingang_onderzoek)
                    else 0,
                },
            },
        }

    ingeschreven_persoon_dict["nationaliteit"] = []

    nationaliteiten = persoon.nationaliteit_set.all()

    for nationaliteit in nationaliteiten:
        ingeschreven_persoon_dict["nationaliteit"].append(
            {
                "aanduidingBijzonderNederlanderschap": nationaliteit.aanduiding_bijzonder_nederlanderschap,
                "datumIngangGeldigheid": {
                    "dag": int(
                        nationaliteit.datum_van_ingang_geldigheid_met_betrekking[
                            settings.DAY_START : settings.DAY_END
                        ]
                    )
                    if is_valid_date_format(
                        nationaliteit.datum_van_ingang_geldigheid_met_betrekking
                    )
                    else 0,
                    "datum": nationaliteit.datum_van_ingang_geldigheid_met_betrekking,
                    "jaar": int(
                        nationaliteit.datum_van_ingang_geldigheid_met_betrekking[
                            settings.YEAR_START : settings.YEAR_END
                        ]
                    )
                    if is_valid_date_format(
                        nationaliteit.datum_van_ingang_geldigheid_met_betrekking
                    )
                    else 0,
                    "maand": int(
                        nationaliteit.datum_van_ingang_geldigheid_met_betrekking[
                            settings.MONTH_START : settings.MONTH_END
                        ]
                    )
                    if is_valid_date_format(
                        nationaliteit.datum_van_ingang_geldigheid_met_betrekking
                    )
                    else 0,
                },
                "nationaliteit": {
                    "code": "string",
                    "omschrijving": nationaliteit.nationaliteit,
                },
                "redenOpname": {
                    "code": "string",
                    "omschrijving": nationaliteit.reden_opname_nationaliteit,
                },
                "inOnderzoek": {
                    "aanduidingBijzonderNederlanderschap": bool(
                        nationaliteit.aanduiding_bijzonder_nederlanderschap
                    ),
                    "nationaliteit": bool(nationaliteit.nationaliteit),
                    "redenOpname": bool(nationaliteit.reden_opname_nationaliteit),
                    "datumIngangOnderzoek": {
                        "dag": int(
                            nationaliteit.datum_ingang_onderzoek[
                                settings.DAY_START : settings.DAY_END
                            ]
                        )
                        if is_valid_date_format(nationaliteit.datum_ingang_onderzoek)
                        else 0,
                        "datum": nationaliteit.datum_ingang_onderzoek,
                        "jaar": int(
                            nationaliteit.datum_ingang_onderzoek[
                                settings.YEAR_START : settings.YEAR_END
                            ]
                        )
                        if is_valid_date_format(nationaliteit.datum_ingang_onderzoek)
                        else 0,
                        "maand": int(
                            nationaliteit.datum_ingang_onderzoek[
                                settings.MONTH_START : settings.MONTH_END
                            ]
                        )
                        if is_valid_date_format(nationaliteit.datum_ingang_onderzoek)
                        else 0,
                    },
                },
            }
        )

    ingeschreven_persoon_dict["reisdocumenten"] = []

    reisdocumenten = persoon.reisdocument_set.all()

    for reisdocument in reisdocumenten:
        ingeschreven_persoon_dict["reisdocumenten"].append(
            reisdocument.nummer_nederlands_reisdocument
        )

    return ingeschreven_persoon_dict
