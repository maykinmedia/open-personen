from collections import OrderedDict
from datetime import datetime


def convert_empty_instances(dictionary):
    for key in dictionary.keys():
        if isinstance(dictionary[key], OrderedDict):
            dictionary[key] = None
        elif isinstance(dictionary[key], dict):
            convert_empty_instances(dictionary[key])


def is_expected_date_format(value):
    try:
        datetime.strptime(value, "%Y%m%d")
        return True
    except ValueError:
        return False
