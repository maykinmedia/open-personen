from django.db import models
from django.utils.translation import gettext_lazy as _

from .persoon import Persoon


class Verblijfstitel(models.Model):
    persoon = models.ForeignKey(Persoon, null=True, on_delete=models.CASCADE)
    aanduiding_verblijfstitel = models.CharField(
        _("Aanduiding verblijfstitel"), max_length=200, blank=True
    )
    datum_einde_verblijfstitel = models.CharField(
        _("Datum einde verblijfstitel"), max_length=200, blank=True
    )
    ingangsdatum_verblijfstitel = models.CharField(
        _("Ingangsdatum verblijfstitel"), max_length=200, blank=True
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
            "Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Verblijfstitel"
        ),
        max_length=200,
        blank=True,
    )
    datum_van_opneming_met_betrekking = models.CharField(
        _(
            "Datum van opneming met betrekking tot de elementen van de categorie Verblijfstitel"
        ),
        max_length=200,
        blank=True,
    )
