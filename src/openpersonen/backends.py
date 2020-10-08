from django.conf import settings
from django.utils.module_loading import import_string

backend = import_string(settings.OPENPERSONEN_BACKEND)
