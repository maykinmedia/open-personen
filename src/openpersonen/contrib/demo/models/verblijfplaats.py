from django.db import models
from django.utils.translation import gettext_lazy as _

from .persoon import Persoon


class Verblijfplaats(models.Model):
    persoon = models.ForeignKey(Persoon, null=True, on_delete=models.CASCADE)
    gemeente_van_inschrijving = models.CharField(
        _("Gemeente van inschrijving"), max_length=200, blank=True
    )
    datum_inschrijving_in_de_gemeente = models.CharField(
        _("Datum inschrijving in de gemeente"), max_length=200, blank=True
    )
    functie_adres = models.CharField(_("Functie adres"), max_length=200, blank=True)
    gemeentedeel = models.CharField(_("Gemeentedeel"), max_length=200, blank=True)
    datum_aanvang_adreshouding = models.CharField(
        _("Datum aanvang adreshouding"), max_length=200, blank=True
    )
    straatnaam = models.CharField(_("Straatnaam"), max_length=200, blank=True)
    naam_openbare_ruimte = models.CharField(
        _("Naam openbare ruimte"), max_length=200, blank=True
    )
    huisnummer = models.CharField(_("Huisnummer"), max_length=200, blank=True)
    huisletter = models.CharField(_("Huisletter"), max_length=200, blank=True)
    huisnummertoevoeging = models.CharField(
        _("Huisnummertoevoeging"), max_length=200, blank=True
    )
    aanduiding_bij_huisnummer = models.CharField(
        _("Aanduiding bij huisnummer"), max_length=200, blank=True
    )
    postcode = models.CharField(_("Postcode"), max_length=200, blank=True)
    woonplaatsnaam = models.CharField(_("Woonplaatsnaam"), max_length=200, blank=True)
    identificatiecode_verblijfplaats = models.CharField(
        _("Identificatiecode verblijfplaats"), max_length=200, blank=True
    )
    identificatiecode_nummeraanduiding = models.CharField(
        _("Identificatiecode nummeraanduiding"), max_length=200, blank=True
    )
    locatiebeschrijving = models.CharField(
        _("Locatiebeschrijving"), max_length=200, blank=True
    )
    land_adres_buitenland = models.CharField(
        _("Land adres buitenland"), max_length=200, blank=True
    )
    datum_aanvang_adres_buitenland = models.CharField(
        _("Datum aanvang adres buitenland"), max_length=200, blank=True
    )
    regel_1_adres_buitenland = models.CharField(
        _("Regel 1 adres buitenland"), max_length=200, blank=True
    )
    regel_2_adres_buitenland = models.CharField(
        _("Regel 2 adres buitenland"), max_length=200, blank=True
    )
    regel_3_adres_buitenland = models.CharField(
        _("Regel 3 adres buitenland"), max_length=200, blank=True
    )
    land_vanwaar_ingeschreven = models.CharField(
        _("Land vanwaar ingeschreven"), max_length=200, blank=True
    )
    datum_vestiging_in_nederland = models.CharField(
        _("Datum vestiging in Nederland"), max_length=200, blank=True
    )
    omschrijving_van_de_aangifte_adreshouding = models.CharField(
        _("Omschrijving van de aangifte adreshouding"), max_length=200, blank=True
    )
    indicatie_document = models.CharField(
        _("Indicatie document"), max_length=200, blank=True
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
            "Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Verblijfplaats"
        ),
        max_length=200,
        blank=True,
    )
    datum_van_opneming_met_betrekking = models.CharField(
        _(
            "Datum van opneming met betrekking tot de elementen van de categorie Verblijfplaats"
        ),
        max_length=200,
        blank=True,
    )
    rni_deelnemer = models.CharField(_("RNI-deelnemer"), max_length=200, blank=True)
    omschrijving_verdrag = models.CharField(
        _("Omschrijving verdrag"), max_length=200, blank=True
    )
