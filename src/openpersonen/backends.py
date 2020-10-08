from django.conf import settings
from django.utils.module_loading import import_string


def get_backend():
    return import_string(settings.OPENPERSONEN_BACKEND)
