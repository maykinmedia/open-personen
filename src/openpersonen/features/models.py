from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class CodeAndOmschrijving(models.Model):
    code = models.IntegerField()
    omschrijving = models.CharField(max_length=200)

    class Meta:
        abstract = True

    @classmethod
    def get_code_from_omschrijving(cls, omschrijving):
        try:
            return cls.objects.get(omschrijving=omschrijving).code
        except ObjectDoesNotExist:
            return 0

    @classmethod
    def get_omschrijving_from_code(cls, code):
        try:
            return cls.objects.get(code=code).omschrijving
        except ObjectDoesNotExist:
            return "Onbekend"
