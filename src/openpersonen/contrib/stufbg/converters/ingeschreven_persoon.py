from django.conf import settings

import xmltodict

from openpersonen.contrib.utils import calculate_age, convert_empty_instances

from .kind import get_kind_instance_dict
from .ouder import get_ouder_instance_dict
from .partner import get_partner_instance_dict


def get_persoon_instance_dict(response, instance_xml_dict, prefix):
    ingeschreven_persoon_dict = {
        "burgerservicenummer": instance_xml_dict.get(f"{prefix}:inp.bsn", "string"),
        "geheimhoudingPersoonsgegevens": instance_xml_dict.get(
            f"{prefix}:inp.indicatieGeheim", "string"
        ),
        "naam": {
            "geslachtsnaam": instance_xml_dict.get(f"{prefix}:geslachtsnaam", "string"),
            "voorletters": instance_xml_dict.get(f"{prefix}:voorletters", "string"),
            "voornamen": instance_xml_dict.get(f"{prefix}:voornamen", "string"),
            "voorvoegsel": instance_xml_dict.get(
                f"{prefix}:voorvoegselGeslachtsnaam", "string"
            ),
            "inOnderzoek": {
                "geslachtsnaam": instance_xml_dict.get(f"{prefix}:inOnderzoek", {}).get(
                    "groepsnaam"
                )
                == "Persoonsgegevens",
                "voornamen": instance_xml_dict.get(f"{prefix}:inOnderzoek", {}).get(
                    "groepsnaam"
                )
                == "Persoonsgegevens",
                "voorvoegsel": instance_xml_dict.get(f"{prefix}:inOnderzoek", {}).get(
                    "groepsnaam"
                )
                == "Persoonsgegevens",
                "datumIngangOnderzoek": {
                    "dag": 1,
                    "datum": "01-01-1900",
                    "jaar": 1900,
                    "maand": 1,
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
                    instance_xml_dict.get(f"{prefix}:geboortedatum", "19000101")[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                ),
                "datum": instance_xml_dict.get(f"{prefix}:geboortedatum", "string"),
                "jaar": int(
                    instance_xml_dict.get(f"{prefix}:geboortedatum", "19000101")[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                ),
                "maand": int(
                    instance_xml_dict.get(f"{prefix}:geboortedatum", "19000101")[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                ),
            },
            "land": {
                "code": instance_xml_dict.get(f"{prefix}:inp.geboorteLand", "string"),
                "omschrijving": instance_xml_dict.get(
                    f"{prefix}:inp.geboorteLand", "string"
                ),
            },
            "plaats": {
                "code": instance_xml_dict.get(f"{prefix}:inp.geboorteplaats", "string"),
                "omschrijving": instance_xml_dict.get(
                    f"{prefix}:inp.geboorteplaats", "string"
                ),
            },
            "inOnderzoek": {
                "datum": instance_xml_dict.get(f"{prefix}:inOnderzoek", {}).get(
                    "groepsnaam"
                )
                == "Persoonsgegevens",
                "land": instance_xml_dict.get(f"{prefix}:inOnderzoek", {}).get(
                    "groepsnaam"
                )
                == "Persoonsgegevens",
                "plaats": instance_xml_dict.get(f"{prefix}:inOnderzoek", {}).get(
                    "groepsnaam"
                )
                == "Persoonsgegevens",
                "datumIngangOnderzoek": {
                    "dag": 1,
                    "datum": "01-01-1900",
                    "jaar": 1900,
                    "maand": 1,
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
                instance_xml_dict.get(f"{prefix}:inp.datumInschrijving", "19000101")[
                    settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                ]
            ),
            "datum": instance_xml_dict.get(
                f"{prefix}:inp.datumInschrijving", "19000101"
            ),
            "jaar": int(
                instance_xml_dict.get(f"{prefix}:inp.datumInschrijving", "string")[
                    settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                ]
            ),
            "maand": int(
                instance_xml_dict.get(f"{prefix}:inp.datumInschrijving", "19000101")[
                    settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                ]
            ),
        },
        "kiesrecht": {
            "europeesKiesrecht": instance_xml_dict.get(
                f"{prefix}:ing.aanduidingEuropeesKiesrecht"
            )
            == "2",
            "uitgeslotenVanKiesrecht": instance_xml_dict.get(
                f"{prefix}:ing.aanduidingUitgeslotenKiesrecht"
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
            "burgerservicenummer": instance_xml_dict.get(
                f"{prefix}:inOnderzoek", {}
            ).get("groepsnaam")
            == "Persoonsgegevens",
            "geslachtsaanduiding": instance_xml_dict.get(
                f"{prefix}:inOnderzoek", {}
            ).get("groepsnaam")
            == "Persoonsgegevens",
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
                    f"{prefix}:inp.aanduidingBijzonderNederlanderschap", "string"
                ),
                "datumIngangGeldigheid": {
                    "dag": int(
                        instance_xml_dict.get(
                            f"{prefix}:inp.heeftAlsNationaliteit", {}
                        ).get("inp.datumVerkrijging", "19000101")[
                            settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                        ]
                    ),
                    "datum": instance_xml_dict.get(
                        f"{prefix}:inp.heeftAlsNationaliteit", {}
                    ).get("inp.datumVerkrijging", "19000101"),
                    "jaar": int(
                        instance_xml_dict.get(
                            f"{prefix}:inp.heeftAlsNationaliteit", {}
                        ).get("inp.datumVerkrijging", "19000101")[
                            settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                        ]
                    ),
                    "maand": int(
                        instance_xml_dict.get(
                            f"{prefix}:inp.heeftAlsNationaliteit", {}
                        ).get("inp.datumVerkrijging", "19000101")[
                            settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                        ]
                    ),
                },
                "nationaliteit": {
                    "code": instance_xml_dict.get(
                        f"{prefix}:inp.heeftAlsNationaliteit", {}
                    )
                    .get("gerelateerde", {})
                    .get("code"),
                    "omschrijving": instance_xml_dict.get(
                        f"{prefix}:inp.heeftAlsNationaliteit", {}
                    )
                    .get("gerelateerde", {})
                    .get("omschrijving"),
                },
                "redenOpname": {
                    "code": instance_xml_dict.get(
                        f"{prefix}:inp.heeftAlsNationaliteit", {}
                    ).get("inp.redenVerkrijging"),
                    "omschrijving": instance_xml_dict.get(
                        f"{prefix}:inp.heeftAlsNationaliteit", {}
                    ).get("inp.redenVerkrijging"),
                },
                "inOnderzoek": {
                    "aanduidingBijzonderNederlanderschap": instance_xml_dict.get(
                        f"{prefix}:inOnderzoek", {}
                    ).get("elementnaam")
                    == "aanduidingBijzonderNederlanderschap",
                    "nationaliteit": instance_xml_dict.get(
                        f"{prefix}:inOnderzoek", {}
                    ).get("groepsnaam")
                    == "Nationaliteit",
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
            "reden": instance_xml_dict.get(
                f"{prefix}:inp.redenOpschortingBijhouding", "string"
            ),
            "datum": {
                "dag": int(
                    instance_xml_dict.get(
                        f"{prefix}:inp.datumOpschortingBijhouding", "19000101"
                    )[settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END]
                ),
                "datum": instance_xml_dict.get(
                    f"{prefix}:inp.datumOpschortingBijhouding", "19000101"
                ),
                "jaar": int(
                    instance_xml_dict.get(
                        f"{prefix}:inp.datumOpschortingBijhouding", "19000101"
                    )[settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END]
                ),
                "maand": int(
                    instance_xml_dict.get(
                        f"{prefix}:inp.datumOpschortingBijhouding", "19000101"
                    )[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                ),
            },
        },
        "overlijden": {
            "indicatieOverleden": instance_xml_dict.get(
                f"{prefix}:inp.redenOpschortingBijhouding"
            )
            == "O",
            "datum": {
                "dag": int(
                    instance_xml_dict.get(f"{prefix}:overlijdensdatum", "19000101")[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                    if not isinstance(
                        instance_xml_dict.get(f"{prefix}:overlijdensdatum"), dict
                    )
                    else 0
                ),
                "datum": instance_xml_dict.get(f"{prefix}:overlijdensdatum", "19000101")
                if not isinstance(
                    instance_xml_dict.get(f"{prefix}:overlijdensdatum"), dict
                )
                else "19000101",
                "jaar": int(
                    instance_xml_dict.get(f"{prefix}:overlijdensdatum", "19000101")[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                    if not isinstance(
                        instance_xml_dict.get(f"{prefix}:overlijdensdatum"), dict
                    )
                    else 1900
                ),
                "maand": int(
                    instance_xml_dict.get(f"{prefix}:overlijdensdatum", "19000101")[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                    if not isinstance(
                        instance_xml_dict.get(f"{prefix}:overlijdensdatum"), dict
                    )
                    else 1
                ),
            },
            "land": {
                "code": instance_xml_dict.get(f"{prefix}:inp.overlijdenLand", "string")
                if not isinstance(
                    instance_xml_dict.get(f"{prefix}:overlijdensdatum"), dict
                )
                else "string",
                "omschrijving": instance_xml_dict.get(
                    f"{prefix}:inp.overlijdenLand", "string"
                )
                if not isinstance(
                    instance_xml_dict.get(f"{prefix}:overlijdensdatum"), dict
                )
                else "string",
            },
            "plaats": {
                "code": instance_xml_dict.get(
                    f"{prefix}:inp.overlijdenplaats", "string"
                )
                if not isinstance(
                    instance_xml_dict.get(f"{prefix}:inp.overlijdenplaats"), dict
                )
                else "string",
                "omschrijving": instance_xml_dict.get(
                    f"{prefix}:inp.overlijdenplaats", "string"
                )
                if not isinstance(
                    instance_xml_dict.get(f"{prefix}:inp.overlijdenplaats"), dict
                )
                else "string",
            },
            "inOnderzoek": {
                "datum": instance_xml_dict.get(f"{prefix}:inOnderzoek", {}).get(
                    "groepsnaam"
                )
                == "Overlijden",
                "land": instance_xml_dict.get(f"{prefix}:inOnderzoek", {}).get(
                    "groepsnaam"
                )
                == "Overlijden",
                "plaats": instance_xml_dict.get(f"{prefix}:inOnderzoek", {}).get(
                    "groepsnaam"
                )
                == "Overlijden",
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
            "huisletter": instance_xml_dict.get(f"{prefix}:verblijfsadres", {}).get(
                f"{prefix}:aoa.huisletter", "string"
            ),
            "huisnummer": instance_xml_dict.get(f"{prefix}:verblijfsadres", {}).get(
                f"{prefix}:aoa.huisnummer", "string"
            ),
            "huisnummertoevoeging": instance_xml_dict.get(
                f"{prefix}:verblijfsadres", {}
            ).get(f"{prefix}:aoa.huisnummertoevoeging", "string"),
            "aanduidingBijHuisnummer": None,
            "identificatiecodeNummeraanduiding": instance_xml_dict.get(
                f"{prefix}:verblijfsadres", {}
            ).get(f"{prefix}:aoa.identificatie", "string"),
            "naamOpenbareRuimte": instance_xml_dict.get(
                f"{prefix}:verblijfsadres", {}
            ).get(f"{prefix}:gor.openbareRuimteNaam", "string"),
            "postcode": instance_xml_dict.get(f"{prefix}:verblijfsadres", {}).get(
                f"{prefix}:aoa.postcode", "string"
            ),
            "woonplaatsnaam": instance_xml_dict.get(f"{prefix}:verblijfsadres", {}).get(
                f"{prefix}:wpl.woonplaatsNaam", "string"
            ),
            "identificatiecodeAdresseerbaarObject": instance_xml_dict.get(
                f"{prefix}:verblijfsadres", {}
            ).get(f"{prefix}:wpl.identificatie", "string"),
            "indicatieVestigingVanuitBuitenland": True,
            "locatiebeschrijving": instance_xml_dict.get(
                f"{prefix}:verblijfsadres", {}
            ).get(f"{prefix}:inp.locatiebeschrijving", "string"),
            "straatnaam": instance_xml_dict.get(f"{prefix}:verblijfsadres", {}).get(
                f"{prefix}:gor.straatnaam", "string"
            ),
            "vanuitVertrokkenOnbekendWaarheen": True,
            "datumAanvangAdreshouding": {
                "dag": int(
                    instance_xml_dict.get(f"{prefix}:verblijfsadres", {}).get(
                        "begindatumVerblijf", "19000101"
                    )[settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END]
                ),
                "datum": instance_xml_dict.get(f"{prefix}:verblijfsadres", {}).get(
                    "begindatumVerblijf", "19000101"
                ),
                "jaar": int(
                    instance_xml_dict.get(f"{prefix}:verblijfsadres", {}).get(
                        "begindatumVerblijf", "19000101"
                    )[settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END]
                ),
                "maand": int(
                    instance_xml_dict.get(f"{prefix}:verblijfsadres", {}).get(
                        "begindatumVerblijf", "19000101"
                    )[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                ),
            },
            "datumIngangGeldigheid": {
                "dag": int(
                    instance_xml_dict.get(f"{prefix}:inp.verblijftIn", {})
                    .get("gerelateerde", {})
                    .get("ingangsdatumObject", "19000101")[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                ),
                "datum": instance_xml_dict.get(f"{prefix}:inp.verblijftIn", {})
                .get("gerelateerde", {})
                .get("ingangsdatumObject", "19000101"),
                "jaar": int(
                    instance_xml_dict.get(f"{prefix}:inp.verblijftIn", {})
                    .get("gerelateerde", {})
                    .get("ingangsdatumObject", "19000101")[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                ),
                "maand": int(
                    instance_xml_dict.get(f"{prefix}:inp.verblijftIn", {})
                    .get("gerelateerde", {})
                    .get("ingangsdatumObject", "19000101")[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                ),
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
                "code": instance_xml_dict.get(f"{prefix}:inp.verblijftIn", {})
                .get("gerelateerde", {})
                .get("gemeenteCode"),
                "omschrijving": instance_xml_dict.get(f"{prefix}:inp.verblijftIn", {})
                .get("gerelateerde", {})
                .get("gemeenteNaam"),
            },
            "landVanwaarIngeschreven": {"code": "", "omschrijving": ""},
            "verblijfBuitenland": {
                "adresRegel1": instance_xml_dict.get(
                    f"{prefix}:sub.verblijfBuitenland", {}
                ).get("sub.adresBuitenland1"),
                "adresRegel2": instance_xml_dict.get(
                    f"{prefix}:sub.verblijfBuitenland", {}
                ).get("sub.adresBuitenland2"),
                "adresRegel3": instance_xml_dict.get(
                    f"{prefix}:sub.verblijfBuitenland", {}
                ).get("sub.adresBuitenland3"),
                "vertrokkenOnbekendWaarheen": True,
                "land": {
                    "code": instance_xml_dict.get(
                        f"{prefix}:sub.verblijfBuitenland", {}
                    ).get("lnd.landcode"),
                    "omschrijving": instance_xml_dict.get(
                        f"{prefix}:sub.verblijfBuitenland", {}
                    ).get("lnd.landcode"),
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
                "huisletter": instance_xml_dict.get(f"{prefix}:inOnderzoek", {}).get(
                    "groepsnaam"
                )
                == "Verblijfplaats",
                "huisnummer": instance_xml_dict.get(f"{prefix}:inOnderzoek", {}).get(
                    "groepsnaam"
                )
                == "Verblijfplaats",
                "huisnummertoevoeging": instance_xml_dict.get(
                    f"{prefix}:inOnderzoek", {}
                ).get("groepsnaam")
                == "Verblijfplaats",
                "identificatiecodeNummeraanduiding": instance_xml_dict.get(
                    f"{prefix}:inOnderzoek", {}
                ).get("groepsnaam")
                == "Verblijfplaats",
                "identificatiecodeAdresseerbaarObject": instance_xml_dict.get(
                    f"{prefix}:inOnderzoek", {}
                ).get("groepsnaam")
                == "Verblijfplaats",
                "landVanwaarIngeschreven": instance_xml_dict.get(
                    f"{prefix}:inOnderzoek", {}
                ).get("groepsnaam")
                == "Verblijfplaats",
                "locatiebeschrijving": instance_xml_dict.get(
                    f"{prefix}:inOnderzoek", {}
                ).get("groepsnaam")
                == "Verblijfplaats",
                "naamOpenbareRuimte": instance_xml_dict.get(
                    f"{prefix}:inOnderzoek", {}
                ).get("groepsnaam")
                == "Verblijfplaats",
                "postcode": instance_xml_dict.get(f"{prefix}:inOnderzoek", {}).get(
                    "groepsnaam"
                )
                == "Verblijfplaats",
                "straatnaam": instance_xml_dict.get(f"{prefix}:inOnderzoek", {}).get(
                    "groepsnaam"
                )
                == "Verblijfplaats",
                "verblijfBuitenland": instance_xml_dict.get(
                    f"{prefix}:inOnderzoek", {}
                ).get("groepsnaam")
                == "Verblijfplaats",
                "woonplaatsnaam": instance_xml_dict.get(
                    f"{prefix}:inOnderzoek", {}
                ).get("groepsnaam")
                == "Verblijfplaats",
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
                f"{prefix}:ing.indicatieCurateleRegister", False
            ),
            "indicatieGezagMinderjarige": instance_xml_dict.get(
                f"{prefix}:ing.indicatieGezagMinderjarige", False
            ),
            "inOnderzoek": {
                "indicatieCurateleRegister": instance_xml_dict.get(
                    f"{prefix}:inOnderzoek", {}
                ).get("groepsnaam")
                == "Gezagsverhouding",
                "indicatieGezagMinderjarige": instance_xml_dict.get(
                    f"{prefix}:inOnderzoek", {}
                ).get("groepsnaam")
                == "Gezagsverhouding",
                "datumIngangOnderzoek": {
                    "dag": instance_xml_dict.get(f"{prefix}:inOnderzoek", {}).get(
                        "groepsnaam"
                    )
                    == "Gezagsverhouding",
                    "datum": instance_xml_dict.get(f"{prefix}:inOnderzoek", {}).get(
                        "groepsnaam"
                    )
                    == "Gezagsverhouding",
                    "jaar": instance_xml_dict.get(f"{prefix}:inOnderzoek", {}).get(
                        "groepsnaam"
                    )
                    == "Gezagsverhouding",
                    "maand": instance_xml_dict.get(f"{prefix}:inOnderzoek", {}).get(
                        "groepsnaam"
                    )
                    == "Gezagsverhouding",
                },
            },
        },
        "verblijfstitel": {
            "aanduiding": {
                "code": instance_xml_dict.get(f"{prefix}:vbt.aanduidingVerblijfstitel"),
                "omschrijving": "string",
            },
            "datumEinde": {
                "dag": int(
                    instance_xml_dict.get(
                        f"{prefix}:ing.datumVerliesVerblijfstitel", "19000101"
                    )[settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END]
                ),
                "datum": instance_xml_dict.get(
                    f"{prefix}:ing.datumVerliesVerblijfstitel", "19000101"
                ),
                "jaar": int(
                    instance_xml_dict.get(
                        f"{prefix}:ing.datumVerliesVerblijfstitel", "19000101"
                    )[settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END]
                ),
                "maand": int(
                    instance_xml_dict.get(
                        f"{prefix}:ing.datumVerliesVerblijfstitel", "19000101"
                    )[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                ),
            },
            "datumIngang": {
                "dag": int(
                    instance_xml_dict.get(
                        f"{prefix}:ing.datumVerkrijgingVerblijfstitel", "19000101"
                    )[settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END]
                ),
                "datum": instance_xml_dict.get(
                    f"{prefix}:ing.datumVerkrijgingVerblijfstitel", "19000101"
                ),
                "jaar": int(
                    instance_xml_dict.get(
                        f"{prefix}:ing.datumVerkrijgingVerblijfstitel", "19000101"
                    )[settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END]
                ),
                "maand": int(
                    instance_xml_dict.get(
                        f"{prefix}:ing.datumVerkrijgingVerblijfstitel", "19000101"
                    )[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                ),
            },
            "inOnderzoek": {
                "aanduiding": instance_xml_dict.get(f"{prefix}:inOnderzoek", {}).get(
                    "elementnaam"
                )
                == "aanduidingVerblijfstitel",
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

    kinderen_info = instance_xml_dict[f"{prefix}:inp.heeftAlsKinderen"]
    ouders_info = instance_xml_dict[f"{prefix}:inp.heeftAlsOuders"]
    partners_info = instance_xml_dict[f"{prefix}:inp.heeftAlsEchtgenootPartner"]

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
        ingeschreven_persoon_dict["kinderen"].append(
            get_kind_instance_dict(kind_info, prefix)
        )

    for ouder_info in ouders_info:
        ingeschreven_persoon_dict["ouders"].append(
            get_ouder_instance_dict(ouder_info, prefix)
        )

    for partner_info in partners_info:
        ingeschreven_persoon_dict["partners"].append(
            get_partner_instance_dict(partner_info, prefix)
        )

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
            result_dict = get_persoon_instance_dict(response, antwood_dict, prefix)
            result.append(result_dict)
    else:
        result = [get_persoon_instance_dict(response, antwoord_object, prefix)]

    return result
