from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = "openpersonen.utils"

    def ready(self):
        from . import checks  # noqa
