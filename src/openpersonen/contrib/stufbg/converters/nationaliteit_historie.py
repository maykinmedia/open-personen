from django.conf import settings

import xmltodict

from openpersonen.api.utils import convert_empty_instances


def convert_response_to_nationaliteit_historie_dict(response):
    dict_object = xmltodict.parse(response.content)

    antwoord_dict_object = dict_object["soapenv:Envelope"]["soapenv:Body"][
        "ns:npsLa01"
    ]["ns:antwoord"]["ns:object"]["ns:inp.heeftAlsNationaliteit"]

    nationaliteit_historie_dict = {
        "aanduidingBijzonderNederlanderschap": antwoord_dict_object[
            "ns:historieMaterieel"
        ]["ns:aanduidingStrijdigheidNietigheid"],
        "datumIngangGeldigheid": {
            "dag": int(
                antwoord_dict_object["ns:historieMaterieel"][
                    "StUF:tijdvakGeldigheid"
                ]["StUF:beginGeldigheid"][
                settings.OPENPERSONEN_DAY_START: settings.OPENPERSONEN_DAY_END
                ]
            ),
            "datum": antwoord_dict_object["ns:historieMaterieel"][
                "StUF:tijdvakGeldigheid"
            ]["StUF:beginGeldigheid"],
            "jaar": int(
                antwoord_dict_object["ns:historieMaterieel"][
                    "StUF:tijdvakGeldigheid"
                ]["StUF:beginGeldigheid"][
                settings.OPENPERSONEN_YEAR_START: settings.OPENPERSONEN_YEAR_END
                ]
            ),
            "maand": int(
                antwoord_dict_object["ns:historieMaterieel"][
                    "StUF:tijdvakGeldigheid"
                ]["StUF:beginGeldigheid"][
                settings.OPENPERSONEN_MONTH_START: settings.OPENPERSONEN_MONTH_END
                ]
            ),
        },
        "nationaliteit": {"code": "0000", "omschrijving": "Nederland"},
        "redenOpname": {
            "code": "0000",
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
                ]["StUF:eindGeldigheid"][
                settings.OPENPERSONEN_DAY_START: settings.OPENPERSONEN_DAY_END
                ]
            ),
            "datum": antwoord_dict_object["ns:historieMaterieel"][
                "StUF:tijdvakGeldigheid"
            ]["StUF:eindGeldigheid"],
            "jaar": int(
                antwoord_dict_object["ns:historieMaterieel"][
                    "StUF:tijdvakGeldigheid"
                ]["StUF:eindGeldigheid"][
                settings.OPENPERSONEN_YEAR_START: settings.OPENPERSONEN_YEAR_END
                ]
            ),
            "maand": int(
                antwoord_dict_object["ns:historieMaterieel"][
                    "StUF:tijdvakGeldigheid"
                ]["StUF:eindGeldigheid"][
                settings.OPENPERSONEN_MONTH_START: settings.OPENPERSONEN_MONTH_END
                ]
            ),
        },
        "redenBeeindigen": {
            "code": "0000",
            "omschrijving": antwoord_dict_object["ns:historieFormeelRelatie"][
                "ns:inp.redenVerlies"
            ],
        },
        "indicatieNationaliteitBeeindigd": True,
    }

    convert_empty_instances(nationaliteit_historie_dict)

    return nationaliteit_historie_dict
