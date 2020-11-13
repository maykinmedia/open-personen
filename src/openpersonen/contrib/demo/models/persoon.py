from django.db import models
from django.utils.translation import gettext_lazy as _


class Persoon(models.Model):
    a_nummer_persoon = models.CharField(
        _("A-nummer persoon"), max_length=200, blank=True
    )
    burgerservicenummer_persoon = models.CharField(
        _("Burgerservicenummer persoon"), max_length=200, blank=True
    )
    voornamen_persoon = models.CharField(
        _("Voornamen persoon"), max_length=200, blank=True
    )
    adellijke_titel_predikaat_persoon = models.CharField(
        _("Adellijke titel/predikaat persoon"), max_length=200, blank=True
    )
    voorvoegsel_geslachtsnaam_persoon = models.CharField(
        _("Voorvoegsel geslachtsnaam persoon"), max_length=200, blank=True
    )
    geslachtsnaam_persoon = models.CharField(
        _("Geslachtsnaam persoon"), max_length=200, blank=True
    )
    geboortedatum_persoon = models.CharField(
        _("Geboortedatum persoon"),
        max_length=200,
        blank=True,
        help_text="Format YYYYMMDD",
    )
    geboorteplaats_persoon = models.CharField(
        _("Geboorteplaats persoon"), max_length=200, blank=True
    )
    geboorteland_persoon = models.CharField(
        _("Geboorteland persoon"),
        max_length=200,
        blank=True,
        help_text="Four digit code",
    )
    geslachtsaanduiding = models.CharField(
        _("Geslachtsaanduiding"),
        max_length=1,
        blank=True,
        help_text="M for mannen and V for vrouwen",
    )
    vorig_a_nummer = models.CharField(_("Vorig A-nummer"), max_length=200, blank=True)
    volgend_a_nummer = models.CharField(
        _("Volgend A-nummer"), max_length=200, blank=True
    )
    aanduiding_naamgebruik = models.CharField(
        _("Aanduiding naamgebruik"), max_length=1, blank=True
    )
    registergemeente_akte_waaraan_gegevens = models.CharField(
        _("Registergemeente akte waaraan gegevens over persoon ontleend zijn"),
        max_length=200,
        blank=True,
        help_text="Four digit code",
    )
    aktenummer_van_de_akte = models.CharField(
        _("Aktenummer van de akte waaraan gegevens over persoon ontleend zijn"),
        max_length=7,
        blank=True,
    )
    gemeente_waar_de_gegevens_over_persoon = models.CharField(
        _("Gemeente waar de gegevens over persoon aan het document ontleend zijn"),
        max_length=200,
        blank=True,
        help_text="Four digit code",
    )
    datum_van_de_ontlening_van_de_gegevens_over_persoon = models.CharField(
        _("Datum van de ontlening van de gegevens over persoon"),
        max_length=200,
        blank=True,
        help_text="Format YYYYMMDD",
    )
    beschrijving_van_het_document = models.CharField(
        _(
            "Beschrijving van het document waaraan de gegevens over persoon ontleend zijn"
        ),
        max_length=200,
        blank=True,
    )
    aanduiding_gegevens_in_onderzoek = models.CharField(
        _("Aanduiding gegevens in onderzoek"),
        max_length=6,
        blank=True,
        help_text="Six digit code",
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
    indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde = models.CharField(
        _("Indicatie onjuist dan wel strijdigheid met de openbare orde"),
        max_length=200,
        blank=True,
    )
    ingangsdatum_geldigheid_met_betrekking = models.CharField(
        _(
            "Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Persoon"
        ),
        max_length=200,
        blank=True,
        help_text="Format YYYYMMDD",
    )
    datum_van_opneming_met_betrekking = models.CharField(
        _(
            "Datum van opneming met betrekking tot de elementen van de categorie Persoon"
        ),
        max_length=200,
        blank=True,
        help_text="Format YYYYMMDD",
    )
    rni_deelnemer = models.CharField(_("RNI-deelnemer"), max_length=200, blank=True)

    class Meta:
        verbose_name = "Persoon"
        verbose_name_plural = "Personen"
