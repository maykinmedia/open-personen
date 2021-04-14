import xmltodict

from openpersonen.utils.instance_dicts import (
    NAMESPACE_REPLACEMENTS,
    get_persoon_instance_dict,
)


def convert_response_to_persoon_dicts(response):
    dict_object = xmltodict.parse(
        response.content,
        process_namespaces=True,
        namespaces=NAMESPACE_REPLACEMENTS,
    )

    antwoord_object = dict_object["soapenv:Envelope"]["soapenv:Body"]["ns:npsLa01"][
        "ns:antwoord"
    ]["ns:object"]

    if isinstance(antwoord_object, list):
        result = []
        for antwood_dict in antwoord_object:
            result_dict = get_persoon_instance_dict(antwood_dict)
            result.append(result_dict)
    else:
        result = [get_persoon_instance_dict(antwoord_object)]

    return result
