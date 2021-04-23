from openpersonen.utils.converters import convert_xml_to_dict
from openpersonen.utils.instance_dicts import (
    NAMESPACE_REPLACEMENTS,
    get_partner_instance_dict,
)


def convert_response_to_partner_dict(response, id=None):
    dict_object = convert_xml_to_dict(response.content)

    antwoord_object = dict_object["Envelope"]["Body"]["npsLa01"]["antwoord"]["object"][
        "inp.heeftAlsEchtgenootPartner"
    ]

    result = []
    if isinstance(antwoord_object, list):
        for antwood_dict in antwoord_object:
            result_dict = get_partner_instance_dict(antwood_dict["gerelateerde"])
            if not id or id == result_dict["burgerservicenummer"]:
                result.append(result_dict)
    else:
        result.append(get_partner_instance_dict(antwoord_object["gerelateerde"]))
        if id and result[0]["burgerservicenummer"] != id:
            result = []

    return result
