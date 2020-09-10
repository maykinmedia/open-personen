from django.db import models
from django.utils.translation import gettext_lazy as _

from .persoon import Persoon


class Kiesrecht(models.Model):
    persoon = models.ForeignKey(Persoon, null=True, on_delete=models.CASCADE)
    aanduiding_europees_kiesrecht = models.CharField(
        _("Aanduiding Europees kiesrecht"), max_length=200, blank=True
    )
    datum_verzoek_of_mededeling_europees_kiesrecht = models.CharField(
        _("Datum verzoek of mededeling Europees kiesrecht"), max_length=200, blank=True
    )
    einddatum_uitsluiting_europees_kiesrecht = models.CharField(
        _("Einddatum uitsluiting Europees kiesrecht"), max_length=200, blank=True
    )
    aanduiding_uitgesloten_kiesrecht = models.CharField(
        _("Aanduiding uitgesloten kiesrecht"), max_length=200, blank=True
    )
    einddatum_uitsluiting_kiesrecht = models.CharField(
        _("Einddatum uitsluiting kiesrecht"), max_length=200, blank=True
    )
    gemeente_waar_de_gegevens_over_kiesrecht = models.CharField(
        _("Gemeente waar de gegevens over kiesrecht aan het document ontleend zijn"),
        max_length=200,
        blank=True,
    )
    datum_van_de_ontlening_van_de_gegevens_over_kiesrecht = models.CharField(
        _("Datum van de ontlening van de gegevens over kiesrecht"),
        max_length=200,
        blank=True,
    )
    beschrijving_van_het_document = models.CharField(
        _(
            "Beschrijving van het document waaraan de gegevens over kiesrecht ontleend zijn"
        ),
        max_length=200,
        blank=True,
    )
