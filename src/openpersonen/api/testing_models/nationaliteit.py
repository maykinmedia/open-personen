from django.db import models
from django.utils.translation import gettext_lazy as _

from .persoon import Persoon


class Nationaliteit(models.Model):
    persoon = models.ForeignKey(Persoon, null=True, on_delete=models.CASCADE)
    nationaliteit = models.CharField(
        _("Nationaliteit"), max_length=200, blank=True, help_text="Four digit code"
    )
    reden_opname_nationaliteit = models.CharField(
        _("Reden opname nationaliteit"),
        max_length=3,
        blank=True,
        help_text="Three digit code",
    )
    reden_beeindigen_nationaliteit = models.CharField(
        _("Reden beëindigen nationaliteit"),
        max_length=3,
        blank=True,
        help_text="Three digit code",
    )
    aanduiding_bijzonder_nederlanderschap = models.CharField(
        _("Aanduiding bijzonder Nederlanderschap"), max_length=200, blank=True
    )
    eu_persoonsummer = models.CharField(
        _("EU-persoonsummer"), max_length=200, blank=True
    )
    gemeente_waar_de_gegevens_over_nationaliteit = models.CharField(
        _(
            "Gemeente waar de gegevens over nationaliteit aan het document ontleend dan wel afgeleid zijn"
        ),
        max_length=200,
        blank=True,
        help_text="Four digit code",
    )
    datum_van_de_ontlening = models.CharField(
        _(
            "Datum van de ontlening dan wel afleiding van de gegevens over nationaliteit"
        ),
        max_length=200,
        blank=True,
        help_text="Format YYYYMMDD",
    )
    beschrijving_van_het_document = models.CharField(
        _(
            "Beschrijving van het document waaraan de gegevens over nationaliteit ontleend dan wel afgeleid zijn"
        ),
        max_length=200,
        blank=True,
    )
    aanduiding_gegevens_in_onderzoek = models.CharField(
        _("Aanduiding gegevens in onderzoek"), max_length=200, blank=True
    )
    datum_ingang_onderzoek = models.CharField(
        _("Datum ingang onderzoek"),
        max_length=200,
        blank=True,
        help_text="Format YYYYMMDD",
    )
    datum_einde_onderzoek = models.CharField(
        _("Datum einde onderzoek"),
        max_length=200,
        blank=True,
        help_text="Format YYYYMMDD",
    )
    indicatie_onjuist = models.CharField(
        _("Indicatie onjuist"), max_length=200, blank=True
    )
    datum_van_ingang_geldigheid_met_betrekking = models.CharField(
        _(
            "Datum van ingang geldigheid met betrekking tot de elementen van de categorie Nationaliteit"
        ),
        max_length=200,
        blank=True,
        help_text="Format YYYYMMDD",
    )
    datum_van_opneming_met_betrekking = models.CharField(
        _(
            "Datum van opneming met betrekking tot de elementen van de categorie Nationaliteit"
        ),
        max_length=200,
        blank=True,
        help_text="Format YYYYMMDD",
    )
    rni_deelnemer = models.CharField(_("RNI-deelnemer"), max_length=200, blank=True)
    omschrijving_verdrag = models.CharField(
        _("Omschrijving verdrag"), max_length=200, blank=True
    )
