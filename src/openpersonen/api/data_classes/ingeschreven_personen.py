from dataclasses import dataclass
from datetime import datetime

from django.conf import settings

import xmltodict
from dateutil.relativedelta import relativedelta

from openpersonen.api.enum import GeslachtsaanduidingChoices
from openpersonen.api.models import StufBGClient
from openpersonen.api.utils import convert_empty_instances

from .datum import Datum
from .gezags_verhouding import GezagsVerhouding
from .in_onderzoek import IngeschrevenPersoonInOnderzoek
from .kiesrecht import Kiesrecht
from .naam import IngeschrevenPersoonNaam
from .nationaliteit import Nationaliteit
from .opschorting_bijhouding import OpschortingBijhouding
from .overlijden import Overlijden
from .persoon import Persoon
from .verblijf_plaats import VerblijfPlaats
from .verblijfs_titel import VerblijfsTitel


@dataclass
class IngeschrevenPersoon(Persoon):
    naam: IngeschrevenPersoonNaam
    geslachtsaanduiding: str
    leeftijd: int
    datumEersteInschrijvingGBA: Datum
    kiesrecht: Kiesrecht
    inOnderzoek: IngeschrevenPersoonInOnderzoek
    nationaliteit: Nationaliteit
    opschortingBijhouding: OpschortingBijhouding
    overlijden: Overlijden
    verblijfplaats: VerblijfPlaats
    gezagsverhouding: GezagsVerhouding
    verblijfstitel: VerblijfsTitel
    reisdocumenten: list

    def get_geslachtsaanduiding_display(self):
        return GeslachtsaanduidingChoices.values[self.geslachtsaanduiding]

    @staticmethod
    def get_client_instance_dict(response):
        dict_object = xmltodict.parse(response.content)

        antwoord_dict_object = dict_object["soapenv:Envelope"]["soapenv:Body"][
            "ns:npsLa01"
        ]["ns:antwoord"]["ns:object"]

        ingeschreven_persoon_dict = {
            "burgerservicenummer": antwoord_dict_object["ns:inp.bsn"],
            "geheimhoudingPersoonsgegevens": True,
            "naam": {
                "geslachtsnaam": antwoord_dict_object["ns:geslachtsnaam"],
                "voorletters": antwoord_dict_object["ns:voorletters"],
                "voornamen": antwoord_dict_object["ns:voornamen"],
                "voorvoegsel": antwoord_dict_object["ns:voorvoegselGeslachtsnaam"],
                "inOnderzoek": {
                    "geslachtsnaam": bool(antwoord_dict_object["ns:geslachtsnaam"]),
                    "voornamen": bool(antwoord_dict_object["ns:voornamen"]),
                    "voorvoegsel": bool(
                        antwoord_dict_object["ns:voorvoegselGeslachtsnaam"]
                    ),
                    "datumIngangOnderzoek": {
                        "dag": 0,
                        "datum": "string",
                        "jaar": 0,
                        "maand": 0,
                    },
                },
                "aanhef": antwoord_dict_object["ns:voornamen"],
                "aanschrijfwijze": "string",
                "gebruikInLopendeTekst": "string",
                "aanduidingNaamgebruik": antwoord_dict_object[
                    "ns:aanduidingNaamgebruik"
                ],
            },
            "geboorte": {
                "datum": {
                    "dag": int(
                        antwoord_dict_object["ns:geboortedatum"][
                            settings.DAY_START : settings.DAY_END
                        ]
                    ),
                    "datum": antwoord_dict_object["ns:geboortedatum"],
                    "jaar": int(
                        antwoord_dict_object["ns:geboortedatum"][
                            settings.YEAR_START : settings.YEAR_END
                        ]
                    ),
                    "maand": int(
                        antwoord_dict_object["ns:geboortedatum"][
                            settings.MONTH_START : settings.MONTH_END
                        ]
                    ),
                },
                "land": {
                    "code": "string",
                    "omschrijving": antwoord_dict_object["ns:inp.geboorteLand"],
                },
                "plaats": {
                    "code": "string",
                    "omschrijving": antwoord_dict_object["ns:inp.geboorteplaats"],
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
            "geslachtsaanduiding": antwoord_dict_object["ns:geslachtsaanduiding"],
            "leeftijd": relativedelta(
                datetime.now(),
                datetime.strptime(antwoord_dict_object["ns:geboortedatum"], "%Y%m%d"),
            ).years,
            "datumEersteInschrijvingGBA": {
                "dag": int(
                    antwoord_dict_object["ns:inp.datumInschrijving"][
                        settings.DAY_START : settings.DAY_END
                    ]
                ),
                "datum": antwoord_dict_object["ns:inp.datumInschrijving"],
                "jaar": int(
                    antwoord_dict_object["ns:inp.datumInschrijving"][
                        settings.YEAR_START : settings.YEAR_END
                    ]
                ),
                "maand": int(
                    antwoord_dict_object["ns:inp.datumInschrijving"][
                        settings.MONTH_START : settings.MONTH_END
                    ]
                ),
            },
            "kiesrecht": {
                "europeesKiesrecht": bool(
                    antwoord_dict_object["ns:ing.aanduidingEuropeesKiesrecht"]
                ),
                "uitgeslotenVanKiesrecht": bool(
                    antwoord_dict_object["ns:ing.aanduidingUitgeslotenKiesrecht"]
                ),
                "einddatumUitsluitingEuropeesKiesrecht": {
                    "dag": int(
                        antwoord_dict_object["ns:ing.aanduidingEuropeesKiesrecht"][
                            settings.DAY_START : settings.DAY_END
                        ]
                    ),
                    "datum": antwoord_dict_object["ns:ing.aanduidingEuropeesKiesrecht"],
                    "jaar": int(
                        antwoord_dict_object["ns:ing.aanduidingEuropeesKiesrecht"][
                            settings.YEAR_START : settings.YEAR_END
                        ]
                    ),
                    "maand": int(
                        antwoord_dict_object["ns:ing.aanduidingEuropeesKiesrecht"][
                            settings.MONTH_START : settings.MONTH_END
                        ]
                    ),
                },
                "einddatumUitsluitingKiesrecht": {
                    "dag": int(
                        antwoord_dict_object["ns:ing.aanduidingUitgeslotenKiesrecht"][
                            settings.DAY_START : settings.DAY_END
                        ]
                    ),
                    "datum": antwoord_dict_object[
                        "ns:ing.aanduidingUitgeslotenKiesrecht"
                    ],
                    "jaar": int(
                        antwoord_dict_object["ns:ing.aanduidingUitgeslotenKiesrecht"][
                            settings.YEAR_START : settings.YEAR_END
                        ]
                    ),
                    "maand": int(
                        antwoord_dict_object["ns:ing.aanduidingUitgeslotenKiesrecht"][
                            settings.MONTH_START : settings.MONTH_END
                        ]
                    ),
                },
            },
            "inOnderzoek": {
                "burgerservicenummer": bool(antwoord_dict_object["ns:inp.bsn"]),
                "geslachtsaanduiding": bool(
                    antwoord_dict_object["ns:geslachtsaanduiding"]
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
                    "aanduidingBijzonderNederlanderschap": antwoord_dict_object[
                        "ns:inp.aanduidingBijzonderNederlanderschap"
                    ],
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
                            antwoord_dict_object[
                                "ns:inp.aanduidingBijzonderNederlanderschap"
                            ]
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
                    "omschrijving": antwoord_dict_object["ns:inp.overlijdenLand"],
                },
                "plaats": {
                    "code": "string",
                    "omschrijving": antwoord_dict_object["ns:inp.overlijdenplaats"],
                },
                "inOnderzoek": {
                    "datum": bool(antwoord_dict_object["ns:overlijdensdatum"]),
                    "land": bool(antwoord_dict_object["ns:inp.overlijdenLand"]),
                    "plaats": bool(antwoord_dict_object["ns:inp.overlijdenplaats"]),
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
                "huisletter": antwoord_dict_object["ns:inp.verblijftIn"][
                    "ns:gerelateerde"
                ]["ns:adresAanduidingGrp"]["ns:aoa.huisletter"],
                "huisnummer": antwoord_dict_object["ns:inp.verblijftIn"][
                    "ns:gerelateerde"
                ]["ns:adresAanduidingGrp"]["ns:aoa.huisnummer"],
                "huisnummertoevoeging": antwoord_dict_object["ns:inp.verblijftIn"][
                    "ns:gerelateerde"
                ]["ns:adresAanduidingGrp"]["ns:aoa.huisnummertoevoeging"],
                "aanduidingBijHuisnummer": "tegenover",
                "identificatiecodeNummeraanduiding": "string",
                "naamOpenbareRuimte": "string",
                "postcode": antwoord_dict_object["ns:inp.verblijftIn"][
                    "ns:gerelateerde"
                ]["ns:adresAanduidingGrp"]["ns:aoa.postcode"],
                "woonplaatsnaam": antwoord_dict_object["ns:inp.verblijftIn"][
                    "ns:gerelateerde"
                ]["ns:adresAanduidingGrp"]["ns:wpl.woonplaatsNaam"],
                "identificatiecodeAdresseerbaarObject": "string",
                "indicatieVestigingVanuitBuitenland": True,
                "locatiebeschrijving": "string",
                "straatnaam": antwoord_dict_object["ns:inp.verblijftIn"][
                    "ns:gerelateerde"
                ]["ns:adresAanduidingGrp"]["ns:gor.straatnaam"],
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
                        antwoord_dict_object["ns:inp.verblijftIn"]["ns:gerelateerde"][
                            "ns:adresAanduidingGrp"
                        ]["ns:aoa.huisletter"]
                    ),
                    "huisnummer": bool(
                        antwoord_dict_object["ns:inp.verblijftIn"]["ns:gerelateerde"][
                            "ns:adresAanduidingGrp"
                        ]["ns:aoa.huisnummer"]
                    ),
                    "huisnummertoevoeging": bool(
                        antwoord_dict_object["ns:inp.verblijftIn"]["ns:gerelateerde"][
                            "ns:adresAanduidingGrp"
                        ]["ns:aoa.huisnummertoevoeging"]
                    ),
                    "identificatiecodeNummeraanduiding": True,
                    "identificatiecodeAdresseerbaarObject": True,
                    "landVanwaarIngeschreven": True,
                    "locatiebeschrijving": True,
                    "naamOpenbareRuimte": True,
                    "postcode": bool(
                        antwoord_dict_object["ns:inp.verblijftIn"]["ns:gerelateerde"][
                            "ns:adresAanduidingGrp"
                        ]["ns:aoa.postcode"]
                    ),
                    "straatnaam": bool(
                        antwoord_dict_object["ns:inp.verblijftIn"]["ns:gerelateerde"][
                            "ns:adresAanduidingGrp"
                        ]["ns:gor.straatnaam"]
                    ),
                    "verblijfBuitenland": True,
                    "woonplaatsnaam": bool(
                        antwoord_dict_object["ns:inp.verblijftIn"]["ns:gerelateerde"][
                            "ns:adresAanduidingGrp"
                        ]["ns:wpl.woonplaatsNaam"]
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

    @staticmethod
    def get_model_instance_dict(persoon):

        kiesrecht = persoon.kiesrecht_set.first()
        overlijden = persoon.overlijden_set.first()
        verblijfplaats = persoon.verblijfplaats_set.first()

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
                    "voorvoegsel": bool(
                        persoon.voorvoegsel_geslachtsnaam_persoon
                    ),
                    "datumIngangOnderzoek": {
                        "dag": 0,
                        "datum": "string",
                        "jaar": 0,
                        "maand": 0,
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
                        persoon.geboortedatum_persoon[
                        settings.DAY_START: settings.DAY_END
                        ]
                    ),
                    "datum": persoon.geboortedatum_persoon,
                    "jaar": int(
                        persoon.geboortedatum_persoon[
                        settings.YEAR_START: settings.YEAR_END
                        ]
                    ),
                    "maand": int(
                        persoon.geboortedatum_persoon[
                        settings.MONTH_START: settings.MONTH_END
                        ]
                    ),
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
            "leeftijd": relativedelta(
                datetime.now(),
                datetime.strptime(persoon.geboortedatum_persoon, "%Y%m%d"),
            ).years,
            "datumEersteInschrijvingGBA": {
                "dag": int(
                    persoon.datum_ingang_onderzoek[
                    settings.DAY_START: settings.DAY_END
                    ]
                ),
                "datum": persoon.datum_ingang_onderzoek,
                "jaar": int(
                    persoon.datum_ingang_onderzoek[
                    settings.YEAR_START: settings.YEAR_END
                    ]
                ),
                "maand": int(
                    persoon.datum_ingang_onderzoek[
                    settings.MONTH_START: settings.MONTH_END
                    ]
                ),
            },
            "kiesrecht": {
                "europeesKiesrecht": bool(
                    kiesrecht.aanduiding_europees_kiesrecht
                ),
                "uitgeslotenVanKiesrecht": bool(
                    kiesrecht.aanduiding_uitgesloten_kiesrecht
                ),
                "einddatumUitsluitingEuropeesKiesrecht": {
                    "dag": int(
                        kiesrecht.einddatum_uitsluiting_europees_kiesrecht[
                        settings.DAY_START: settings.DAY_END
                        ]
                    ),
                    "datum": kiesrecht.einddatum_uitsluiting_europees_kiesrecht,
                    "jaar": int(
                        kiesrecht.einddatum_uitsluiting_europees_kiesrecht[
                        settings.YEAR_START: settings.YEAR_END
                        ]
                    ),
                    "maand": int(
                        kiesrecht.einddatum_uitsluiting_europees_kiesrecht[
                        settings.MONTH_START: settings.MONTH_END
                        ]
                    ),
                },
                "einddatumUitsluitingKiesrecht": {
                    "dag": int(
                        kiesrecht.einddatum_uitsluiting_kiesrecht[
                        settings.DAY_START: settings.DAY_END
                        ]
                    ),
                    "datum": kiesrecht.einddatum_uitsluiting_kiesrecht,
                    "jaar": int(
                        kiesrecht.einddatum_uitsluiting_kiesrecht[
                        settings.YEAR_START: settings.YEAR_END
                        ]
                    ),
                    "maand": int(
                        kiesrecht.einddatum_uitsluiting_kiesrecht[
                        settings.MONTH_START: settings.MONTH_END
                        ]
                    ),
                },
            },
            "inOnderzoek": {
                "burgerservicenummer": bool(persoon.burgerservicenummer_persoon),
                "geslachtsaanduiding": bool(
                    persoon.geslachtsaanduiding
                ),
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
            "overlijden": {
                "indicatieOverleden": True,
                "datum": {
                    "dag": int(
                        overlijden.datum_overlijden[
                        settings.DAY_START: settings.DAY_END
                        ]
                    ),
                    "datum": overlijden.datum_overlijden,
                    "jaar": int(
                        overlijden.datum_overlijden[
                        settings.YEAR_START: settings.YEAR_END
                        ]
                    ),
                    "maand": int(
                        overlijden.datum_overlijden[
                        settings.MONTH_START: settings.MONTH_END
                        ]
                    ),
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
            },
            "verblijfplaats": {
                "functieAdres": "woonadres",
                "huisletter": verblijfplaats.huisletter,
                "huisnummer": verblijfplaats.huisnummer,
                "huisnummertoevoeging": verblijfplaats.huisnummertoevoeging,
                "aanduidingBijHuisnummer": verblijfplaats.aanduiding_bij_huisnummer,
                "identificatiecodeNummeraanduiding": verblijfplaats.identificatiecode_nummeraanduiding,
                "naamOpenbareRuimte": "string",
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
                        settings.DAY_START: settings.DAY_END
                        ]
                    ),
                    "datum": verblijfplaats.datum_aanvang_adres_buitenland,
                    "jaar": int(
                        verblijfplaats.datum_aanvang_adres_buitenland[
                        settings.YEAR_START: settings.YEAR_END
                        ]
                    ),
                    "maand": int(
                        verblijfplaats.datum_aanvang_adres_buitenland[
                        settings.MONTH_START: settings.MONTH_END
                        ]
                    ),
                },
                "datumIngangGeldigheid": {
                    "dag": int(
                        verblijfplaats.ingangsdatum_geldigheid_met_betrekking[
                        settings.DAY_START: settings.DAY_END
                        ]
                    ),
                    "datum": verblijfplaats.ingangsdatum_geldigheid_met_betrekking,
                    "jaar": int(
                        verblijfplaats.ingangsdatum_geldigheid_met_betrekking[
                        settings.YEAR_START: settings.YEAR_END
                        ]
                    ),
                    "maand": int(
                        verblijfplaats.ingangsdatum_geldigheid_met_betrekking[
                        settings.MONTH_START: settings.MONTH_END
                        ]
                    ),
                },
                "datumInschrijvingInGemeente": {
                    "dag": int(
                        verblijfplaats.datum_inschrijving_in_de_gemeente[
                        settings.DAY_START: settings.DAY_END
                        ]
                    ),
                    "datum": verblijfplaats.datum_inschrijving_in_de_gemeente,
                    "jaar": int(
                        verblijfplaats.datum_inschrijving_in_de_gemeente[
                        settings.YEAR_START: settings.YEAR_END
                        ]
                    ),
                    "maand": int(
                        verblijfplaats.datum_inschrijving_in_de_gemeente[
                        settings.MONTH_START: settings.MONTH_END
                        ]
                    ),
                },
                "datumVestigingInNederland": {
                    "dag": int(
                        verblijfplaats.datum_vestiging_in_nederland[
                        settings.DAY_START: settings.DAY_END
                        ]
                    ),
                    "datum": verblijfplaats.datum_vestiging_in_nederland,
                    "jaar": int(
                        verblijfplaats.datum_vestiging_in_nederland[
                        settings.YEAR_START: settings.YEAR_END
                        ]
                    ),
                    "maand": int(
                        verblijfplaats.datum_vestiging_in_nederland[
                        settings.MONTH_START: settings.MONTH_END
                        ]
                    ),
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
                        verblijfplaats.huisletter
                    ),
                    "huisnummer": bool(
                        verblijfplaats.huisnummer
                    ),
                    "huisnummertoevoeging": bool(
                        verblijfplaats.huisnummertoevoeging
                    ),
                    "identificatiecodeNummeraanduiding": True,
                    "identificatiecodeAdresseerbaarObject": True,
                    "landVanwaarIngeschreven": True,
                    "locatiebeschrijving": True,
                    "naamOpenbareRuimte": True,
                    "postcode": bool(
                        verblijfplaats.postcode
                    ),
                    "straatnaam": bool(
                        verblijfplaats.straatnaam
                    ),
                    "verblijfBuitenland": True,
                    "woonplaatsnaam": bool(
                        verblijfplaats.woonplaatsnaam
                    ),
                    "datumIngangOnderzoek": {
                        "dag": int(
                            verblijfplaats.datum_ingang_onderzoek[
                            settings.DAY_START: settings.DAY_END
                            ]
                        ),
                        "datum": verblijfplaats.datum_ingang_onderzoek,
                        "jaar": int(
                            verblijfplaats.datum_ingang_onderzoek[
                            settings.YEAR_START: settings.YEAR_END
                            ]
                        ),
                        "maand": int(
                            verblijfplaats.datum_ingang_onderzoek[
                            settings.MONTH_START: settings.MONTH_END
                            ]
                        ),
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

        ingeschreven_persoon_dict['nationaliteit'] = []

        nationaliteiten = persoon.nationaliteit_set.all()

        for nationaliteit in nationaliteiten:
            ingeschreven_persoon_dict['nationaliteit'].append(
                {
                    "aanduidingBijzonderNederlanderschap": nationaliteit.aanduiding_bijzonder_nederlanderschap,
                    "datumIngangGeldigheid": {
                        "dag": int(
                            kiesrecht.datum_van_ingang_geldigheid_met_betrekking[
                            settings.DAY_START: settings.DAY_END
                            ]
                        ),
                        "datum": kiesrecht.datum_van_ingang_geldigheid_met_betrekking,
                        "jaar": int(
                            kiesrecht.datum_van_ingang_geldigheid_met_betrekking[
                            settings.YEAR_START: settings.YEAR_END
                            ]
                        ),
                        "maand": int(
                            kiesrecht.datum_van_ingang_geldigheid_met_betrekking[
                            settings.MONTH_START: settings.MONTH_END
                            ]
                        ),
                    },
                    "nationaliteit": {
                        "code": "string",
                        "omschrijving": nationaliteit.nationaliteit
                    },
                    "redenOpname": {
                        "code": "string",
                        "omschrijving": nationaliteit.reden_opname_nationaliteit
                    },
                    "inOnderzoek": {
                        "aanduidingBijzonderNederlanderschap": bool(
                            nationaliteit.aanduiding_bijzonder_nederlanderschap
                        ),
                        "nationaliteit": bool(nationaliteit.nationaliteit),
                        "redenOpname": bool(nationaliteit.reden_opname_nationaliteit),
                        "datumIngangOnderzoek": {
                            "dag": int(
                                kiesrecht.datum_ingang_onderzoek[
                                settings.DAY_START: settings.DAY_END
                                ]
                            ),
                            "datum": kiesrecht.datum_ingang_onderzoek,
                            "jaar": int(
                                kiesrecht.datum_ingang_onderzoek[
                                settings.YEAR_START: settings.YEAR_END
                                ]
                            ),
                            "maand": int(
                                kiesrecht.datum_ingang_onderzoek[
                                settings.MONTH_START: settings.MONTH_END
                                ]
                            ),
                        },
                    },
                }
            )

        return ingeschreven_persoon_dict

    @classmethod
    def list(cls, filters):
        if settings.USE_STUF_BG_DATABASE:
            pass
        else:
            response = StufBGClient.get_solo().get_ingeschreven_persoon(filters=filters)
            instance_dict = cls.get_client_instance_dict(response)
        return [cls(**instance_dict)]

    @classmethod
    def retrieve(cls, bsn=None):
        if settings.USE_STUF_BG_DATABASE:
            instance = Persoon.objects.get(burgerservicenummer_persoon=bsn)
            instance_dict = cls.get_model_instance_dict(instance)
        else:
            response = StufBGClient.get_solo().get_ingeschreven_persoon(bsn=bsn)
            instance_dict = cls.get_client_instance_dict(response)
        return cls(**instance_dict)
