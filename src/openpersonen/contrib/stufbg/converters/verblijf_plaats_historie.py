import xmltodict

from openpersonen.contrib.utils import convert_empty_instances


def convert_response_to_verblijf_plaats_historie_dict(response):
    dict_object = xmltodict.parse(response.content)

    antwoord_dict_object = dict_object["soapenv:Envelope"]["soapenv:Body"][
        "ns:npsLa01"
    ]["ns:antwoord"]["ns:object"]["ns:inp.verblijftIn"][
        "ns:historieFormeelRelatie"
    ][
        "ns:gerelateerde"
    ][
        "ns:adresAanduidingGrp"
    ]

    verblijf_plaats_dict = {
        "functieAdres": "woonadres",
        "huisletter": antwoord_dict_object["ns:aoa.huisletter"],
        "huisnummer": antwoord_dict_object["ns:aoa.huisnummer"],
        "huisnummertoevoeging": antwoord_dict_object["ns:aoa.huisnummertoevoeging"],
        "aanduidingBijHuisnummer": "tegenover",
        "identificatiecodeNummeraanduiding": "0518200000366054",
        "naamOpenbareRuimte": antwoord_dict_object["ns:gor.openbareRuimteNaam"],
        "postcode": antwoord_dict_object["ns:aoa.postcode"],
        "woonplaatsnaam": antwoord_dict_object["ns:wpl.woonplaatsNaam"],
        "identificatiecodeAdresseerbaarObject": "0518200000366054",
        "indicatieVestigingVanuitBuitenland": True,
        "locatiebeschrijving": "Naast de derde brug",
        "straatnaam": "string",
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
        "gemeenteVanInschrijving": {"code": "0000", "omschrijving": "Nederland"},
        "landVanwaarIngeschreven": {"code": "0000", "omschrijving": "Nederland"},
        "verblijfBuitenland": {
            "adresRegel1": "string",
            "adresRegel2": "string",
            "adresRegel3": "string",
            "vertrokkenOnbekendWaarheen": True,
            "land": {"code": "0000", "omschrijving": "Nederland"},
        },
        "inOnderzoek": {
            "aanduidingBijHuisnummer": True,
            "datumAanvangAdreshouding": True,
            "datumIngangGeldigheid": True,
            "datumInschrijvingInGemeente": True,
            "datumVestigingInNederland": True,
            "functieAdres": True,
            "gemeenteVanInschrijving": True,
            "huisletter": bool(antwoord_dict_object["ns:aoa.huisletter"]),
            "huisnummer": bool(antwoord_dict_object["ns:aoa.huisnummer"]),
            "huisnummertoevoeging": bool(
                antwoord_dict_object["ns:aoa.huisnummertoevoeging"]
            ),
            "identificatiecodeNummeraanduiding": True,
            "identificatiecodeAdresseerbaarObject": True,
            "landVanwaarIngeschreven": True,
            "locatiebeschrijving": True,
            "naamOpenbareRuimte": bool(
                antwoord_dict_object["ns:gor.openbareRuimteNaam"]
            ),
            "postcode": bool(antwoord_dict_object["ns:aoa.postcode"]),
            "straatnaam": True,
            "verblijfBuitenland": True,
            "woonplaatsnaam": bool(antwoord_dict_object["ns:wpl.woonplaatsNaam"]),
            "datumIngangOnderzoek": {
                "dag": 0,
                "datum": "string",
                "jaar": 0,
                "maand": 0,
            },
        },
        "datumTot": {"dag": 0, "datum": "string", "jaar": 0, "maand": 0},
        "geheimhoudingPersoonsgegevens": True,
    }

    convert_empty_instances(verblijf_plaats_dict)

    return verblijf_plaats_dict
