import xmltodict

from openpersonen.utils.instance_dicts import get_kind_instance_dict


def convert_response_to_kind_dict(response, id=None):
    dict_object = xmltodict.parse(
        response.content,
        process_namespaces=True,
        namespaces={
            "http://schemas.xmlsoap.org/soap/envelope/": None,
            "http://www.egem.nl/StUF/sector/bg/0310": None,
        },
    )

    antwoord_object = dict_object["Envelope"]["Body"]["npsLa01"]["antwoord"]["object"][
        "inp.heeftAlsKinderen"
    ]

    result = []
    if isinstance(antwoord_object, list):
        for antwood_dict in antwoord_object:
            result_dict = get_kind_instance_dict(antwood_dict["gerelateerde"])
            if not id or id == result_dict["burgerservicenummer"]:
                result.append(result_dict)
    else:
        result.append(get_kind_instance_dict(antwoord_object["gerelateerde"]))
        if id and result[0]["burgerservicenummer"] != id:
            result = []

    return result
