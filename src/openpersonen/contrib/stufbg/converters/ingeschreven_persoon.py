from openpersonen.utils.instance_dicts import (
    NAMESPACE_REPLACEMENTS,
    get_persoon_instance_dict,
)
from src.openpersonen.utils.converters import convert_xml_to_dict


def convert_response_to_persoon_dicts(response):
    dict_object = convert_xml_to_dict(response.content)

    antwoord_object = dict_object["Envelope"]["Body"]["npsLa01"]["antwoord"]["object"]

    if isinstance(antwoord_object, list):
        result = []
        for antwood_dict in antwoord_object:
            result_dict = get_persoon_instance_dict(antwood_dict)
            result.append(result_dict)
    else:
        result = [get_persoon_instance_dict(antwoord_object)]

    return result
