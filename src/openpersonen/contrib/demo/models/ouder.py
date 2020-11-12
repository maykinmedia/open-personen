from django.db import models
from django.utils.translation import gettext_lazy as _

from .persoon import Persoon


class Ouder(models.Model):
    persoon = models.ForeignKey(Persoon, null=True, on_delete=models.CASCADE)
    a_nummer_ouder = models.CharField(_("A-nummer ouder"), max_length=200, blank=True)
    burgerservicenummer_ouder = models.CharField(
        _("Burgerservicenummer ouder"), max_length=200, blank=True
    )
    voornamen_ouder = models.CharField(_("Voornamen ouder"), max_length=200, blank=True)
    adellijke_titel_predikaat_ouder = models.CharField(
        _("Adellijke titel/predikaat ouder"), max_length=200, blank=True
    )
    voorvoegsel_geslachtsnaam_ouder = models.CharField(
        _("Voorvoegsel geslachtsnaam ouder"), max_length=200, blank=True
    )
    geslachtsnaam_ouder = models.CharField(
        _("Geslachtsnaam ouder"), max_length=200, blank=True
    )
    geboortedatum_ouder = models.CharField(
        _("Geboortedatum ouder"),
        max_length=200,
        blank=True,
        help_text="Format YYYYMMDD",
    )
    geboorteplaats_ouder = models.CharField(
        _("Geboorteplaats ouder"), max_length=200, blank=True
    )
    geboorteland_ouder = models.CharField(
        _("Geboorteland ouder"), max_length=200, blank=True, help_text="Four digit code"
    )
    geslachtsaanduiding_ouder = models.CharField(
        _("Geslachtsaanduiding ouder"),
        max_length=1,
        blank=True,
        help_text="M for mannen and V for vrouwen",
    )
    datum_ingang_familierechtelijke_betrekking_ouder = models.CharField(
        _("Datum ingang familierechtelijke betrekking ouder"),
        max_length=200,
        blank=True,
        help_text="Four digit code",
    )
    registergemeente_akte_waaraan_gegevens_over_ouder_ontleend_zijn = models.CharField(
        _("Registergemeente akte waaraan gegevens over ouder ontleend zijn"),
        max_length=200,
        blank=True,
        help_text="Four digit code",
    )
    aktenummer_van_de_akte_waaraan_gegevens = models.CharField(
        _("Aktenummer van de akte waaraan gegevens over ouder ontleend zijn"),
        max_length=200,
        blank=True,
    )
    gemeente_waar_de_gegevens_over_ouder = models.CharField(
        _("Gemeente waar de gegevens over ouder aan het document ontleend zijn"),
        max_length=200,
        blank=True,
        help_text="Four digit code",
    )
    datum_van_de_ontlening_van_de_gegevens_over_ouder = models.CharField(
        _("Datum van de ontlening van de gegevens over ouder"),
        max_length=200,
        blank=True,
    )
    beschrijving_van_het_document_waaraan_de_gegevens = models.CharField(
        _("Beschrijving van het document waaraan de gegevens over ouder ontleend zijn"),
        max_length=200,
        blank=True,
    )
    aanduiding_gegevens_in_onderzoek = models.CharField(
        _("Aanduiding gegevens in onderzoek"), max_length=200, blank=True
    )
    datum_ingang_onderzoek = models.CharField(
        _("Datum ingang onderzoek"),
        max_length=200,
        help_text="Format YYYYMMDD",
        blank=True,
    )
    datum_einde_onderzoek = models.CharField(
        _("Datum einde onderzoek"),
        max_length=200,
        help_text="Format YYYYMMDD",
        blank=True,
    )
    indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde = models.CharField(
        _("Indicatie onjuist dan wel strijdigheid met de openbare orde"),
        max_length=1,
        blank=True,
        help_text="One digit code",
    )
    ingangsdatum_geldigheid_met_betrekking = models.CharField(
        _(
            "Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Ouder"
        ),
        max_length=200,
        help_text="Format YYYYMMDD",
        blank=True,
    )
    datum_van_opneming_met_betrekking = models.CharField(
        _("Datum van opneming met betrekking tot de elementen van de categorie Ouder"),
        max_length=200,
        help_text="Format YYYYMMDD",
        blank=True,
    )

    class Meta:
        verbose_name = "Ouder"
        verbose_name_plural = "Ouders"
