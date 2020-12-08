import xmltodict

from openpersonen.utils.instance_dicts import get_persoon_instance_dict


def convert_response_to_persoon_dicts(response):
    dict_object = xmltodict.parse(response.content)

    try:
        antwoord_object = dict_object["soapenv:Envelope"]["soapenv:Body"]["ns:npsLa01"][
            "ns:antwoord"
        ]["ns:object"]
        prefix = "ns"
    except KeyError:
        antwoord_object = dict_object["env:Envelope"]["env:Body"]["npsLa01"][
            "BG:antwoord"
        ]["object"]
        prefix = "BG"

    if isinstance(antwoord_object, list):
        result = []
        for antwood_dict in antwoord_object:
            result_dict = get_persoon_instance_dict(antwood_dict, prefix)
            result.append(result_dict)
    else:
        result = [get_persoon_instance_dict(antwoord_object, prefix)]

    return result
