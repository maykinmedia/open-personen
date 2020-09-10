from django.db import models
from django.utils.translation import gettext_lazy as _

from .persoon import Persoon


class Overlijden(models.Model):
    persoon = models.ForeignKey(Persoon, null=True, on_delete=models.CASCADE)
    datum_overlijden = models.CharField(
        _("Datum overlijden"), max_length=200, blank=True
    )
    plaats_overlijden = models.CharField(
        _("Plaats overlijden"), max_length=200, blank=True
    )
    land_overlijden = models.CharField(_("Land overlijden"), max_length=200, blank=True)
    registergemeente_akte_waaraan_gegevens = models.CharField(
        _("Registergemeente akte waaraan gegevens over overlijden ontleend zijn"),
        max_length=200,
        blank=True,
    )
    aktenummer_van_de_akte_waaraan_gegevens = models.CharField(
        _("Aktenummer van de akte waaraan gegevens over overlijden ontleend zijn"),
        max_length=200,
        blank=True,
    )
    gemeente_waar_de_gegevens_over_overlijden = models.CharField(
        _("Gemeente waar de gegevens over overlijden aan het document ontleend zijn"),
        max_length=200,
        blank=True,
    )
    datum_van_de_ontlening_van_de_gegevens_over_overlijden = models.CharField(
        _("Datum van de ontlening van de gegevens over overlijden"),
        max_length=200,
        blank=True,
    )
    beschrijving_van_het_document_waaraan_de_gegevens = models.CharField(
        _(
            "Beschrijving van het document waaraan de gegevens over overlijden ontleend zijn"
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
    indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde = models.CharField(
        _("Indicatie onjuist dan wel strijdigheid met de openbare orde"),
        max_length=200,
        blank=True,
    )
    ingangsdatum_geldigheid_met_betrekking = models.CharField(
        _(
            "Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Overlijden"
        ),
        max_length=200,
        blank=True,
    )
    datum_van_opneming_met_betrekking = models.CharField(
        _(
            "Datum van opneming met betrekking tot de elementen van de categorie Overlijden"
        ),
        max_length=200,
        blank=True,
    )
    rni_deelnemer = models.CharField(_("RNI-deelnemer"), max_length=200, blank=True)
