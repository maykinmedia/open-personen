from collections import OrderedDict
from datetime import datetime

from django.conf import settings

from dateutil.relativedelta import relativedelta


def convert_empty_instances(dictionary):
    for key in dictionary.keys():
        if isinstance(dictionary[key], OrderedDict):
            dictionary[key] = None
        elif isinstance(dictionary[key], dict):
            convert_empty_instances(dictionary[key])


def calculate_age(person_birth_date):
    if not person_birth_date:
        return 0

    try:
        return relativedelta(
            datetime.now(),
            datetime.strptime(person_birth_date, "%Y%m%d"),
        ).years
    except ValueError:
        try:
            return datetime.now().year - int(
                person_birth_date[
                    settings.OPENPERSONEN_YEAR_START : settings.OPENPERSONEN_YEAR_END
                ]
            )
        except ValueError:
            return 0


def is_valid_date_format(date):
    if len(date) != 8:
        return False

    return date.isdigit()
