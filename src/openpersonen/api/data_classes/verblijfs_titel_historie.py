from dataclasses import dataclass

from django.conf import settings

import xmltodict

from openpersonen.contrib.stufbg.models import StufBGClient
from openpersonen.api.utils import convert_empty_instances

from .verblijfs_titel import VerblijfsTitel


@dataclass
class VerblijfsTitelHistorie(VerblijfsTitel):
    geheimhoudingPersoonsgegevens: bool

    @staticmethod
    def get_instance_dict(response):
        dict_object = xmltodict.parse(response.content)

        antwoord_dict_object = dict_object["soapenv:Envelope"]["soapenv:Body"][
            "ns:npsLa01"
        ]["ns:antwoord"]["ns:object"]["ns:historieMaterieel"]

        verblijf_plaats_dict = {
            "aanduiding": {
                "code": "0000",
                "omschrijving": antwoord_dict_object["ns:vbt.aanduidingVerblijfstitel"],
            },
            "datumEinde": {
                "dag": int(
                    antwoord_dict_object["StUF:tijdvakGeldigheid"][
                        "StUF:beginGeldigheid"
                    ][settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END]
                ),
                "datum": antwoord_dict_object["StUF:tijdvakGeldigheid"][
                    "StUF:beginGeldigheid"
                ],
                "jaar": int(
                    antwoord_dict_object["StUF:tijdvakGeldigheid"][
                        "StUF:beginGeldigheid"
                    ][settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END]
                ),
                "maand": int(
                    antwoord_dict_object["StUF:tijdvakGeldigheid"][
                        "StUF:beginGeldigheid"
                    ][
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                ),
            },
            "datumIngang": {
                "dag": int(
                    antwoord_dict_object["StUF:tijdvakGeldigheid"][
                        "StUF:eindGeldigheid"
                    ][settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END]
                ),
                "datum": antwoord_dict_object["StUF:tijdvakGeldigheid"][
                    "StUF:eindGeldigheid"
                ],
                "jaar": int(
                    antwoord_dict_object["StUF:tijdvakGeldigheid"][
                        "StUF:eindGeldigheid"
                    ][settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END]
                ),
                "maand": int(
                    antwoord_dict_object["StUF:tijdvakGeldigheid"][
                        "StUF:eindGeldigheid"
                    ][
                        settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                    ]
                ),
            },
            "inOnderzoek": {
                "aanduiding": bool(
                    antwoord_dict_object["ns:vbt.aanduidingVerblijfstitel"]
                ),
                "datumEinde": bool(
                    antwoord_dict_object["StUF:tijdvakGeldigheid"][
                        "StUF:eindGeldigheid"
                    ]
                ),
                "datumIngang": bool(
                    antwoord_dict_object["StUF:tijdvakGeldigheid"][
                        "StUF:beginGeldigheid"
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
        }
        convert_empty_instances(verblijf_plaats_dict)

        return verblijf_plaats_dict

    @classmethod
    def list(cls, bsn, filters):
        response = StufBGClient.get_solo().get_verblijfs_titel_historie(bsn, filters)
        instance_dict = cls.get_instance_dict(response)
        return [cls(**instance_dict)]
