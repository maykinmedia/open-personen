from django.db import models
from django.utils.translation import gettext_lazy as _

from .persoon import Persoon


class Inschrijving(models.Model):
    persoon = models.ForeignKey(Persoon, null=True, on_delete=models.CASCADE)
    datum_ingang_blokkering_pl = models.CharField(
        _("Datum ingang blokkering PL"), max_length=200, blank=True
    )
    datum_opschorting_bijhouding = models.CharField(
        _("Datum opschorting bijhouding"), max_length=200, blank=True
    )
    omschrijving_reden_opschorting_bijhouding = models.CharField(
        _("Omschrijving reden opschorting bijhouding"), max_length=200, blank=True
    )
    datum_eerste_inschrijving_gba_rni = models.CharField(
        _("Datum eerste inschrijving GBA/RNI"), max_length=200, blank=True
    )
    gemeente_waar_de_pk_zich_bevindt = models.CharField(
        _("Gemeente waar de PK zich bevindt"), max_length=200, blank=True
    )
    indicatie_geheim = models.CharField(
        _("Indicatie geheim"), max_length=200, blank=True
    )
    datum_verfificatie = models.CharField(
        _("Datum verfificatie"), max_length=200, blank=True
    )
    omschrijving_verificatie = models.CharField(
        _("Omschrijving verificatie"), max_length=200, blank=True
    )
    versienummer = models.CharField(_("Versienummer"), max_length=200, blank=True)
    datumtijdstempel = models.CharField(
        _("Datumtijdstempel"), max_length=200, blank=True
    )
    pk_gegevens_volledig_meegeconverteerd = models.CharField(
        _("PK-gegevens volledig meegeconverteerd"), max_length=200, blank=True
    )
    rni_deelnemer = models.CharField(_("RNI-deelnemer"), max_length=200, blank=True)
    omschrijving_verdrag = models.CharField(
        _("Omschrijving verdrag"), max_length=200, blank=True
    )
