from django.db import models
from django.utils.translation import gettext_lazy as _

from .persoon import Persoon


class Gezagsverhouding(models.Model):
    persoon = models.ForeignKey(Persoon, null=True, on_delete=models.CASCADE)
    indicatie_gezag_minderjarige = models.CharField(
        _("Indicatie gezag minderjarige"), max_length=200, blank=True
    )
    indicatie_curateleregister = models.CharField(
        _("Indicatie curateleregister"), max_length=200, blank=True
    )
    gemeente_waar_de_gegevens_over_gezagsverhouding = models.CharField(
        _(
            "Gemeente waar de gegevens over gezagsverhouding aan het document ontleend zijn"
        ),
        max_length=200,
        blank=True,
    )
    datum_van_de_ontlening_van_de_gegevens_over_gezagsverhouding = models.CharField(
        _("Datum van de ontlening van de gegevens over gezagsverhouding"),
        max_length=200,
        blank=True,
    )
    beschrijving_van_het_document = models.CharField(
        _(
            "Beschrijving van het document waaraan de gegevens over gezagsverhouding ontleend zijn"
        ),
        max_length=200,
        blank=True,
    )
    aanduiding_gegevens_in_onderzoek = models.CharField(
        _("Aanduiding gegevens in onderzoek"), max_length=200, blank=True
    )
    datum_ingang_onderzoek = models.CharField(
        _("Datum ingang onderzoek"), max_length=200, blank=True
    )
    datum_einde_onderzoek = models.CharField(
        _("Datum einde onderzoek"), max_length=200, blank=True
    )
    indicatie_onjuist = models.CharField(
        _("Indicatie onjuist"), max_length=200, blank=True
    )
    ingangsdatum_geldigheid_met_betrekking = models.CharField(
        _(
            "Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Gezagsverhouding"
        ),
        max_length=200,
        blank=True,
    )
    datum_van_opneming_met_betrekking = models.CharField(
        _(
            "Datum van opneming met betrekking tot de elementen van de categorie Gezagsverhouding"
        ),
        max_length=200,
        blank=True,
    )
