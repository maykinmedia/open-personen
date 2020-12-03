from django.db import models


class CodeAndOmschrijving(models.Model):
    code = models.IntegerField()
    omschrijving = models.CharField(max_length=200)

    class Meta:
        abstract = True
