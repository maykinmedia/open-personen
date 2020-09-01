from dataclasses import dataclass

from django.conf import settings

import xmltodict

from openpersonen.api.client import client
from openpersonen.api.utils import convert_empty_instances

from .datum import Datum
from .nationaliteit import Nationaliteit
from .waarde import Waarde


@dataclass
class NationaliteitHistorie(Nationaliteit):
    geheimhoudingPersoonsgegevens: bool
    datumEindeGeldigheid: Datum
    redenBeeindigen: Waarde
    indicatieNationaliteitBeeindigd: bool

    @staticmethod
    def get_instance_dict(response):
        dict_object = xmltodict.parse(response.content)

        antwoord_dict_object = dict_object["soapenv:Envelope"]["soapenv:Body"][
            "ns:npsLa01"
        ]["ns:antwoord"]["ns:object"]["ns:inp.heeftAlsNationaliteit"]

        verblijf_plaats_dict = {
            "aanduidingBijzonderNederlanderschap": antwoord_dict_object[
                "ns:historieMaterieel"
            ]["ns:aanduidingStrijdigheidNietigheid"],
            "datumIngangGeldigheid": {
                "dag": int(
                    antwoord_dict_object["ns:historieMaterieel"][
                        "StUF:tijdvakGeldigheid"
                    ]["StUF:beginGeldigheid"][settings.DAY_START : settings.DAY_END]
                ),
                "datum": antwoord_dict_object["ns:historieMaterieel"][
                    "StUF:tijdvakGeldigheid"
                ]["StUF:beginGeldigheid"],
                "jaar": int(
                    antwoord_dict_object["ns:historieMaterieel"][
                        "StUF:tijdvakGeldigheid"
                    ]["StUF:beginGeldigheid"][settings.YEAR_START : settings.YEAR_END]
                ),
                "maand": int(
                    antwoord_dict_object["ns:historieMaterieel"][
                        "StUF:tijdvakGeldigheid"
                    ]["StUF:beginGeldigheid"][settings.MONTH_START : settings.MONTH_END]
                ),
            },
            "nationaliteit": {"code": "0000", "omschrijving": "Nederland"},
            "redenOpname": {
                "code": "6030",
                "omschrijving": antwoord_dict_object["ns:historieFormeelRelatie"][
                    "ns:inp.redenVerkrijging"
                ],
            },
            "inOnderzoek": {
                "aanduidingBijzonderNederlanderschap": bool(
                    antwoord_dict_object["ns:historieMaterieel"][
                        "ns:aanduidingStrijdigheidNietigheid"
                    ]
                ),
                "nationaliteit": True,
                "redenOpname": bool(
                    antwoord_dict_object["ns:historieFormeelRelatie"][
                        "ns:inp.redenVerkrijging"
                    ]
                ),
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0,
                },
            },
            "geheimhoudingPersoonsgegevens": True,
            "datumEindeGeldigheid": {
                "dag": int(
                    antwoord_dict_object["ns:historieMaterieel"][
                        "StUF:tijdvakGeldigheid"
                    ]["StUF:eindGeldigheid"][settings.DAY_START : settings.DAY_END]
                ),
                "datum": antwoord_dict_object["ns:historieMaterieel"][
                    "StUF:tijdvakGeldigheid"
                ]["StUF:eindGeldigheid"],
                "jaar": int(
                    antwoord_dict_object["ns:historieMaterieel"][
                        "StUF:tijdvakGeldigheid"
                    ]["StUF:eindGeldigheid"][settings.YEAR_START : settings.YEAR_END]
                ),
                "maand": int(
                    antwoord_dict_object["ns:historieMaterieel"][
                        "StUF:tijdvakGeldigheid"
                    ]["StUF:eindGeldigheid"][settings.MONTH_START : settings.MONTH_END]
                ),
            },
            "redenBeeindigen": {
                "code": "6030",
                "omschrijving": antwoord_dict_object["ns:historieFormeelRelatie"][
                    "ns:inp.redenVerlies"
                ],
            },
            "indicatieNationaliteitBeeindigd": True,
        }

        convert_empty_instances(verblijf_plaats_dict)

        return verblijf_plaats_dict

    @classmethod
    def list(cls, bsn, filters):
        response = client.get_nationaliteit_historie(bsn, filters)
        instance_dict = cls.get_instance_dict(response)
        return [cls(**instance_dict)]
