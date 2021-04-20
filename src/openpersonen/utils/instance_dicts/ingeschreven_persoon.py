from django.conf import settings

from openpersonen.features import (
    get_aanhef,
    get_aanschrijfwijze,
    get_gebruik_in_lopende_tekst,
)
from openpersonen.features.country_code_and_omschrijving.models import (
    CountryCodeAndOmschrijving,
)
from openpersonen.features.gemeente_code_and_omschrijving.models import (
    GemeenteCodeAndOmschrijving,
)
from openpersonen.features.reden_code_and_omschrijving.models import (
    RedenCodeAndOmschrijving,
)
from openpersonen.utils.converters import convert_xml_to_dict
from openpersonen.utils.helpers import calculate_age, convert_empty_instances

from .kind import get_kind_instance_dict
from .ouder import get_ouder_instance_dict
from .partner import get_partner_instance_dict


def _get_partner_info(partner_info):
    return (
        partner_info["gerelateerde"].get("adellijkeTitelPredikaat"),
        partner_info["gerelateerde"].get("voorvoegselGeslachtsnaam"),
        partner_info["gerelateerde"].get("geslachtsnaam"),
        partner_info.get("datumSluiting"),
    )


def get_persoon_instance_dict(instance_xml_dict):
    ingeschreven_persoon_dict = {
        "burgerservicenummer": instance_xml_dict.get("inp.bsn", "string"),
        "geheimhoudingPersoonsgegevens": instance_xml_dict.get(
            "inp.indicatieGeheim", "string"
        ),
        "naam": {
            "geslachtsnaam": instance_xml_dict.get("geslachtsnaam", "string"),
            "voorletters": instance_xml_dict.get("voorletters", "string"),
            "voornamen": instance_xml_dict.get("voornamen", "string"),
            "voorvoegsel": instance_xml_dict.get("voorvoegselGeslachtsnaam", "string"),
            "inOnderzoek": {
                "geslachtsnaam": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "voornamen": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "voorvoegsel": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "datumIngangOnderzoek": {
                    "dag": 1,
                    "datum": "01-01-1900",
                    "jaar": 1900,
                    "maand": 1,
                },
            },
            "aanduidingNaamgebruik": instance_xml_dict.get(
                "aanduidingNaamgebruik", "string"
            ),
        },
        "geboorte": {
            "datum": {
                "dag": int(
                    instance_xml_dict.get("geboortedatum", "19000101")[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                ),
                "datum": instance_xml_dict.get("geboortedatum", "string")
                if not isinstance(
                    instance_xml_dict.get("geboortedatum"), dict
                )
                else 1,
                "jaar": int(
                    instance_xml_dict.get("geboortedatum", "19000101")[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                )
                if not isinstance(
                    instance_xml_dict.get("geboortedatum"), dict
                )
                else 1900,
                "maand": int(
                    instance_xml_dict.get("geboortedatum", "19000101")[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                )
                if not isinstance(
                    instance_xml_dict.get("geboortedatum"), dict
                )
                else 1,
            },
            "land": {
                "code": instance_xml_dict.get("inp.geboorteLand", "string"),
                "omschrijving": CountryCodeAndOmschrijving.get_omschrijving_from_code(
                    instance_xml_dict.get("inp.geboorteLand", 0)
                ),
            },
            "plaats": {
                "code": GemeenteCodeAndOmschrijving.get_code_from_omschrijving(instance_xml_dict.get("inp.geboorteplaats", 0)),
                "omschrijving": instance_xml_dict.get("inp.geboorteplaats", "string"),
            },
            "inOnderzoek": {
                "datum": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "land": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "plaats": any(
                    [
                        "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "datumIngangOnderzoek": {
                    "dag": 1,
                    "datum": "01-01-1900",
                    "jaar": 1900,
                    "maand": 1,
                },
            },
        },
        "geslachtsaanduiding": instance_xml_dict.get("geslachtsaanduiding", "string"),
        "leeftijd": calculate_age(instance_xml_dict.get("geboortedatum", "string")),
        "datumEersteInschrijvingGBA": {
            "dag": int(
                instance_xml_dict.get("inp.datumInschrijving", "19000101")[
                    settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                ]
            ),
            "datum": instance_xml_dict.get("inp.datumInschrijving", "19000101")
            if not isinstance(
                instance_xml_dict.get("datumInschrijving"), dict
            )
            else 1,
            "jaar": int(
                instance_xml_dict.get("inp.datumInschrijving", "string")[
                    settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                ]
            )
            if not isinstance(
                instance_xml_dict.get("datumInschrijving"), dict
            )
            else 1900,
            "maand": int(
                instance_xml_dict.get("inp.datumInschrijving", "19000101")[
                    settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                ]
            )
            if not isinstance(
                instance_xml_dict.get("datumInschrijving"), dict
            )
            else 1,
        },
        "kiesrecht": {
            "europeesKiesrecht": instance_xml_dict.get(
                "ing.aanduidingEuropeesKiesrecht"
            )
            == "2",
            "uitgeslotenVanKiesrecht": instance_xml_dict.get(
                "ing.aanduidingUitgeslotenKiesrecht"
            )
            == "A",
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
        "inOnderzoek": {
            "burgerservicenummer": any(
                [
                    "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                    for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                    if isinstance(in_onderzoek, dict)
                ]
            ),
            "geslachtsaanduiding": any(
                [
                    "Persoonsgegevens" == in_onderzoek.get("groepsnaam")
                    for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                    if isinstance(in_onderzoek, dict)
                ]
            ),
            "datumIngangOnderzoek": {
                "dag": 1,
                "datum": "01-01-1900",
                "jaar": 1900,
                "maand": 1,
            },
        },
        "nationaliteit": [
            {
                "aanduidingBijzonderNederlanderschap": instance_xml_dict.get(
                    "inp.aanduidingBijzonderNederlanderschap", "string"
                ),
                "datumIngangGeldigheid": {
                    "dag": int(
                        instance_xml_dict.get("inp.heeftAlsNationaliteit", {}).get(
                            "inp.datumVerkrijging", "19000101"
                        )[
                            settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                        ]
                    ),
                    "datum": instance_xml_dict.get("inp.heeftAlsNationaliteit", {}).get(
                        "inp.datumVerkrijging", "19000101"
                    )
                    if not isinstance(
                        instance_xml_dict.get(
                            "inp.heeftAlsNationaliteit", {}
                        ).get("inp.datumVerkrijging"),
                        dict,
                    )
                    else 1,
                    "jaar": int(
                        instance_xml_dict.get("inp.heeftAlsNationaliteit", {}).get(
                            "inp.datumVerkrijging", "19000101"
                        )[
                            settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                        ]
                    )
                    if not isinstance(
                        instance_xml_dict.get(
                            "inp.heeftAlsNationaliteit", {}
                        ).get("inp.datumVerkrijging"),
                        dict,
                    )
                    else 1900,
                    "maand": int(
                        instance_xml_dict.get("inp.heeftAlsNationaliteit", {}).get(
                            "inp.datumVerkrijging", "19000101"
                        )[
                            settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                        ]
                    )
                    if not isinstance(
                        instance_xml_dict.get(
                            "inp.heeftAlsNationaliteit", {}
                        ).get("inp.datumVerkrijging"),
                        dict,
                    )
                    else 1,
                },
                "nationaliteit": {
                    "code": instance_xml_dict.get("inp.heeftAlsNationaliteit", {})
                    .get("gerelateerde", {})
                    .get("code"),
                    "omschrijving": instance_xml_dict.get(
                        "inp.heeftAlsNationaliteit", {}
                    )
                    .get("gerelateerde", {})
                    .get("omschrijving"),
                },
                "redenOpname": {
                    "code": instance_xml_dict.get("inp.heeftAlsNationaliteit", {}).get(
                        "inp.redenVerkrijging", "."
                    ),
                    "omschrijving": RedenCodeAndOmschrijving.get_omschrijving_from_code(
                        instance_xml_dict.get("inp.heeftAlsNationaliteit", {}).get(
                            "inp.redenVerkrijging", 0
                        )
                    ),
                },
                "inOnderzoek": {
                    "aanduidingBijzonderNederlanderschap": any(
                        [
                            "aanduidingBijzonderNederlanderschap"
                            == in_onderzoek.get("elementnaam")
                            for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        ]
                    ),
                    "nationaliteit": any(
                        [
                            "Nationaliteit" == in_onderzoek.get("groepsnaam")
                            for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                            if isinstance(in_onderzoek, dict)
                        ]
                    ),
                    "redenOpname": True,
                    "datumIngangOnderzoek": {
                        "dag": 1,
                        "datum": "01-01-1900",
                        "jaar": 1900,
                        "maand": 1,
                    },
                },
            }
        ],
        "opschortingBijhouding": {
            "reden": instance_xml_dict.get("inp.redenOpschortingBijhouding", "string"),
            "datum": {
                "dag": int(
                    instance_xml_dict.get("inp.datumOpschortingBijhouding", "19000101")[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                )                if not isinstance(
                    instance_xml_dict.get("inp.datumOpschortingBijhouding"), dict
                )
                else 1,
                "datum": instance_xml_dict.get(
                    "inp.datumOpschortingBijhouding", "19000101"
                ),
                "jaar": int(
                    instance_xml_dict.get("inp.datumOpschortingBijhouding", "19000101")[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                )                if not isinstance(
                    instance_xml_dict.get("inp.datumOpschortingBijhouding"), dict
                )
                else 1900,
                "maand": int(
                    instance_xml_dict.get("inp.datumOpschortingBijhouding", "19000101")[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                )
                if not isinstance(
                    instance_xml_dict.get("inp.datumOpschortingBijhouding"), dict
                )
                else 1,
            },
        },
        "overlijden": {
            "indicatieOverleden": instance_xml_dict.get(
                "inp.redenOpschortingBijhouding"
            )
            == "O",
            "datum": {
                "dag": int(
                    instance_xml_dict.get("overlijdensdatum", "19000101")[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                    if not isinstance(instance_xml_dict.get("overlijdensdatum"), dict)
                    else 0
                ),
                "datum": instance_xml_dict.get("overlijdensdatum", "19000101")
                if not isinstance(instance_xml_dict.get("overlijdensdatum"), dict)
                else "19000101",
                "jaar": int(
                    instance_xml_dict.get("overlijdensdatum", "19000101")[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                    if not isinstance(instance_xml_dict.get("overlijdensdatum"), dict)
                    else 1900
                ),
                "maand": int(
                    instance_xml_dict.get("overlijdensdatum", "19000101")[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                    if not isinstance(instance_xml_dict.get("overlijdensdatum"), dict)
                    else 1
                ),
            },
            "land": {
                "code": instance_xml_dict.get("inp.overlijdenLand", "string")
                if not isinstance(instance_xml_dict.get("overlijdensdatum"), dict)
                else "string",
                "omschrijving": CountryCodeAndOmschrijving.get_omschrijving_from_code(
                    instance_xml_dict.get("inp.overlijdenLand", 0)
                )
                if not isinstance(instance_xml_dict.get("overlijdensdatum"), dict)
                else "string",
            },
            "plaats": {
                "code": instance_xml_dict.get("inp.overlijdenplaats", "string")
                if not isinstance(instance_xml_dict.get("inp.overlijdenplaats"), dict)
                else "string",
                "omschrijving": GemeenteCodeAndOmschrijving.get_omschrijving_from_code(
                    instance_xml_dict.get("inp.overlijdenplaats", 0)
                )
                if not isinstance(instance_xml_dict.get("inp.overlijdenplaats"), dict)
                else "string",
            },
            "inOnderzoek": {
                "datum": any(
                    [
                        "Overlijden" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "land": any(
                    [
                        "Overlijden" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "plaats": any(
                    [
                        "Overlijden" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "datumIngangOnderzoek": {
                    "dag": 1,
                    "datum": "01-01-1900",
                    "jaar": 1900,
                    "maand": 1,
                },
            },
        },
        "verblijfplaats": {
            "functieAdres": "woonadres",
            "huisletter": instance_xml_dict.get("verblijfsadres", {}).get(
                "aoa.huisletter", "string"
            ),
            "huisnummer": instance_xml_dict.get("verblijfsadres", {}).get(
                "aoa.huisnummer", "string"
            ),
            "huisnummertoevoeging": instance_xml_dict.get("verblijfsadres", {}).get(
                "aoa.huisnummertoevoeging", "string"
            ),
            "aanduidingBijHuisnummer": None,
            "identificatiecodeNummeraanduiding": instance_xml_dict.get(
                "verblijfsadres", {}
            ).get("aoa.identificatie", "string"),
            "naamOpenbareRuimte": instance_xml_dict.get("verblijfsadres", {}).get(
                "gor.openbareRuimteNaam", "string"
            ),
            "postcode": instance_xml_dict.get("verblijfsadres", {}).get(
                "aoa.postcode", "string"
            ),
            "woonplaatsnaam": instance_xml_dict.get("verblijfsadres", {}).get(
                "wpl.woonplaatsNaam", "string"
            ),
            "identificatiecodeAdresseerbaarObject": instance_xml_dict.get(
                "verblijfsadres", {}
            ).get("wpl.identificatie", "string"),
            "indicatieVestigingVanuitBuitenland": True,
            "locatiebeschrijving": instance_xml_dict.get("verblijfsadres", {}).get(
                "inp.locatiebeschrijving", "string"
            ),
            "straatnaam": instance_xml_dict.get("verblijfsadres", {}).get(
                "gor.straatnaam", "string"
            ),
            "vanuitVertrokkenOnbekendWaarheen": True,
            "datumAanvangAdreshouding": {
                "dag": int(
                    instance_xml_dict.get("verblijfsadres", {}).get(
                        "begindatumVerblijf", "19000101"
                    )[settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END]
                ),
                "datum": instance_xml_dict.get("verblijfsadres", {}).get(
                    "begindatumVerblijf", "19000101"
                )                if not isinstance(
                    instance_xml_dict.get("verblijfsadres", {}).get("begindatumVerblijf"), dict
                )
                else 1,
                "jaar": int(
                    instance_xml_dict.get("verblijfsadres", {}).get(
                        "begindatumVerblijf", "19000101"
                    )[settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END]
                )
                if not isinstance(
                    instance_xml_dict.get("verblijfsadres"), dict
                )
                else 1900,
                "maand": int(
                    instance_xml_dict.get("verblijfsadres", {}).get(
                        "begindatumVerblijf", "19000101"
                    )[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                )
                if not isinstance(
                    instance_xml_dict.get("verblijfsadres"), dict
                )
                else 1,
            },
            "datumIngangGeldigheid": {
                "dag": int(
                    instance_xml_dict.get("inp.verblijftIn", {})
                    .get("gerelateerde", {})
                    .get("ingangsdatumObject", "19000101")[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                )                if not isinstance(
                    instance_xml_dict.get("inp.verblijftIn", {})
                    .get("gerelateerde", {})
                    .get("ingangsdatumObject"),
                    dict,
                )
                else 1,
                "datum": instance_xml_dict.get("inp.verblijftIn", {})
                .get("gerelateerde", {})
                .get("ingangsdatumObject", "19000101"),
                "jaar": int(
                    instance_xml_dict.get("inp.verblijftIn", {})
                    .get("gerelateerde", {})
                    .get("ingangsdatumObject", "19000101")[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                )
                if not isinstance(
                    instance_xml_dict.get("inp.verblijftIn", {})
                    .get("gerelateerde", {})
                    .get("ingangsdatumObject"),
                    dict,
                )
                else 1900,
                "maand": int(
                    instance_xml_dict.get("inp.verblijftIn", {})
                    .get("gerelateerde", {})
                    .get("ingangsdatumObject", "19000101")[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                )
                if not isinstance(
                    instance_xml_dict.get("inp.verblijftIn", {})
                    .get("gerelateerde", {})
                    .get("ingangsdatumObject"),
                    dict,
                )
                else 1,
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
            "gemeenteVanInschrijving": {
                "code": instance_xml_dict.get("inp.verblijftIn", {})
                .get("gerelateerde", {})
                .get("gemeenteCode"),
                "omschrijving": instance_xml_dict.get("inp.verblijftIn", {})
                .get("gerelateerde", {})
                .get("gemeenteNaam"),
            },
            "landVanwaarIngeschreven": {"code": "", "omschrijving": ""},
            "verblijfBuitenland": {
                "adresRegel1": instance_xml_dict.get("sub.verblijfBuitenland", {}).get(
                    "sub.adresBuitenland1"
                ),
                "adresRegel2": instance_xml_dict.get("sub.verblijfBuitenland", {}).get(
                    "sub.adresBuitenland2"
                ),
                "adresRegel3": instance_xml_dict.get("sub.verblijfBuitenland", {}).get(
                    "sub.adresBuitenland3"
                ),
                "vertrokkenOnbekendWaarheen": True,
                "land": {
                    "code": instance_xml_dict.get("sub.verblijfBuitenland", {}).get(
                        "lnd.landcode"
                    ),
                    "omschrijving": CountryCodeAndOmschrijving.get_omschrijving_from_code(
                        instance_xml_dict.get("sub.verblijfBuitenland", {}).get(
                            "lnd.landcode", 0
                        )
                    ),
                },
            },
            "inOnderzoek": {
                "aanduidingBijHuisnummer": True,
                "datumAanvangAdreshouding": True,
                "datumIngangGeldigheid": True,
                "datumInschrijvingInGemeente": True,
                "datumVestigingInNederland": True,
                "functieAdres": True,
                "gemeenteVanInschrijving": True,
                "huisletter": any(
                    [
                        "Verblijfplaats" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "huisnummer": any(
                    [
                        "Verblijfplaats" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "huisnummertoevoeging": any(
                    [
                        "Verblijfplaats" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "identificatiecodeNummeraanduiding": any(
                    [
                        "Verblijfplaats" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "identificatiecodeAdresseerbaarObject": any(
                    [
                        "Verblijfplaats" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "landVanwaarIngeschreven": any(
                    [
                        "Verblijfplaats" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "locatiebeschrijving": any(
                    [
                        "Verblijfplaats" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "naamOpenbareRuimte": any(
                    [
                        "Verblijfplaats" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "postcode": any(
                    [
                        "Verblijfplaats" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "straatnaam": any(
                    [
                        "Verblijfplaats" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "verblijfBuitenland": any(
                    [
                        "Verblijfplaats" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "woonplaatsnaam": any(
                    [
                        "Verblijfplaats" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "datumIngangOnderzoek": {
                    "dag": 1,
                    "datum": "01-01-1900",
                    "jaar": 1900,
                    "maand": 1,
                },
            },
        },
        "gezagsverhouding": {
            "indicatieCurateleRegister": instance_xml_dict.get(
                "ing.indicatieCurateleRegister", False
            ),
            "indicatieGezagMinderjarige": instance_xml_dict.get(
                "ing.indicatieGezagMinderjarige", False
            ),
            "inOnderzoek": {
                "indicatieCurateleRegister": any(
                    [
                        "Gezagsverhouding" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "indicatieGezagMinderjarige": any(
                    [
                        "Gezagsverhouding" == in_onderzoek.get("groepsnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                        if isinstance(in_onderzoek, dict)
                    ]
                ),
                "datumIngangOnderzoek": {
                    "dag": any(
                        [
                            "Gezagsverhouding" == in_onderzoek.get("groepsnaam")
                            for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                            if isinstance(in_onderzoek, dict)
                        ]
                    ),
                    "datum": any(
                        [
                            "Gezagsverhouding" == in_onderzoek.get("groepsnaam")
                            for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                            if isinstance(in_onderzoek, dict)
                        ]
                    ),
                    "jaar": any(
                        [
                            "Gezagsverhouding" == in_onderzoek.get("groepsnaam")
                            for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                            if isinstance(in_onderzoek, dict)
                        ]
                    ),
                    "maand": any(
                        [
                            "Gezagsverhouding" == in_onderzoek.get("groepsnaam")
                            for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                            if isinstance(in_onderzoek, dict)
                        ]
                    ),
                },
            },
        },
        "verblijfstitel": {
            "aanduiding": {
                "code": instance_xml_dict.get("vbt.aanduidingVerblijfstitel"),
                "omschrijving": "string",
            },
            "datumEinde": {
                "dag": int(
                    instance_xml_dict.get("ing.datumVerliesVerblijfstitel", "19000101")[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                )                if not isinstance(
                    instance_xml_dict.get("ing.datumVerliesVerblijfstitel"),
                    dict,
                )
                else 1,
                "datum": instance_xml_dict.get(
                    "ing.datumVerliesVerblijfstitel", "19000101"
                ),
                "jaar": int(
                    instance_xml_dict.get("ing.datumVerliesVerblijfstitel", "19000101")[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                )                if not isinstance(
                    instance_xml_dict.get("ing.datumVerliesVerblijfstitel"),
                    dict,
                )
                else 1900,
                "maand": int(
                    instance_xml_dict.get("ing.datumVerliesVerblijfstitel", "19000101")[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                )
                if not isinstance(
                    instance_xml_dict.get("ing.datumVerliesVerblijfstitel"),
                    dict,
                )
                else 1,
            },
            "datumIngang": {
                "dag": int(
                    instance_xml_dict.get(
                        "ing.datumVerkrijgingVerblijfstitel", "19000101"
                    )[settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END]
                )
                if not isinstance(
                    instance_xml_dict.get(
                        "ing.datumVerkrijgingVerblijfstitel"
                    ),
                    dict,
                )
                else 1,
                "datum": instance_xml_dict.get(
                    "ing.datumVerkrijgingVerblijfstitel", "19000101"
                ),
                "jaar": int(
                    instance_xml_dict.get(
                        "ing.datumVerkrijgingVerblijfstitel", "19000101"
                    )[settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END]
                )
                if not isinstance(
                    instance_xml_dict.get(
                        "ing.datumVerkrijgingVerblijfstitel"
                    ),
                    dict,
                )
                else 1900,
                "maand": int(
                    instance_xml_dict.get(
                        "ing.datumVerkrijgingVerblijfstitel", "19000101"
                    )[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                )
                if not isinstance(
                    instance_xml_dict.get(
                        "ing.datumVerkrijgingVerblijfstitel"
                    ),
                    dict,
                )
                else 1,
            },
            "inOnderzoek": {
                "aanduiding": any(
                    [
                        "aanduidingVerblijfstitel" == in_onderzoek.get("elementnaam")
                        for in_onderzoek in instance_xml_dict.get("inOnderzoek", [])
                    ]
                ),
                "datumEinde": "01-01-1900",
                "datumIngang": "01-01-1900",
                "datumIngangOnderzoek": {
                    "dag": 1,
                    "datum": "01-01-1900",
                    "jaar": 1900,
                    "maand": 1,
                },
            },
        },
        "reisdocumenten": ["string"],
    }

    kinderen_info = instance_xml_dict["inp.heeftAlsKinderen"]
    ouders_info = instance_xml_dict["inp.heeftAlsOuders"]
    partners_info = instance_xml_dict["inp.heeftAlsEchtgenootPartner"]

    if not isinstance(kinderen_info, list):
        kinderen_info = [kinderen_info]

    if not isinstance(ouders_info, list):
        ouders_info = [ouders_info]

    if not isinstance(partners_info, list):
        partners_info = [partners_info]

    ingeschreven_persoon_dict["kinderen"] = []
    ingeschreven_persoon_dict["ouders"] = []
    ingeschreven_persoon_dict["partners"] = []

    for kind_info in kinderen_info:
        ingeschreven_persoon_dict["kinderen"].append(get_kind_instance_dict(kind_info))

    for ouder_info in ouders_info:
        ingeschreven_persoon_dict["ouders"].append(get_ouder_instance_dict(ouder_info))

    partners_title = None
    partners_last_name_prefix = None
    partners_last_name = None
    partners_date = None
    for partner_info in partners_info:
        ingeschreven_persoon_dict["partners"].append(
            get_partner_instance_dict(partner_info)
        )
        if (
            not partners_last_name
            or (
                partner_info.get("datumOntbinding")
                and partners_date
                and partners_date > partner_info["datumSluiting"]
            )
            or (
                partner_info.get("datumOntbinding") is None
                and partners_date
                and partners_date < partner_info["datumSluiting"]
            )
        ):
            (
                partners_title,
                partners_last_name_prefix,
                partners_last_name,
                partners_date,
            ) = _get_partner_info(partner_info)

    ingeschreven_persoon_dict["naam"]["aanhef"] = get_aanhef(
        instance_xml_dict.get("voorvoegselGeslachtsnaam"),
        instance_xml_dict.get("geslachtsnaam"),
        partners_last_name_prefix,
        partners_last_name,
        instance_xml_dict.get("aanduidingNaamgebruik"),
        instance_xml_dict.get("geslachtsaanduiding"),
        instance_xml_dict.get("adellijkeTitelPredikaat"),
        partners_title,
    )

    ingeschreven_persoon_dict["naam"]["aanschrijfwijze"] = get_aanschrijfwijze(
        instance_xml_dict.get("voorvoegselGeslachtsnaam"),
        instance_xml_dict.get("geslachtsnaam"),
        instance_xml_dict.get("voornamen"),
        partners_last_name_prefix,
        partners_last_name,
        instance_xml_dict.get("aanduidingNaamgebruik"),
        instance_xml_dict.get("geslachtsaanduiding"),
        instance_xml_dict.get("adellijkeTitelPredikaat"),
        partners_title,
    )

    ingeschreven_persoon_dict["naam"][
        "gebruikInLopendeTekst"
    ] = get_gebruik_in_lopende_tekst(
        instance_xml_dict.get("voorvoegselGeslachtsnaam"),
        instance_xml_dict.get("geslachtsnaam"),
        partners_last_name_prefix,
        partners_last_name,
        instance_xml_dict.get("aanduidingNaamgebruik"),
        instance_xml_dict.get("geslachtsaanduiding"),
        instance_xml_dict.get("adellijkeTitelPredikaat"),
        partners_title,
    )

    convert_empty_instances(ingeschreven_persoon_dict)

    return ingeschreven_persoon_dict


def convert_xml_to_persoon_dicts(xml):
    dict_object = convert_xml_to_dict(xml)

    antwoord_object = dict_object["Envelope"]["Body"]["npsLa01"]["antwoord"]["object"]

    if isinstance(antwoord_object, list):
        result = []
        for antwood_dict in antwoord_object:
            result_dict = get_persoon_instance_dict(antwood_dict)
            result.append(result_dict)
    else:
        result = [get_persoon_instance_dict(antwoord_object)]

    return result
