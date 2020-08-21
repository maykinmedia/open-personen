from collections import OrderedDict


def convert_empty_instances(dictionary):
    for key in dictionary.keys():
        if isinstance(dictionary[key], OrderedDict):
            dictionary[key] = None
        elif isinstance(dictionary[key], dict):
            convert_empty_instances(dictionary[key])
