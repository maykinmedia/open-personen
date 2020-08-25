from dataclasses import dataclass

import xmltodict

from openpersonen.api.client import client
from openpersonen.api.enum import GeslachtsaanduidingChoices, OuderAanduiding
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
    def get_instance_dict(response):
        dict_object = xmltodict.parse(response.content)

        antwoord_dict_object = dict_object['soapenv:Envelope']['soapenv:Body']['ns:npsLa01']['ns:antwoord']['ns:object']['ns:inp.heeftAlsOuders']['ns:gerelateerde']

        ouder_dict = {
            "burgerservicenummer": antwoord_dict_object['ns:inp.bsn'],
            "geslachtsaanduiding": antwoord_dict_object['ns:geslachtsaanduiding'],
            "ouderAanduiding": antwoord_dict_object['ns:ouderAanduiding'],
            "datumIngangFamilierechtelijkeBetrekking": {
                "dag": antwoord_dict_object['ns:datumIngangFamilierechtelijkeBetrekking'][6:8],
                "datum": antwoord_dict_object['ns:datumIngangFamilierechtelijkeBetrekking'],
                "jaar": antwoord_dict_object['ns:datumIngangFamilierechtelijkeBetrekking'][0:4],
                "maand": antwoord_dict_object['ns:datumIngangFamilierechtelijkeBetrekking'][4:6]
            },
            "naam": {
                "geslachtsnaam": antwoord_dict_object['ns:geslachtsnaam'],
                "voorletters": antwoord_dict_object['ns:voorletters'],
                "voornamen": antwoord_dict_object['ns:voornamen'],
                "voorvoegsel": antwoord_dict_object['ns:voorvoegselGeslachtsnaam'],
                "inOnderzoek": {
                    "geslachtsnaam": bool(antwoord_dict_object['ns:geslachtsnaam']),
                    "voornamen": bool(antwoord_dict_object['ns:voornamen']),
                    "voorvoegsel": bool(antwoord_dict_object['ns:voorvoegselGeslachtsnaam']),
                    "datumIngangOnderzoek": {
                        "dag": 0,
                        "datum": "string",
                        "jaar": 0,
                        "maand": 0
                    }
                }
            },
            "inOnderzoek": {
                "burgerservicenummer": bool(antwoord_dict_object['ns:inp.bsn']),
                "datumIngangFamilierechtelijkeBetrekking": bool(antwoord_dict_object['ns:datumIngangFamilierechtelijkeBetrekking']),
                "geslachtsaanduiding": bool(antwoord_dict_object['ns:geslachtsaanduiding']),
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0
                }
            },
            "geboorte": {
                "datum": {
                    "dag": antwoord_dict_object['ns:geboortedatum'][6:8],
                    "datum": antwoord_dict_object['ns:geboortedatum'],
                    "jaar": antwoord_dict_object['ns:geboortedatum'][0:4],
                    "maand": antwoord_dict_object['ns:geboortedatum'][4:6]
                },
                "land": {
                    "code": "0000",
                    "omschrijving": antwoord_dict_object['ns:inp.geboorteLand']
                },
                "plaats": {
                    "code": "0000",
                    "omschrijving": antwoord_dict_object['ns:inp.geboorteplaats']
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
            "geheimhoudingPersoonsgegevens": True
        }

        convert_empty_instances(ouder_dict)

        return ouder_dict

    @classmethod
    def retrieve(cls, bsn):
        response = client.get_ouder(bsn)
        instance_dict = cls.get_instance_dict(response)
        return cls(**instance_dict)
