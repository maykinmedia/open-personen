from dataclasses import dataclass

from django.conf import settings

import xmltodict

from openpersonen.api.enum import GeslachtsaanduidingChoices, OuderAanduiding
from openpersonen.api.models import StufBGClient
from openpersonen.api.testing_models import Persoon as PersoonModel
from openpersonen.api.utils import convert_empty_instances

from .datum import Datum
from .in_onderzoek import OuderInOnderzoek
from .persoon import Persoon


@dataclass
class Ouder(Persoon):
    geslachtsaanduiding: str
    ouderAanduiding: str
    datumIngangFamilierechtelijkeBetrekking: Datum
    inOnderzoek: OuderInOnderzoek

    def get_geslachtsaanduiding_display(self):
        return GeslachtsaanduidingChoices.values[self.geslachtsaanduiding]

    def get_ouderAanduiding_display(self):
        return OuderAanduiding.values[self.ouderAanduiding]

    @staticmethod
    def get_client_instance_dict(response):
        dict_object = xmltodict.parse(response.content)

        antwoord_dict_object = dict_object["soapenv:Envelope"]["soapenv:Body"][
            "ns:npsLa01"
        ]["ns:antwoord"]["ns:object"]["ns:inp.heeftAlsOuders"]["ns:gerelateerde"]

        ouder_dict = {
            "burgerservicenummer": antwoord_dict_object["ns:inp.bsn"],
            "geslachtsaanduiding": antwoord_dict_object["ns:geslachtsaanduiding"],
            "ouderAanduiding": antwoord_dict_object["ns:ouderAanduiding"],
            "datumIngangFamilierechtelijkeBetrekking": {
                "dag": int(
                    antwoord_dict_object["ns:datumIngangFamilierechtelijkeBetrekking"][
                        settings.DAY_START : settings.DAY_END
                    ]
                ),
                "datum": antwoord_dict_object[
                    "ns:datumIngangFamilierechtelijkeBetrekking"
                ],
                "jaar": int(
                    antwoord_dict_object["ns:datumIngangFamilierechtelijkeBetrekking"][
                        settings.YEAR_START : settings.YEAR_END
                    ]
                ),
                "maand": int(
                    antwoord_dict_object["ns:datumIngangFamilierechtelijkeBetrekking"][
                        settings.MONTH_START : settings.MONTH_END
                    ]
                ),
            },
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
            },
            "inOnderzoek": {
                "burgerservicenummer": bool(antwoord_dict_object["ns:inp.bsn"]),
                "datumIngangFamilierechtelijkeBetrekking": bool(
                    antwoord_dict_object["ns:datumIngangFamilierechtelijkeBetrekking"]
                ),
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
                    "code": "0000",
                    "omschrijving": antwoord_dict_object["ns:inp.geboorteLand"],
                },
                "plaats": {
                    "code": "0000",
                    "omschrijving": antwoord_dict_object["ns:inp.geboorteplaats"],
                },
                "inOnderzoek": {
                    "datum": bool(antwoord_dict_object["ns:geboortedatum"]),
                    "land": bool(antwoord_dict_object["ns:inp.geboorteLand"]),
                    "plaats": bool(antwoord_dict_object["ns:inp.geboorteplaats"]),
                    "datumIngangOnderzoek": {
                        "dag": 0,
                        "datum": "string",
                        "jaar": 0,
                        "maand": 0,
                    },
                },
            },
            "geheimhoudingPersoonsgegevens": True,
        }

        convert_empty_instances(ouder_dict)

        return ouder_dict

    @staticmethod
    def get_model_instance_dict(ouder):

        ouder_dict = {
            "burgerservicenummer": ouder.burgerservicenummer_ouder,
            "geslachtsaanduiding": ouder.geslachtsaanduiding_ouder,
            "ouderAanduiding": ouder.geslachtsaanduiding_ouder,
            "datumIngangFamilierechtelijkeBetrekking": {
                "dag": int(
                    ouder.datum_ingang_familierechtelijke_betrekking_ouder[
                        settings.DAY_START : settings.DAY_END
                    ] if ouder.datum_ingang_familierechtelijke_betrekking_ouder else 0
                ),
                "datum": ouder.datum_ingang_familierechtelijke_betrekking_ouder,
                "jaar": int(
                    ouder.datum_ingang_familierechtelijke_betrekking_ouder[
                        settings.YEAR_START : settings.YEAR_END
                    ] if ouder.datum_ingang_familierechtelijke_betrekking_ouder else 0
                ),
                "maand": int(
                    ouder.datum_ingang_familierechtelijke_betrekking_ouder[
                        settings.MONTH_START : settings.MONTH_END
                    ] if ouder.datum_ingang_familierechtelijke_betrekking_ouder else 0
                ),
            },
            "naam": {
                "geslachtsnaam": ouder.geslachtsnaam_ouder,
                "voorletters": "string",
                "voornamen": ouder.voornamen_ouder,
                "voorvoegsel": ouder.voorvoegsel_geslachtsnaam_ouder,
                "inOnderzoek": {
                    "geslachtsnaam": bool(ouder.geslachtsnaam_ouder),
                    "voornamen": bool(ouder.voornamen_ouder),
                    "voorvoegsel": bool(ouder.voorvoegsel_geslachtsnaam_ouder),
                    "datumIngangOnderzoek": {
                        "dag": 0,
                        "datum": "string",
                        "jaar": 0,
                        "maand": 0,
                    },
                },
            },
            "inOnderzoek": {
                "burgerservicenummer": bool(ouder.burgerservicenummer_ouder),
                "datumIngangFamilierechtelijkeBetrekking": bool(
                    ouder.datum_ingang_familierechtelijke_betrekking_ouder
                ),
                "geslachtsaanduiding": bool(ouder.geslachtsaanduiding_ouder),
                "datumIngangOnderzoek": {
                    "dag": int(
                        ouder.datum_ingang_onderzoek[
                            settings.DAY_START : settings.DAY_END
                        ] if ouder.datum_ingang_onderzoek else 0
                    ),
                    "datum": ouder.datum_ingang_onderzoek,
                    "jaar": int(
                        ouder.datum_ingang_onderzoek[
                            settings.YEAR_START : settings.YEAR_END
                        ] if ouder.datum_ingang_onderzoek else 0
                    ),
                    "maand": int(
                        ouder.datum_ingang_onderzoek[
                            settings.MONTH_START : settings.MONTH_END
                        ] if ouder.datum_ingang_onderzoek else 0
                    ),
                },
            },
            "geboorte": {
                "datum": {
                    "dag": int(
                        ouder.geboortedatum_ouder[settings.DAY_START : settings.DAY_END]
                    ) if ouder.geboortedatum_ouder else 0,
                    "datum": ouder.geboortedatum_ouder,
                    "jaar": int(
                        ouder.geboortedatum_ouder[
                            settings.YEAR_START : settings.YEAR_END
                        ]
                    ) if ouder.geboortedatum_ouder else 0,
                    "maand": int(
                        ouder.geboortedatum_ouder[
                            settings.MONTH_START : settings.MONTH_END
                        ]
                    ) if ouder.geboortedatum_ouder else 0,
                },
                "land": {
                    "code": "0000",
                    "omschrijving": ouder.geboorteland_ouder,
                },
                "plaats": {
                    "code": "0000",
                    "omschrijving": ouder.geboorteplaats_ouder,
                },
                "inOnderzoek": {
                    "datum": bool(ouder.geboortedatum_ouder),
                    "land": bool(ouder.geboorteland_ouder),
                    "plaats": bool(ouder.geboorteplaats_ouder),
                    "datumIngangOnderzoek": {
                        "dag": 0,
                        "datum": "string",
                        "jaar": 0,
                        "maand": 0,
                    },
                },
            },
            "geheimhoudingPersoonsgegevens": True,
        }

        return ouder_dict

    @classmethod
    def list(cls, bsn):
        class_instances = []
        if getattr(settings, "USE_STUF_BG_DATABASE", False):
            instances = PersoonModel.objects.get(
                burgerservicenummer_persoon=bsn
            ).ouder_set.all()
            for instance in instances:
                instance_dict = cls.get_model_instance_dict(instance)
                class_instances.append(cls(**instance_dict))
        return class_instances

    @classmethod
    def retrieve(cls, bsn, id):
        if getattr(settings, "USE_STUF_BG_DATABASE", False):
            instance = PersoonModel.objects.get(
                burgerservicenummer_persoon=bsn
            ).ouder_set.get(burgerservicenummer_ouder=id)
            instance_dict = cls.get_model_instance_dict(instance)
        else:
            response = StufBGClient.get_solo().get_ouder(bsn)
            instance_dict = cls.get_client_instance_dict(response)
        return cls(**instance_dict)
