from django.conf import settings

from openpersonen.contrib.utils import calculate_age, is_valid_date_format
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
from openpersonen.utils.helpers import calculate_age, is_valid_date_format

from .kind import convert_kind_instance_to_dict
from .ouder import convert_ouder_instance_to_dict
from .partner import convert_partner_instance_to_dict


def _get_partner_info(partner):
    return (
        partner.adellijke_titel_predikaat_echtgenoot_geregistreerd_partner,
        partner.voorvoegsel_geslachtsnaam_echtgenoot_geregistreerd_partner,
        partner.geslachtsnaam_echtgenoot_geregistreerd_partner,
        partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap,
    )


def convert_persoon_to_instance_dict(persoon):

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
                            settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                        ]
                    )
                    if is_valid_date_format(persoon.datum_ingang_onderzoek)
                    else 0,
                    "datum": persoon.datum_ingang_onderzoek,
                    "jaar": int(
                        persoon.datum_ingang_onderzoek[
                            settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                        ]
                    )
                    if is_valid_date_format(persoon.datum_ingang_onderzoek)
                    else 0,
                    "maand": int(
                        persoon.datum_ingang_onderzoek[
                            settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                        ]
                    )
                    if is_valid_date_format(persoon.datum_ingang_onderzoek)
                    else 0,
                },
            },
            "aanduidingNaamgebruik": persoon.aanduiding_naamgebruik,
        },
        "geboorte": {
            "datum": {
                "dag": int(
                    persoon.geboortedatum_persoon[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                )
                if is_valid_date_format(persoon.geboortedatum_persoon)
                else 0,
                "datum": persoon.geboortedatum_persoon,
                "jaar": int(
                    persoon.geboortedatum_persoon[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                )
                if is_valid_date_format(persoon.geboortedatum_persoon)
                else 0,
                "maand": int(
                    persoon.geboortedatum_persoon[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                )
                if is_valid_date_format(persoon.geboortedatum_persoon)
                else 0,
            },
            "land": {
                "code": persoon.geboorteland_persoon,
                "omschrijving": CountryCodeAndOmschrijving.get_omschrijving_from_code(
                    persoon.geboorteland_persoon
                ),
            },
            "plaats": {
                "code": persoon.geboorteplaats_persoon,
                "omschrijving": GemeenteCodeAndOmschrijving.get_omschrijving_from_code(
                    persoon.geboorteplaats_persoon
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
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                )
                if is_valid_date_format(
                    kiesrecht.einddatum_uitsluiting_europees_kiesrecht
                )
                else 0,
                "datum": kiesrecht.einddatum_uitsluiting_europees_kiesrecht,
                "jaar": int(
                    kiesrecht.einddatum_uitsluiting_europees_kiesrecht[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                )
                if is_valid_date_format(
                    kiesrecht.einddatum_uitsluiting_europees_kiesrecht
                )
                else 0,
                "maand": int(
                    kiesrecht.einddatum_uitsluiting_europees_kiesrecht[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
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
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                )
                if is_valid_date_format(kiesrecht.einddatum_uitsluiting_kiesrecht)
                else 0,
                "datum": kiesrecht.einddatum_uitsluiting_kiesrecht,
                "jaar": int(
                    kiesrecht.einddatum_uitsluiting_kiesrecht[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                )
                if is_valid_date_format(kiesrecht.einddatum_uitsluiting_kiesrecht)
                else 0,
                "maand": int(
                    kiesrecht.einddatum_uitsluiting_kiesrecht[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
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
                    overlijden.datum_overlijden[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                )
                if is_valid_date_format(overlijden.datum_overlijden)
                else 0,
                "datum": overlijden.datum_overlijden,
                "jaar": int(
                    overlijden.datum_overlijden[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                )
                if is_valid_date_format(overlijden.datum_overlijden)
                else 0,
                "maand": int(
                    overlijden.datum_overlijden[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                )
                if is_valid_date_format(overlijden.datum_overlijden)
                else 0,
            },
            "land": {
                "code": overlijden.land_overlijden,
                "omschrijving": CountryCodeAndOmschrijving.get_omschrijving_from_code(
                    overlijden.land_overlijden
                ),
            },
            "plaats": {
                "code": overlijden.plaats_overlijden,
                "omschrijving": GemeenteCodeAndOmschrijving.get_omschrijving_from_code(
                    overlijden.plaats_overlijden
                ),
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
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                )
                if is_valid_date_format(verblijfplaats.datum_aanvang_adres_buitenland)
                else 0,
                "datum": verblijfplaats.datum_aanvang_adres_buitenland,
                "jaar": int(
                    verblijfplaats.datum_aanvang_adres_buitenland[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                )
                if is_valid_date_format(verblijfplaats.datum_aanvang_adres_buitenland)
                else 0,
                "maand": int(
                    verblijfplaats.datum_aanvang_adres_buitenland[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                )
                if is_valid_date_format(verblijfplaats.datum_aanvang_adres_buitenland)
                else 0,
            },
            "datumIngangGeldigheid": {
                "dag": int(
                    verblijfplaats.ingangsdatum_geldigheid_met_betrekking[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                )
                if is_valid_date_format(
                    verblijfplaats.ingangsdatum_geldigheid_met_betrekking
                )
                else 0,
                "datum": verblijfplaats.ingangsdatum_geldigheid_met_betrekking,
                "jaar": int(
                    verblijfplaats.ingangsdatum_geldigheid_met_betrekking[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                )
                if is_valid_date_format(
                    verblijfplaats.ingangsdatum_geldigheid_met_betrekking
                )
                else 0,
                "maand": int(
                    verblijfplaats.ingangsdatum_geldigheid_met_betrekking[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
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
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                )
                if is_valid_date_format(
                    verblijfplaats.datum_inschrijving_in_de_gemeente
                )
                else 0,
                "datum": verblijfplaats.datum_inschrijving_in_de_gemeente,
                "jaar": int(
                    verblijfplaats.datum_inschrijving_in_de_gemeente[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                )
                if is_valid_date_format(
                    verblijfplaats.datum_inschrijving_in_de_gemeente
                )
                else 0,
                "maand": int(
                    verblijfplaats.datum_inschrijving_in_de_gemeente[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
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
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                )
                if is_valid_date_format(verblijfplaats.datum_vestiging_in_nederland)
                else 0,
                "datum": verblijfplaats.datum_vestiging_in_nederland,
                "jaar": int(
                    verblijfplaats.datum_vestiging_in_nederland[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                )
                if is_valid_date_format(verblijfplaats.datum_vestiging_in_nederland)
                else 0,
                "maand": int(
                    verblijfplaats.datum_vestiging_in_nederland[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
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
                            settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                        ]
                    )
                    if is_valid_date_format(verblijfplaats.datum_ingang_onderzoek)
                    else 0,
                    "datum": verblijfplaats.datum_ingang_onderzoek,
                    "jaar": int(
                        verblijfplaats.datum_ingang_onderzoek[
                            settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                        ]
                    )
                    if is_valid_date_format(verblijfplaats.datum_ingang_onderzoek)
                    else 0,
                    "maand": int(
                        verblijfplaats.datum_ingang_onderzoek[
                            settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
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
                            settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                        ]
                    )
                    if is_valid_date_format(gezagsverhouding.datum_ingang_onderzoek)
                    else 0,
                    "datum": gezagsverhouding.datum_ingang_onderzoek,
                    "jaar": int(
                        gezagsverhouding.datum_ingang_onderzoek[
                            settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                        ]
                    )
                    if is_valid_date_format(gezagsverhouding.datum_ingang_onderzoek)
                    else 0,
                    "maand": int(
                        gezagsverhouding.datum_ingang_onderzoek[
                            settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
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
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                )
                if is_valid_date_format(verblijfstitel.datum_einde_verblijfstitel)
                else 0,
                "datum": verblijfstitel.datum_einde_verblijfstitel,
                "jaar": int(
                    verblijfstitel.datum_einde_verblijfstitel[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                )
                if is_valid_date_format(verblijfstitel.datum_einde_verblijfstitel)
                else 0,
                "maand": int(
                    verblijfstitel.datum_einde_verblijfstitel[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                )
                if is_valid_date_format(verblijfstitel.datum_einde_verblijfstitel)
                else 0,
            },
            "datumIngang": {
                "dag": int(
                    verblijfstitel.ingangsdatum_verblijfstitel[
                        settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                    ]
                )
                if is_valid_date_format(verblijfstitel.ingangsdatum_verblijfstitel)
                else 0,
                "datum": verblijfstitel.ingangsdatum_verblijfstitel,
                "jaar": int(
                    verblijfstitel.ingangsdatum_verblijfstitel[
                        settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                    ]
                )
                if is_valid_date_format(verblijfstitel.ingangsdatum_verblijfstitel)
                else 0,
                "maand": int(
                    verblijfstitel.ingangsdatum_verblijfstitel[
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
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
                            settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                        ]
                    )
                    if is_valid_date_format(verblijfstitel.datum_ingang_onderzoek)
                    else 0,
                    "datum": verblijfstitel.datum_ingang_onderzoek,
                    "jaar": int(
                        verblijfstitel.datum_ingang_onderzoek[
                            settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                        ]
                    )
                    if is_valid_date_format(verblijfstitel.datum_ingang_onderzoek)
                    else 0,
                    "maand": int(
                        verblijfstitel.datum_ingang_onderzoek[
                            settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
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
                            settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                        ]
                    )
                    if is_valid_date_format(
                        nationaliteit.datum_van_ingang_geldigheid_met_betrekking
                    )
                    else 0,
                    "datum": nationaliteit.datum_van_ingang_geldigheid_met_betrekking,
                    "jaar": int(
                        nationaliteit.datum_van_ingang_geldigheid_met_betrekking[
                            settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                        ]
                    )
                    if is_valid_date_format(
                        nationaliteit.datum_van_ingang_geldigheid_met_betrekking
                    )
                    else 0,
                    "maand": int(
                        nationaliteit.datum_van_ingang_geldigheid_met_betrekking[
                            settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
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
                    "code": nationaliteit.reden_opname_nationaliteit,
                    "omschrijving": RedenCodeAndOmschrijving.get_omschrijving_from_code(
                        nationaliteit.reden_opname_nationaliteit
                    ),
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
                                settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                            ]
                        )
                        if is_valid_date_format(nationaliteit.datum_ingang_onderzoek)
                        else 0,
                        "datum": nationaliteit.datum_ingang_onderzoek,
                        "jaar": int(
                            nationaliteit.datum_ingang_onderzoek[
                                settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                            ]
                        )
                        if is_valid_date_format(nationaliteit.datum_ingang_onderzoek)
                        else 0,
                        "maand": int(
                            nationaliteit.datum_ingang_onderzoek[
                                settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                            ]
                        )
                        if is_valid_date_format(nationaliteit.datum_ingang_onderzoek)
                        else 0,
                    },
                },
            }
        )

    ingeschreven_persoon_dict["reisdocumenten"] = []
    for reisdocument in persoon.reisdocument_set.all():
        ingeschreven_persoon_dict["reisdocumenten"].append(
            reisdocument.nummer_nederlands_reisdocument
        )

    ingeschreven_persoon_dict["kinderen"] = []
    for kind in persoon.kind_set.all():
        ingeschreven_persoon_dict["kinderen"].append(
            convert_kind_instance_to_dict(kind)
        )

    partners_title = None
    partners_last_name_prefix = None
    partners_last_name = None
    partners_date = None
    ingeschreven_persoon_dict["partners"] = []
    for partner in persoon.partnerschap_set.all():
        ingeschreven_persoon_dict["partners"].append(
            convert_partner_instance_to_dict(partner)
        )
        if (
            not partners_last_name
            or (
                partner.datum_ontbinding_huwelijk_geregistreerd_partnerschap
                and partners_date
                > partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap
            )
            or (
                partner.datum_ontbinding_huwelijk_geregistreerd_partnerschap == ""
                and partners_date
                < partner.datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap
            )
        ):
            (
                partners_title,
                partners_last_name_prefix,
                partners_last_name,
                partners_date,
            ) = _get_partner_info(partner)

    ingeschreven_persoon_dict["ouders"] = []
    for ouder in persoon.ouder_set.all():
        ingeschreven_persoon_dict["ouders"].append(
            convert_ouder_instance_to_dict(ouder)
        )

    ingeschreven_persoon_dict["naam"]["aanhef"] = get_aanhef(
        persoon.voorvoegsel_geslachtsnaam_persoon,
        persoon.geslachtsnaam_persoon,
        partners_last_name_prefix,
        partners_last_name,
        persoon.aanduiding_naamgebruik,
        persoon.geslachtsaanduiding,
        persoon.adellijke_titel_predikaat_persoon,
        partners_title,
    )

    ingeschreven_persoon_dict["naam"]["aanschrijfwijze"] = get_aanschrijfwijze(
        persoon.voorvoegsel_geslachtsnaam_persoon,
        persoon.geslachtsnaam_persoon,
        persoon.voornamen_persoon,
        partners_last_name_prefix,
        partners_last_name,
        persoon.aanduiding_naamgebruik,
        persoon.geslachtsaanduiding,
        persoon.adellijke_titel_predikaat_persoon,
        partners_title,
    )

    ingeschreven_persoon_dict["naam"][
        "gebruikInLopendeTekst"
    ] = get_gebruik_in_lopende_tekst(
        persoon.voorvoegsel_geslachtsnaam_persoon,
        persoon.geslachtsnaam_persoon,
        partners_last_name_prefix,
        partners_last_name,
        persoon.aanduiding_naamgebruik,
        persoon.geslachtsaanduiding,
        persoon.adellijke_titel_predikaat_persoon,
        partners_title,
    )

    return ingeschreven_persoon_dict
