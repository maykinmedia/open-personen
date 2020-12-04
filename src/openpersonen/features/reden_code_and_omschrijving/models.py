from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from openpersonen.features.models import CodeAndOmschrijving


class RedenCodeAndOmschrijving(CodeAndOmschrijving):

    code = models.CharField(max_length=1)

    @classmethod
    def get_code_from_omschrijving(cls, omschrijving):
        try:
            return cls.objects.get(omschrijving=omschrijving).code
        except ObjectDoesNotExist:
            return "."
