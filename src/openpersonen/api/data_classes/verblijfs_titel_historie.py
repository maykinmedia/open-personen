from dataclasses import dataclass

import xmltodict
from django.conf import settings

from openpersonen.api.utils import convert_empty_instances
from openpersonen.api.client import client

from .verblijfs_titel import VerblijfsTitel


@dataclass
class VerblijfsTitelHistorie(VerblijfsTitel):
    geheimhoudingPersoonsgegevens: bool

    @staticmethod
    def get_instance_dict(response):
        dict_object = xmltodict.parse(response.content)

        antwoord_dict_object = dict_object["soapenv:Envelope"]["soapenv:Body"]["ns:npsLa01"]["ns:antwoord"]["ns:object"] \
        ['ns:historieMaterieel']

        verblijf_plaats_dict = {
            "aanduiding": {
                "code": "0000",
                "omschrijving": antwoord_dict_object["ns:vbt.aanduidingVerblijfstitel"]
            },
            "datumEinde": {
                "dag": int(antwoord_dict_object["StUF:tijdvakGeldigheid"]["StUF:beginGeldigheid"][settings.DAY_START:settings.DAY_END]),
                "datum": antwoord_dict_object["StUF:tijdvakGeldigheid"]["StUF:beginGeldigheid"],
                "jaar": int(antwoord_dict_object["StUF:tijdvakGeldigheid"]["StUF:beginGeldigheid"][settings.YEAR_START:settings.YEAR_END]),
                "maand": int(antwoord_dict_object["StUF:tijdvakGeldigheid"]["StUF:beginGeldigheid"][settings.MONTH_START:settings.MONTH_END])
            },
            "datumIngang": {
                "dag": int(antwoord_dict_object["StUF:tijdvakGeldigheid"]["StUF:eindGeldigheid"][settings.DAY_START:settings.DAY_END]),
                "datum": antwoord_dict_object["StUF:tijdvakGeldigheid"]["StUF:eindGeldigheid"],
                "jaar": int(antwoord_dict_object["StUF:tijdvakGeldigheid"]["StUF:eindGeldigheid"][settings.YEAR_START:settings.YEAR_END]),
                "maand": int(antwoord_dict_object["StUF:tijdvakGeldigheid"]["StUF:eindGeldigheid"][settings.MONTH_START:settings.MONTH_END])
            },
            "inOnderzoek": {
                "aanduiding": bool(antwoord_dict_object["ns:vbt.aanduidingVerblijfstitel"]),
                "datumEinde": bool(antwoord_dict_object["StUF:tijdvakGeldigheid"]["StUF:eindGeldigheid"]),
                "datumIngang": bool(antwoord_dict_object["StUF:tijdvakGeldigheid"]["StUF:beginGeldigheid"]),
                "datumIngangOnderzoek": {
                    "dag": 0,
                    "datum": "string",
                    "jaar": 0,
                    "maand": 0
                }
            },
            "geheimhoudingPersoonsgegevens": True
        }
        convert_empty_instances(verblijf_plaats_dict)

        return verblijf_plaats_dict

    @classmethod
    def list(cls, bsn):
        response = client.get_verblijfs_titel_historie(bsn)
        instance_dict = cls.get_instance_dict(response)
        return [cls(**instance_dict)]
