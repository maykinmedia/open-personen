from dataclasses import dataclass

from django.conf import settings

import xmltodict

from openpersonen.api.client import client
from openpersonen.api.utils import convert_empty_instances


from .partner import Partner
from .ontbinding_huwelijk_partnerschap import OntbindingHuwelijkPartnerschap


@dataclass
class PartnerHistorie(Partner):
    ontbindingHuwelijkPartnerschap: OntbindingHuwelijkPartnerschap

    @staticmethod
    def get_instance_dict(response):
        dict_object = xmltodict.parse(response.content)

        antwoord_dict_object = dict_object["soapenv:Envelope"]["soapenv:Body"]["ns:npsLa01"]\
            ["ns:antwoord"]["ns:object"]["ns:inp.heeftAlsEchtgenootPartner"]["ns:historieFormeelRelatie"]\
            ["ns:gerelateerde"]

        partner_dict = {
            "burgerservicenummer": antwoord_dict_object["ns:inp.bsn"],
            "geslachtsaanduiding": antwoord_dict_object["ns:geslachtsaanduiding"],
            "soortVerbintenis": antwoord_dict_object["ns:soortVerbintenis"],
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
            "geboorte": {
                "datum": {
                    "dag": int(
                        antwoord_dict_object["ns:geboortedatum"][
                        settings.DAY_START: settings.DAY_END
                        ]
                    ),
                    "datum": antwoord_dict_object["ns:geboortedatum"],
                    "jaar": int(
                        antwoord_dict_object["ns:geboortedatum"][
                        settings.YEAR_START: settings.YEAR_END
                        ]
                    ),
                    "maand": int(
                        antwoord_dict_object["ns:geboortedatum"][
                        settings.MONTH_START: settings.MONTH_END
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
            "aangaanHuwelijkPartnerschap": {
                "datum": {"dag": 0, "datum": "string", "jaar": 0, "maand": 0},
                "land": {"code": "0000", "omschrijving": "string"},
                "plaats": {"code": "0000", "omschrijving": "string"},
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
            "geheimhoudingPersoonsgegevens": True,
            "ontbindingHuwelijkPartnerschap": {
                "indicatieHuwelijkPartnerschapBeeindigd": True,
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
                "reden": {
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
            }
        }

        convert_empty_instances(partner_dict)

        return partner_dict

    @classmethod
    def list(cls, bsn):
        response = client.get_partner_historie(bsn)
        instance_dict = cls.get_instance_dict(response)
        return [cls(**instance_dict)]
