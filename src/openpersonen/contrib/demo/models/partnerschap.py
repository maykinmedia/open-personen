from django.db import models
from django.utils.translation import gettext_lazy as _

from .persoon import Persoon


class Partnerschap(models.Model):
    persoon = models.ForeignKey(Persoon, null=True, on_delete=models.CASCADE)
    a_nummer_echtgenoot_geregistreerd_partner = models.CharField(
        _("A-nummer echtgenoot/geregistreerd partner"), max_length=200, blank=True
    )
    burgerservicenummer_echtgenoot_geregistreerd_partner = models.CharField(
        _("Burgerservicenummer echtgenoot/geregistreerd partner"),
        max_length=200,
        blank=True,
    )
    voornamen_echtgenoot_geregistreerd_partner = models.CharField(
        _("Voornamen echtgenoot/geregistreerd partner"), max_length=200, blank=True
    )
    adellijke_titel_predikaat_echtgenoot_geregistreerd_partner = models.CharField(
        _("Adellijke titel/predikaat echtgenoot/geregistreerd partner"),
        max_length=200,
        blank=True,
    )
    voorvoegsel_geslachtsnaam_echtgenoot_geregistreerd_partner = models.CharField(
        _("Voorvoegsel geslachtsnaam echtgenoot/geregistreerd partner"),
        max_length=200,
        blank=True,
    )
    geslachtsnaam_echtgenoot_geregistreerd_partner = models.CharField(
        _("Geslachtsnaam echtgenoot/geregistreerd partner"), max_length=200, blank=True
    )
    geboortedatum_echtgenoot_geregistreerd_partner = models.CharField(
        _("Geboortedatum echtgenoot/geregistreerd partner"), max_length=200, blank=True
    )
    geboorteplaats_echtgenoot_geregistreerd_partner = models.CharField(
        _("Geboorteplaats echtgenoot/geregistreerd partner"), max_length=200, blank=True
    )
    geboorteland_echtgenoot_geregistreerd_partner = models.CharField(
        _("Geboorteland echtgenoot/geregistreerd partner"), max_length=200, blank=True
    )
    geslachtsaanduiding_echtgenoot_geregistreerd_partner = models.CharField(
        _("Geslachtsaanduiding echtgenoot/geregistreerd partner"),
        max_length=200,
        blank=True,
    )
    datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap = models.CharField(
        _("Datum huwelijkssluiting/aangaan geregistreerd partnerschap"),
        max_length=200,
        blank=True,
    )
    plaats_huwelijkssluiting_aangaan_geregistreerd_partnerschap = models.CharField(
        _("Plaats huwelijkssluiting/aangaan geregistreerd partnerschap"),
        max_length=200,
        blank=True,
    )
    land_huwelijkssluiting_aangaan_geregistreerd_partnerschap = models.CharField(
        _("Land huwelijkssluiting/aangaan geregistreerd partnerschap"),
        max_length=200,
        blank=True,
    )
    datum_ontbinding_huwelijk_geregistreerd_partnerschap = models.CharField(
        _("Datum ontbinding huwelijk/geregistreerd partnerschap"),
        max_length=200,
        blank=True,
    )
    plaats_ontbinding_huwelijk_geregistreerd_partnerschap = models.CharField(
        _("Plaats ontbinding huwelijk/geregistreerd partnerschap"),
        max_length=200,
        blank=True,
    )
    land_ontbinding_huwelijk_geregistreerd_partnerschap = models.CharField(
        _("Land ontbinding huwelijk/geregistreerd partnerschap"),
        max_length=200,
        blank=True,
    )
    reden_ontbinding_huwelijk_geregistreerd_partnerschap = models.CharField(
        _("Reden ontbinding huwelijk/geregistreerd partnerschap"),
        max_length=200,
        blank=True,
    )
    soort_verbintenis = models.CharField(
        _("Soort verbintenis"), max_length=200, blank=True
    )
    registergemeente_akte_waaraan_gegevens = models.CharField(
        _(
            "Registergemeente akte waaraan gegevens over huwelijk/geregistreerd partnerschap ontleend zijn"
        ),
        max_length=200,
        blank=True,
    )
    aktenummer_van_de_akte_waaraan_gegevens = models.CharField(
        _(
            "Aktenummer van de akte waaraan gegevens over huwelijk/geregistreerd partnerschap ontleend zijn"
        ),
        max_length=200,
        blank=True,
    )
    gemeente_waar_de_gegevens_over_huwelijk = models.CharField(
        _(
            "Gemeente waar de gegevens over huwelijk/geregistreerd partnerschap aan het document ontleend zijn"
        ),
        max_length=200,
        blank=True,
    )
    datum_van_de_ontlening_van_de_gegevens = models.CharField(
        _(
            "Datum van de ontlening van de gegevens over huwelijk/geregistreerd partnerschap"
        ),
        max_length=200,
        blank=True,
    )
    beschrijving_van_het_document_waaraan_de_gegevens = models.CharField(
        _(
            "Beschrijving van het document waaraan de gegevens over huwelijk/ geregistreerd partnerschap ontleend zijn"
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
            "Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Huwelijk/geregistreerd part"
        ),
        max_length=200,
        blank=True,
    )
    datum_van_opneming_met_betrekking = models.CharField(
        _(
            "Datum van opneming met betrekking tot de elementen van de categorie Huwelijk/geregistreerd partnersc"
        ),
        max_length=200,
        blank=True,
    )
