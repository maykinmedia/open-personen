from django.db import models
from django.utils.translation import gettext_lazy as _

from .persoon import Persoon


class Reisdocument(models.Model):
    persoon = models.ForeignKey(Persoon, null=True, on_delete=models.CASCADE)
    soort_nederlands_reisdocument = models.CharField(
        _("Soort Nederlands reisdocument"), max_length=200, blank=True
    )
    nummer_nederlands_reisdocument = models.CharField(
        _("Nummer Nederlands reisdocument"), max_length=200, blank=True
    )
    datum_uitgifte_nederlands_reisdocument = models.CharField(
        _("Datum uitgifte Nederlands reisdocument"), max_length=200, blank=True
    )
    autoriteit_van_afgifte_nederlands_reisdocument = models.CharField(
        _("Autoriteit van afgifte Nederlands reisdocument"), max_length=200, blank=True
    )
    datum_einde_geldigheid_nederlands_reisdocument = models.CharField(
        _("Datum einde geldigheid Nederlands reisdocument"), max_length=200, blank=True
    )
    datum_inhouding_dan_wel_vermissing_nederlands_reisdocument = models.CharField(
        _("Datum inhouding dan wel vermissing Nederlands reisdocument"),
        max_length=200,
        blank=True,
    )
    aanduiding_inhouding_dan_wel_vermissing_nederlands_reisdocument = models.CharField(
        _("Aanduiding inhouding dan wel vermissing Nederlands reisdocument"),
        max_length=200,
        blank=True,
    )
    signalering_met_betrekking = models.CharField(
        _("Signalering met betrekking tot verstrekken Nederlands reisdocument"),
        max_length=200,
        blank=True,
    )
    gemeente_waar_het_paspoortdossier_zich_bevindt = models.CharField(
        _("Gemeente waar het paspoortdossier zich bevindt"), max_length=200, blank=True
    )
    datum_van_opname_in_het_paspoortdossier = models.CharField(
        _("Datum van opname in het paspoortdossier"), max_length=200, blank=True
    )
    beschrijving_dossier = models.CharField(
        _("Beschrijving dossier waarin de aanvullende paspoortgegevens zich bevinden"),
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
    datum_van_ingang_geldigheid_met_betrekking = models.CharField(
        _(
            "Datum van ingang geldigheid met betrekking tot de elementen van de categorie Reisdocument"
        ),
        max_length=200,
        blank=True,
    )
    datum_van_opneming_met_betrekking = models.CharField(
        _(
            "Datum van opneming met betrekking tot de elementen van de categorie Reisdocument"
        ),
        max_length=200,
        blank=True,
    )
