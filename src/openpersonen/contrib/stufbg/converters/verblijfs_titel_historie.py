from django.conf import settings

import xmltodict

from openpersonen.utils.helpers import convert_empty_instances


def convert_response_to_verblijfs_titel_historie_dict(response):
    dict_object = xmltodict.parse(response.content)

    antwoord_dict_object = dict_object["soapenv:Envelope"]["soapenv:Body"][
        "ns:npsLa01"
    ]["ns:antwoord"]["ns:object"]["ns:historieMaterieel"]

    verblijfs_titel_dict = {
        "aanduiding": {
            "code": "0000",
            "omschrijving": antwoord_dict_object["ns:vbt.aanduidingVerblijfstitel"],
        },
        "datumEinde": {
            "dag": int(
                antwoord_dict_object["StUF:tijdvakGeldigheid"]["StUF:beginGeldigheid"][
                    settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                ]
            ),
            "datum": antwoord_dict_object["StUF:tijdvakGeldigheid"][
                "StUF:beginGeldigheid"
            ],
            "jaar": int(
                antwoord_dict_object["StUF:tijdvakGeldigheid"]["StUF:beginGeldigheid"][
                    settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                ]
            ),
            "maand": int(
                antwoord_dict_object["StUF:tijdvakGeldigheid"]["StUF:beginGeldigheid"][
                    settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                ]
            ),
        },
        "datumIngang": {
            "dag": int(
                antwoord_dict_object["StUF:tijdvakGeldigheid"]["StUF:eindGeldigheid"][
                    settings.OPENPERSONEN_DAY_START : settings.OPENPERSONEN_DAY_END
                ]
            ),
            "datum": antwoord_dict_object["StUF:tijdvakGeldigheid"][
                "StUF:eindGeldigheid"
            ],
            "jaar": int(
                antwoord_dict_object["StUF:tijdvakGeldigheid"]["StUF:eindGeldigheid"][
                    settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                ]
            ),
            "maand": int(
                antwoord_dict_object["StUF:tijdvakGeldigheid"]["StUF:eindGeldigheid"][
                    settings.OPENPERSONEN_MONTH_START : settings.OPENPERSONEN_MONTH_END
                ]
            ),
        },
        "inOnderzoek": {
            "aanduiding": bool(antwoord_dict_object["ns:vbt.aanduidingVerblijfstitel"]),
            "datumEinde": bool(
                antwoord_dict_object["StUF:tijdvakGeldigheid"]["StUF:eindGeldigheid"]
            ),
            "datumIngang": bool(
                antwoord_dict_object["StUF:tijdvakGeldigheid"]["StUF:beginGeldigheid"]
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
    convert_empty_instances(verblijfs_titel_dict)

    return verblijfs_titel_dict
