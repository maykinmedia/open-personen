from django.db import models
from django.utils.translation import gettext_lazy as _

from .persoon import Persoon


class Kind(models.Model):
    persoon = models.ForeignKey(Persoon, null=True, on_delete=models.CASCADE)
    a_nummer_kind = models.CharField(_("A-nummer kind"), max_length=200, blank=True)
    burgerservicenummer_kind = models.CharField(
        _("Burgerservicenummer kind"), max_length=200, blank=True
    )
    voornamen_kind = models.CharField(_("Voornamen kind"), max_length=200, blank=True)
    adellijke_titel_predikaat_kind = models.CharField(
        _("Adellijke titel/predikaat kind"), max_length=200, blank=True
    )
    voorvoegsel_geslachtsnaam_kind = models.CharField(
        _("Voorvoegsel geslachtsnaam kind"), max_length=200, blank=True
    )
    geslachtsnaam_kind = models.CharField(
        _("Geslachtsnaam kind"), max_length=200, blank=True
    )
    geboortedatum_kind = models.CharField(
        _("Geboortedatum kind"), max_length=200, blank=True
    )
    geboorteplaats_kind = models.CharField(
        _("Geboorteplaats kind"), max_length=200, blank=True
    )
    geboorteland_kind = models.CharField(
        _("Geboorteland kind"), max_length=200, blank=True
    )
    registergemeente_akte_waaraan_gegevens_over_kind_ontleend_zijn = models.CharField(
        _("Registergemeente akte waaraan gegevens over kind ontleend zijn"),
        max_length=200,
        blank=True,
    )
    aktenummer_van_de_akte_waaraan_gegevens_over_kind_ontleend_zijn = models.CharField(
        _("Aktenummer van de akte waaraan gegevens over kind ontleend zijn"),
        max_length=200,
        blank=True,
    )
    gemeente_waar_de_gegevens_over_kind = models.CharField(
        _("Gemeente waar de gegevens over kind aan het document ontleend zijn"),
        max_length=200,
        blank=True,
    )
    datum_van_de_ontlening_van_de_gegevens_over_kind = models.CharField(
        _("Datum van de ontlening van de gegevens over kind"),
        max_length=200,
        blank=True,
    )
    beschrijving_van_het_document = models.CharField(
        _("Beschrijving van het document waaraan de gegevens over kind ontleend zijn"),
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
            "Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Kind"
        ),
        max_length=200,
        blank=True,
    )
    datum_van_opneming_met_betrekking = models.CharField(
        _("Datum van opneming met betrekking tot de elementen van de categorie Kind"),
        max_length=200,
        blank=True,
    )
    registratie_betrekking = models.CharField(
        _("Registratie betrekking"), max_length=200, blank=True
    )
