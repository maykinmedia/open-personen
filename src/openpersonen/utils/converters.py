import xmltodict

from openpersonen.utils.constants import NAMESPACE_REPLACEMENTS


def convert_xml_to_dict(xml):
    return xmltodict.parse(
        xml,
        process_namespaces=True,
        namespaces=NAMESPACE_REPLACEMENTS,
    )
