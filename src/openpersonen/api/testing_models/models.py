from django.db import models
from django.utils.translation import gettext_lazy as _


class Persoon(models.Model):
    a_nummer_persoon = models.IntegerField(_("A-nummer persoon"), max_length=10, blank=True)
    burgerservicenummer_persoon = models.IntegerField(_("Burgerservicenummer persoon"), max_length=9, blank=True)
    voornamen_persoon = models.CharField(_("Voornamen persoon"), max_length=200, blank=True)
    adellijke_titel_predikaat_persoon = models.CharField(_("Adellijke titel/predikaat persoon"), max_length=200,
                                                           blank=True)
    voorvoegsel_geslachtsnaam_persoon = models.CharField(_("Voorvoegsel geslachtsnaam persoon"), max_length=200,
                                                         blank=True)
    geslachtsnaam_persoon = models.CharField(_("Geslachtsnaam persoon"), max_length=200, blank=True)
    geboortedatum_persoon = models.IntegerField(_("Geboortedatum persoon"), max_length=8, blank=True,
                                                help_text='Format YYYYMMDD')
    geboorteplaats_persoon = models.CharField(_("Geboorteplaats persoon"), max_length=200, blank=True)
    geboorteland_persoon = models.IntegerField(_("Geboorteland persoon"), max_length=4, blank=True,
                                               help_text='Four digit code')
    geslachtsaanduiding = models.CharField(_("Geslachtsaanduiding"), max_length=1, blank=True,
                                           help_text='M for mannen and V for vrouwen')
    vorig_a_nummer = models.IntegerField(_("Vorig A-nummer"), max_length=10, blank=True)
    volgend_a_nummer = models.IntegerField(_("Volgend A-nummer"), max_length=10, blank=True)
    aanduiding_naamgebruik = models.CharField(_("Aanduiding naamgebruik"), max_length=1, blank=True)
    registergemeente_akte_waaraan_gegevens_over_persoon_ontleend_zijn = models.CharField(
        _("Registergemeente akte waaraan gegevens over persoon ontleend zijn"), max_length=4, blank=True,
        help_text='Four digit code')
    aktenummer_van_de_akte_waaraan_gegevens_over_persoon_ontleend_zijn = models.CharField(
        _("Aktenummer van de akte waaraan gegevens over persoon ontleend zijn"), max_length=7, blank=True)
    gemeente_waar_de_gegevens_over_persoon_aan_het_document_ontleend_zijn = models.CharField(
        _("Gemeente waar de gegevens over persoon aan het document ontleend zijn"), max_length=4, blank=True,
        help_text='Four digit code')
    datum_van_de_ontlening_van_de_gegevens_over_persoon = models.IntegerField(
        _("Datum van de ontlening van de gegevens over persoon"), max_length=8, blank=True, help_text='Format YYYYMMDD')
    beschrijving_van_het_document_waaraan_de_gegevens_over_persoon_ontleend_zijn = models.CharField(
        _("Beschrijving van het document waaraan de gegevens over persoon ontleend zijn"), max_length=200, blank=True)
    aanduiding_gegevens_in_onderzoek = models.IntegerField(_("Aanduiding gegevens in onderzoek"), max_length=6,
                                                        blank=True, help_text='Six digit code')
    datum_ingang_onderzoek = models.IntegerField(_("Datum ingang onderzoek"), max_length=8, blank=True,
                                                 help_text='Format YYYYMMDD')
    datum_einde_onderzoek = models.IntegerField(_("Datum einde onderzoek"), max_length=8, blank=True,
                                                help_text='Format YYYYMMDD')
    indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde = models.CharField(
        _("Indicatie onjuist dan wel strijdigheid met de openbare orde"), max_length=200, blank=True)
    ingangsdatum_geldigheid_met_betrekking_tot_de_elementen_van_de_categorie_persoon = models.IntegerField(
        _("Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Persoon"), max_length=8,
        blank=True, help_text='Format YYYYMMDD')
    datum_van_opneming_met_betrekking_tot_de_elementen_van_de_categorie_persoon = models.IntegerField(
        _("Datum van opneming met betrekking tot de elementen van de categorie Persoon"), max_length=8, blank=True,
        help_text='Format YYYYMMDD')
    rni_deelnemer = models.CharField(_("RNI-deelnemer"), max_length=200, blank=True)


class Ouder(models.Model):
    omschrijving_verdrag = models.CharField(_("Omschrijving verdrag"), max_length=200, blank=True)
    a_nummer_ouder = models.IntegerField(_("A-nummer ouder"), max_length=10, blank=True)
    burgerservicenummer_ouder = models.IntegerField(_("Burgerservicenummer ouder"), max_length=9, blank=True)
    voornamen_ouder = models.CharField(_("Voornamen ouder"), max_length=200, blank=True)
    adellijke_titel_predikaat_ouder = models.CharField(_("Adellijke titel/predikaat ouder"), max_length=200,
                                                          blank=True)
    voorvoegsel_geslachtsnaam_ouder = models.CharField(_("Voorvoegsel geslachtsnaam ouder"), max_length=200,
                                                        blank=True)
    geslachtsnaam_ouder = models.CharField(_("Geslachtsnaam ouder"), max_length=200, blank=True)
    geboortedatum_ouder = models.IntegerField(_("Geboortedatum ouder"), max_length=8, blank=True,
                                              help_text='Format YYYYMMDD')
    geboorteplaats_ouder = models.CharField(_("Geboorteplaats ouder"), max_length=200, blank=True)
    geboorteland_ouder = models.IntegerField(_("Geboorteland ouder"), max_length=4, blank=True,
                                             help_text='Four digit code')
    geslachtsaanduiding_ouder = models.CharField(_("Geslachtsaanduiding ouder"), max_length=1, blank=True,
                                                 help_text='M for mannen and V for vrouwen')
    datum_ingang_familierechtelijke_betrekking_ouder = models.IntegerField(
        _("Datum ingang familierechtelijke betrekking ouder"), max_length=4, blank=True, help_text='Four digit code')
    registergemeente_akte_waaraan_gegevens_over_ouder_ontleend_zijn = models.IntegerField(
        _("Registergemeente akte waaraan gegevens over ouder ontleend zijn"), max_length=4, blank=True,
        help_text='Four digit code')
    aktenummer_van_de_akte_waaraan_gegevens_over_ouder_ontleend_zijn = models.CharField(
        _("Aktenummer van de akte waaraan gegevens over ouder ontleend zijn"), max_length=200, blank=True)
    gemeente_waar_de_gegevens_over_ouder_aan_het_document_ontleend_zijn = models.IntegerField(
        _("Gemeente waar de gegevens over ouder aan het document ontleend zijn"), max_length=4, blank=True,
        help_text='Four digit code')
    datum_van_de_ontlening_van_de_gegevens_over_ouder = models.IntegerField(
        _("Datum van de ontlening van de gegevens over ouder"), max_length=200, blank=True)
    beschrijving_van_het_document_waaraan_de_gegevens_over_ouder_ontleend_zijn = models.CharField(
        _("Beschrijving van het document waaraan de gegevens over ouder ontleend zijn"), max_length=200, blank=True)
    aanduiding_gegevens_in_onderzoek = models.CharField(_("Aanduiding gegevens in onderzoek"), max_length=200,
                                                        blank=True)
    datum_ingang_onderzoek = models.IntegerField(_("Datum ingang onderzoek"), max_length=8, help_text='Format YYYYMMDD',
                                                 blank=True)
    datum_einde_onderzoek = models.IntegerField(_("Datum einde onderzoek"), max_length=8, help_text='Format YYYYMMDD',
                                                blank=True)
    indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde = models.CharField(
        _("Indicatie onjuist dan wel strijdigheid met de openbare orde"), max_length=1, blank=True,
        help_text='One digit code')
    ingangsdatum_geldigheid_met_betrekking_tot_de_elementen_van_de_categorie_ouder = models.IntegerField(
        _("Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Ouder"), max_length=8,
        help_text='Format YYYYMMDD',
        blank=True)
    datum_van_opneming_met_betrekking_tot_de_elementen_van_de_categorie_ouder = models.IntegerField(
        _("Datum van opneming met betrekking tot de elementen van de categorie Ouder"), max_length=8,
        help_text='Format YYYYMMDD', blank=True)


class Nationaliteit(models.Model):
    nationaliteit = models.IntegerField(_("Nationaliteit"), max_length=4, blank=True, help_text='Four digit code')
    reden_opname_nationaliteit = models.IntegerField(_("Reden opname nationaliteit"), max_length=3, blank=True,
                                                     help_text='Three digit code')
    reden_beeindigen_nationaliteit = models.IntegerField(_("Reden beëindigen nationaliteit"), max_length=3, blank=True,
                                                         help_text='Three digit code')
    aanduiding_bijzonder_nederlanderschap = models.CharField(_("Aanduiding bijzonder Nederlanderschap"), max_length=200,
                                                             blank=True)
    eu_persoonsummer = models.CharField(_("EU-persoonsummer"), max_length=200, blank=True)
    gemeente_waar_de_gegevens_over_nationaliteit_aan_het_document_ontleend_dan_wel_afgeleid_zijn = models.IntegerField(
        _("Gemeente waar de gegevens over nationaliteit aan het document ontleend dan wel afgeleid zijn"),
        max_length=4, blank=True, help_text='Four digit code')
    datum_van_de_ontlening_dan_wel_afleiding_van_de_gegevens_over_nationaliteit = models.IntegerField(
        _("Datum van de ontlening dan wel afleiding van de gegevens over nationaliteit"), max_length=8, blank=True,
        help_text='Format YYYYMMDD')
    beschrijving_van_het_document_waaraan_de_gegevens_over_nationaliteit_ontleend_dan_wel_afgeleid_zijn = models.CharField(
        _("Beschrijving van het document waaraan de gegevens over nationaliteit ontleend dan wel afgeleid zijn"),
        max_length=200, blank=True)
    aanduiding_gegevens_in_onderzoek = models.CharField(_("Aanduiding gegevens in onderzoek"), max_length=200,
                                                        blank=True)
    datum_ingang_onderzoek = models.IntegerField(_("Datum ingang onderzoek"), max_length=8, blank=True,
                                                 help_text='Format YYYYMMDD')
    datum_einde_onderzoek = models.IntegerField(_("Datum einde onderzoek"), max_length=8, blank=True,
                                                 help_text='Format YYYYMMDD')
    indicatie_onjuist = models.CharField(_("Indicatie onjuist"), max_length=200, blank=True)
    datum_van_ingang_geldigheid_met_betrekking_tot_de_elementen_van_de_categorie_nationaliteit = models.IntegerField(
        _("Datum van ingang geldigheid met betrekking tot de elementen van de categorie Nationaliteit"), max_length=8,
        blank=True, help_text='Format YYYYMMDD')
    datum_van_opneming_met_betrekking_tot_de_elementen_van_de_categorie_nationaliteit = models.IntegerField(
        _("Datum van opneming met betrekking tot de elementen van de categorie Nationaliteit"), max_length=8,
        blank=True, help_text='Format YYYYMMDD')
    rni_deelnemer = models.CharField(_("RNI-deelnemer"), max_length=200, blank=True)
    omschrijving_verdrag = models.CharField(_("Omschrijving verdrag"), max_length=200, blank=True)


class Partnerschap(models):
    a_nummer_echtgenoot_geregistreerd_partner = models.CharField(_("A-nummer echtgenoot/geregistreerd partner"),
                                                                     max_length=200, blank=True)
    burgerservicenummer_echtgenoot_geregistreerd_partner = models.CharField(
        _("Burgerservicenummer echtgenoot/geregistreerd partner"), max_length=200, blank=True)
    voornamen_echtgenoot_geregistreerd_partner = models.CharField(_("Voornamen echtgenoot/geregistreerd partner"),
                                                                    max_length=200, blank=True)
    adellijke_titel_predikaat_echtgenoot_geregistreerd_partner = models.CharField(
        _("Adellijke titel/predikaat echtgenoot/geregistreerd partner"), max_length=200, blank=True)
    voorvoegsel_geslachtsnaam_echtgenoot_geregistreerd_partner = models.CharField(
        _("Voorvoegsel geslachtsnaam echtgenoot/geregistreerd partner"), max_length=200, blank=True)
    geslachtsnaam_echtgenoot_geregistreerd_partner = models.CharField(
        _("Geslachtsnaam echtgenoot/geregistreerd partner"), max_length=200, blank=True)
    geboortedatum_echtgenoot_geregistreerd_partner = models.CharField(
        _("Geboortedatum echtgenoot/geregistreerd partner"), max_length=200, blank=True)
    geboorteplaats_echtgenoot_geregistreerd_partner = models.CharField(
        _("Geboorteplaats echtgenoot/geregistreerd partner"), max_length=200, blank=True)
    geboorteland_echtgenoot_geregistreerd_partner = models.CharField(
        _("Geboorteland echtgenoot/geregistreerd partner"), max_length=200, blank=True)
    geslachtsaanduiding_echtgenoot_geregistreerd_partner = models.CharField(
        _("Geslachtsaanduiding echtgenoot/geregistreerd partner"), max_length=200, blank=True)
    datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap = models.CharField(
        _("Datum huwelijkssluiting/aangaan geregistreerd partnerschap"), max_length=200, blank=True)
    plaats_huwelijkssluiting_aangaan_geregistreerd_partnerschap = models.CharField(
        _("Plaats huwelijkssluiting/aangaan geregistreerd partnerschap"), max_length=200, blank=True)
    land_huwelijkssluiting_aangaan_geregistreerd_partnerschap = models.CharField(
        _("Land huwelijkssluiting/aangaan geregistreerd partnerschap"), max_length=200, blank=True)
    datum_ontbinding_huwelijk_geregistreerd_partnerschap = models.CharField(
        _("Datum ontbinding huwelijk/geregistreerd partnerschap"), max_length=200, blank=True)
    plaats_ontbinding_huwelijk_geregistreerd_partnerschap = models.CharField(
        _("Plaats ontbinding huwelijk/geregistreerd partnerschap"), max_length=200, blank=True)
    land_ontbinding_huwelijk_geregistreerd_partnerschap = models.CharField(
        _("Land ontbinding huwelijk/geregistreerd partnerschap"), max_length=200, blank=True)
    reden_ontbinding_huwelijk_geregistreerd_partnerschap = models.CharField(
        _("Reden ontbinding huwelijk/geregistreerd partnerschap"), max_length=200, blank=True)
    soort_verbintenis = models.CharField(_("Soort verbintenis"), max_length=200, blank=True)
    registergemeente_akte_waaraan_gegevens_over_huwelijk_geregistreerd_partnerschap_ontleend_zijn = models.CharField(
        _("Registergemeente akte waaraan gegevens over huwelijk/geregistreerd partnerschap ontleend zijn"),
        max_length=200, blank=True)
    aktenummer_van_de_akte_waaraan_gegevens_over_huwelijk_geregistreerd_partnerschap_ontleend_zijn = models.CharField(
        _("Aktenummer van de akte waaraan gegevens over huwelijk/geregistreerd partnerschap ontleend zijn"),
        max_length=200, blank=True)
    gemeente_waar_de_gegevens_over_huwelijk_geregistreerd_partnerschap_aan_het_document_ontleend_zijn = models.CharField(
        _("Gemeente waar de gegevens over huwelijk/geregistreerd partnerschap aan het document ontleend zijn"),
        max_length=200, blank=True)
    datum_van_de_ontlening_van_de_gegevens_over_huwelijk_geregistreerd_partnerschap = models.CharField(
        _("Datum van de ontlening van de gegevens over huwelijk/geregistreerd partnerschap"), max_length=200,
        blank=True)
    beschrijving_van_het_document_waaraan_de_gegevens_over_huwelijk__geregistreerd_partnerschap_ontleend_zijn = models.CharField(
        _("Beschrijving van het document waaraan de gegevens over huwelijk/ geregistreerd partnerschap ontleend zijn"),
        max_length=200, blank=True)
    aanduiding_gegevens_in_onderzoek = models.CharField(_("Aanduiding gegevens in onderzoek"), max_length=200,
                                                        blank=True)
    datum_ingang_onderzoek = models.CharField(_("Datum ingang onderzoek"), max_length=200, blank=True)
    datum_einde_onderzoek = models.CharField(_("Datum einde onderzoek"), max_length=200, blank=True)
    indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde = models.CharField(
        _("Indicatie onjuist dan wel strijdigheid met de openbare orde"), max_length=200, blank=True)
    ingangsdatum_geldigheid_met_betrekking_tot_de_elementen_van_de_categorie_huwelijk_geregistreerd_part = models.CharField(
        _("Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Huwelijk/geregistreerd part"),
        max_length=200, blank=True)
    datum_van_opneming_met_betrekking_tot_de_elementen_van_de_categorie_huwelijk_geregistreerd_partnersc = models.CharField(
        _("Datum van opneming met betrekking tot de elementen van de categorie Huwelijk/geregistreerd partnersc"),
        max_length=200, blank=True)


class Overlijden(models.Model):
    datum_overlijden = models.CharField(_("Datum overlijden"), max_length=200, blank=True)
    plaats_overlijden = models.CharField(_("Plaats overlijden"), max_length=200, blank=True)
    land_overlijden = models.CharField(_("Land overlijden"), max_length=200, blank=True)
    registergemeente_akte_waaraan_gegevens_over_overlijden_ontleend_zijn = models.CharField(
        _("Registergemeente akte waaraan gegevens over overlijden ontleend zijn"), max_length=200, blank=True)
    aktenummer_van_de_akte_waaraan_gegevens_over_overlijden_ontleend_zijn = models.CharField(
        _("Aktenummer van de akte waaraan gegevens over overlijden ontleend zijn"), max_length=200, blank=True)
    gemeente_waar_de_gegevens_over_overlijden_aan_het_document_ontleend_zijn = models.CharField(
        _("Gemeente waar de gegevens over overlijden aan het document ontleend zijn"), max_length=200, blank=True)
    datum_van_de_ontlening_van_de_gegevens_over_overlijden = models.CharField(
        _("Datum van de ontlening van de gegevens over overlijden"), max_length=200, blank=True)
    beschrijving_van_het_document_waaraan_de_gegevens_over_overlijden_ontleend_zijn = models.CharField(
        _("Beschrijving van het document waaraan de gegevens over overlijden ontleend zijn"), max_length=200,
        blank=True)
    aanduiding_gegevens_in_onderzoek = models.CharField(_("Aanduiding gegevens in onderzoek"), max_length=200,
                                                        blank=True)
    datum_ingang_onderzoek = models.CharField(_("Datum ingang onderzoek"), max_length=200, blank=True)
    datum_einde_onderzoek = models.CharField(_("Datum einde onderzoek"), max_length=200, blank=True)
    indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde = models.CharField(
        _("Indicatie onjuist dan wel strijdigheid met de openbare orde"), max_length=200, blank=True)
    ingangsdatum_geldigheid_met_betrekking_tot_de_elementen_van_de_categorie_overlijden = models.CharField(
        _("Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Overlijden"), max_length=200,
        blank=True)
    datum_van_opneming_met_betrekking_tot_de_elementen_van_de_categorie_overlijden = models.CharField(
        _("Datum van opneming met betrekking tot de elementen van de categorie Overlijden"), max_length=200, blank=True)
    rni_deelnemer = models.CharField(_("RNI-deelnemer"), max_length=200, blank=True)


class Inschrijving(models.Model):
    datum_ingang_blokkering_pl = models.CharField(_("Datum ingang blokkering PL"), max_length=200, blank=True)
    datum_opschorting_bijhouding = models.CharField(_("Datum opschorting bijhouding"), max_length=200, blank=True)
    omschrijving_reden_opschorting_bijhouding = models.CharField(_("Omschrijving reden opschorting bijhouding"),
                                                                 max_length=200, blank=True)
    datum_eerste_inschrijving_gba_rni = models.CharField(_("Datum eerste inschrijving GBA/RNI"), max_length=200,
                                                           blank=True)
    gemeente_waar_de_pk_zich_bevindt = models.CharField(_("Gemeente waar de PK zich bevindt"), max_length=200,
                                                        blank=True)
    indicatie_geheim = models.CharField(_("Indicatie geheim"), max_length=200, blank=True)
    datum_verfificatie = models.CharField(_("Datum verfificatie"), max_length=200, blank=True)
    omschrijving_verificatie = models.CharField(_("Omschrijving verificatie"), max_length=200, blank=True)
    versienummer = models.CharField(_("Versienummer"), max_length=200, blank=True)
    datumtijdstempel = models.CharField(_("Datumtijdstempel"), max_length=200, blank=True)
    pk_gegevens_volledig_meegeconverteerd = models.CharField(_("PK-gegevens volledig meegeconverteerd"),
                                                               max_length=200, blank=True)
    rni_deelnemer = models.CharField(_("RNI-deelnemer"), max_length=200, blank=True)
    omschrijving_verdrag = models.CharField(_("Omschrijving verdrag"), max_length=200, blank=True)


class Verblijfplaats(models.Model):
    gemeente_van_inschrijving = models.CharField(_("Gemeente van inschrijving"), max_length=200, blank=True)
    datum_inschrijving_in_de_gemeente = models.CharField(_("Datum inschrijving in de gemeente"), max_length=200,
                                                         blank=True)
    functie_adres = models.CharField(_("Functie adres"), max_length=200, blank=True)
    gemeentedeel = models.CharField(_("Gemeentedeel"), max_length=200, blank=True)
    datum_aanvang_adreshouding = models.CharField(_("Datum aanvang adreshouding"), max_length=200, blank=True)
    straatnaam = models.CharField(_("Straatnaam"), max_length=200, blank=True)
    naam_openbare_ruimte = models.CharField(_("Naam openbare ruimte"), max_length=200, blank=True)
    huisnummer = models.CharField(_("Huisnummer"), max_length=200, blank=True)
    huisletter = models.CharField(_("Huisletter"), max_length=200, blank=True)
    huisnummertoevoeging = models.CharField(_("Huisnummertoevoeging"), max_length=200, blank=True)
    aanduiding_bij_huisnummer = models.CharField(_("Aanduiding bij huisnummer"), max_length=200, blank=True)
    postcode = models.CharField(_("Postcode"), max_length=200, blank=True)
    woonplaatsnaam = models.CharField(_("Woonplaatsnaam"), max_length=200, blank=True)
    identificatiecode_verblijfplaats = models.CharField(_("Identificatiecode verblijfplaats"), max_length=200,
                                                        blank=True)
    identificatiecode_nummeraanduiding = models.CharField(_("Identificatiecode nummeraanduiding"), max_length=200,
                                                          blank=True)
    locatiebeschrijving = models.CharField(_("Locatiebeschrijving"), max_length=200, blank=True)
    land_adres_buitenland = models.CharField(_("Land adres buitenland"), max_length=200, blank=True)
    datum_aanvang_adres_buitenland = models.CharField(_("Datum aanvang adres buitenland"), max_length=200, blank=True)
    regel_1_adres_buitenland = models.CharField(_("Regel 1 adres buitenland"), max_length=200, blank=True)
    regel_2_adres_buitenland = models.CharField(_("Regel 2 adres buitenland"), max_length=200, blank=True)
    regel_3_adres_buitenland = models.CharField(_("Regel 3 adres buitenland"), max_length=200, blank=True)
    land_vanwaar_ingeschreven = models.CharField(_("Land vanwaar ingeschreven"), max_length=200, blank=True)
    datum_vestiging_in_nederland = models.CharField(_("Datum vestiging in Nederland"), max_length=200, blank=True)
    omschrijving_van_de_aangifte_adreshouding = models.CharField(_("Omschrijving van de aangifte adreshouding"),
                                                                 max_length=200, blank=True)
    indicatie_document = models.CharField(_("Indicatie document"), max_length=200, blank=True)
    aanduiding_gegevens_in_onderzoek = models.CharField(_("Aanduiding gegevens in onderzoek"), max_length=200,
                                                        blank=True)
    datum_ingang_onderzoek = models.CharField(_("Datum ingang onderzoek"), max_length=200, blank=True)
    datum_einde_onderzoek = models.CharField(_("Datum einde onderzoek"), max_length=200, blank=True)
    indicatie_onjuist = models.CharField(_("Indicatie onjuist"), max_length=200, blank=True)
    ingangsdatum_geldigheid_met_betrekking_tot_de_elementen_van_de_categorie_verblijfplaats = models.CharField(
        _("Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Verblijfplaats"), max_length=200,
        blank=True)
    datum_van_opneming_met_betrekking_tot_de_elementen_van_de_categorie_verblijfplaats = models.CharField(
        _("Datum van opneming met betrekking tot de elementen van de categorie Verblijfplaats"), max_length=200,
        blank=True)
    rni_deelnemer = models.CharField(_("RNI-deelnemer"), max_length=200, blank=True)
    omschrijving_verdrag = models.CharField(_("Omschrijving verdrag"), max_length=200, blank=True)


class Kind(models.Model):
    a_nummer_kind = models.CharField(_("A-nummer kind"), max_length=200, blank=True)
    burgerservicenummer_kind = models.CharField(_("Burgerservicenummer kind"), max_length=200, blank=True)
    voornamen_kind = models.CharField(_("Voornamen kind"), max_length=200, blank=True)
    adellijke_titel_predikaat_kind = models.CharField(_("Adellijke titel/predikaat kind"), max_length=200, blank=True)
    voorvoegsel_geslachtsnaam_kind = models.CharField(_("Voorvoegsel geslachtsnaam kind"), max_length=200, blank=True)
    geslachtsnaam_kind = models.CharField(_("Geslachtsnaam kind"), max_length=200, blank=True)
    geboortedatum_kind = models.CharField(_("Geboortedatum kind"), max_length=200, blank=True)
    geboorteplaats_kind = models.CharField(_("Geboorteplaats kind"), max_length=200, blank=True)
    geboorteland_kind = models.CharField(_("Geboorteland kind"), max_length=200, blank=True)
    registergemeente_akte_waaraan_gegevens_over_kind_ontleend_zijn = models.CharField(
        _("Registergemeente akte waaraan gegevens over kind ontleend zijn"), max_length=200, blank=True)
    aktenummer_van_de_akte_waaraan_gegevens_over_kind_ontleend_zijn = models.CharField(
        _("Aktenummer van de akte waaraan gegevens over kind ontleend zijn"), max_length=200, blank=True)
    gemeente_waar_de_gegevens_over_kind_aan_het_document_ontleend_zijn = models.CharField(
        _("Gemeente waar de gegevens over kind aan het document ontleend zijn"), max_length=200, blank=True)
    datum_van_de_ontlening_van_de_gegevens_over_kind = models.CharField(
        _("Datum van de ontlening van de gegevens over kind"), max_length=200, blank=True)
    beschrijving_van_het_document_waaraan_de_gegevens_over_kind_ontleend_zijn = models.CharField(
        _("Beschrijving van het document waaraan de gegevens over kind ontleend zijn"), max_length=200, blank=True)
    aanduiding_gegevens_in_onderzoek = models.CharField(_("Aanduiding gegevens in onderzoek"), max_length=200,
                                                        blank=True)
    datum_ingang_onderzoek = models.CharField(_("Datum ingang onderzoek"), max_length=200, blank=True)
    datum_einde_onderzoek = models.CharField(_("Datum einde onderzoek"), max_length=200, blank=True)
    indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde = models.CharField(
        _("Indicatie onjuist dan wel strijdigheid met de openbare orde"), max_length=200, blank=True)
    ingangsdatum_geldigheid_met_betrekking_tot_de_elementen_van_de_categorie_kind = models.CharField(
        _("Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Kind"), max_length=200, blank=True)
    datum_van_opneming_met_betrekking_tot_de_elementen_van_de_categorie_kind = models.CharField(
        _("Datum van opneming met betrekking tot de elementen van de categorie Kind"), max_length=200, blank=True)
    registratie_betrekking = models.CharField(_("Registratie betrekking"), max_length=200, blank=True)


class Verblijfstitel(models.Model):
    aanduiding_verblijfstitel = models.CharField(_("Aanduiding verblijfstitel"), max_length=200, blank=True)
    datum_einde_verblijfstitel = models.CharField(_("Datum einde verblijfstitel"), max_length=200, blank=True)
    ingangsdatum_verblijfstitel = models.CharField(_("Ingangsdatum verblijfstitel"), max_length=200, blank=True)
    aanduiding_gegevens_in_onderzoek = models.CharField(_("Aanduiding gegevens in onderzoek"), max_length=200,
                                                        blank=True)
    datum_ingang_onderzoek = models.CharField(_("Datum ingang onderzoek"), max_length=200, blank=True)
    datum_einde_onderzoek = models.CharField(_("Datum einde onderzoek"), max_length=200, blank=True)
    indicatie_onjuist = models.CharField(_("Indicatie onjuist"), max_length=200, blank=True)
    ingangsdatum_geldigheid_met_betrekking_tot_de_elementen_van_de_categorie_verblijfstitel = models.CharField(
        _("Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Verblijfstitel"), max_length=200,
        blank=True)
    datum_van_opneming_met_betrekking_tot_de_elementen_van_de_categorie_verblijfstitel = models.CharField(
        _("Datum van opneming met betrekking tot de elementen van de categorie Verblijfstitel"), max_length=200,
        blank=True)


class Gezagsverhouding(models.Model):
    indicatie_gezag_minderjarige = models.CharField(_("Indicatie gezag minderjarige"), max_length=200, blank=True)
    indicatie_curateleregister = models.CharField(_("Indicatie curateleregister"), max_length=200, blank=True)
    gemeente_waar_de_gegevens_over_gezagsverhouding_aan_het_document_ontleend_zijn = models.CharField(
        _("Gemeente waar de gegevens over gezagsverhouding aan het document ontleend zijn"), max_length=200, blank=True)
    datum_van_de_ontlening_van_de_gegevens_over_gezagsverhouding = models.CharField(
        _("Datum van de ontlening van de gegevens over gezagsverhouding"), max_length=200, blank=True)
    beschrijving_van_het_document_waaraan_de_gegevens_over_gezagsverhouding_ontleend_zijn = models.CharField(
        _("Beschrijving van het document waaraan de gegevens over gezagsverhouding ontleend zijn"), max_length=200,
        blank=True)
    aanduiding_gegevens_in_onderzoek = models.CharField(_("Aanduiding gegevens in onderzoek"), max_length=200,
                                                        blank=True)
    datum_ingang_onderzoek = models.CharField(_("Datum ingang onderzoek"), max_length=200, blank=True)
    datum_einde_onderzoek = models.CharField(_("Datum einde onderzoek"), max_length=200, blank=True)
    indicatie_onjuist = models.CharField(_("Indicatie onjuist"), max_length=200, blank=True)
    ingangsdatum_geldigheid_met_betrekking_tot_de_elementen_van_de_categorie_gezagsverhouding = models.CharField(
        _("Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Gezagsverhouding"), max_length=200,
        blank=True)
    datum_van_opneming_met_betrekking_tot_de_elementen_van_de_categorie_gezagsverhouding = models.CharField(
        _("Datum van opneming met betrekking tot de elementen van de categorie Gezagsverhouding"), max_length=200,
        blank=True)


class Reisdocument(models.Model):
    soort_nederlands_reisdocument = models.CharField(_("Soort Nederlands reisdocument"), max_length=200, blank=True)
    nummer_nederlands_reisdocument = models.CharField(_("Nummer Nederlands reisdocument"), max_length=200, blank=True)
    datum_uitgifte_nederlands_reisdocument = models.CharField(_("Datum uitgifte Nederlands reisdocument"),
                                                              max_length=200, blank=True)
    autoriteit_van_afgifte_nederlands_reisdocument = models.CharField(
        _("Autoriteit van afgifte Nederlands reisdocument"), max_length=200, blank=True)
    datum_einde_geldigheid_nederlands_reisdocument = models.CharField(
        _("Datum einde geldigheid Nederlands reisdocument"), max_length=200, blank=True)
    datum_inhouding_dan_wel_vermissing_nederlands_reisdocument = models.CharField(
        _("Datum inhouding dan wel vermissing Nederlands reisdocument"), max_length=200, blank=True)
    aanduiding_inhouding_dan_wel_vermissing_nederlands_reisdocument = models.CharField(
        _("Aanduiding inhouding dan wel vermissing Nederlands reisdocument"), max_length=200, blank=True)
    signalering_met_betrekking_tot_verstrekken_nederlands_reisdocument = models.CharField(
        _("Signalering met betrekking tot verstrekken Nederlands reisdocument"), max_length=200, blank=True)
    gemeente_waar_het_paspoortdossier_zich_bevindt = models.CharField(
        _("Gemeente waar het paspoortdossier zich bevindt"), max_length=200, blank=True)
    datum_van_opname_in_het_paspoortdossier = models.CharField(_("Datum van opname in het paspoortdossier"),
                                                               max_length=200, blank=True)
    beschrijving_dossier_waarin_de_aanvullende_paspoortgegevens_zich_bevinden = models.CharField(
        _("Beschrijving dossier waarin de aanvullende paspoortgegevens zich bevinden"), max_length=200, blank=True)
    aanduiding_gegevens_in_onderzoek = models.CharField(_("Aanduiding gegevens in onderzoek"), max_length=200,
                                                        blank=True)
    datum_ingang_onderzoek = models.CharField(_("Datum ingang onderzoek"), max_length=200, blank=True)
    datum_einde_onderzoek = models.CharField(_("Datum einde onderzoek"), max_length=200, blank=True)
    datum_van_ingang_geldigheid_met_betrekking_tot_de_elementen_van_de_categorie_reisdocument = models.CharField(
        _("Datum van ingang geldigheid met betrekking tot de elementen van de categorie Reisdocument"), max_length=200,
        blank=True)
    datum_van_opneming_met_betrekking_tot_de_elementen_van_de_categorie_reisdocument = models.CharField(
        _("Datum van opneming met betrekking tot de elementen van de categorie Reisdocument"), max_length=200,
        blank=True)


class Kiesrecht(models.Model):
    aanduiding_europees_kiesrecht = models.CharField(_("Aanduiding Europees kiesrecht"), max_length=200, blank=True)
    datum_verzoek_of_mededeling_europees_kiesrecht = models.CharField(
        _("Datum verzoek of mededeling Europees kiesrecht"), max_length=200, blank=True)
    einddatum_uitsluiting_europees_kiesrecht = models.CharField(_("Einddatum uitsluiting Europees kiesrecht"),
                                                                max_length=200, blank=True)
    aanduiding_uitgesloten_kiesrecht = models.CharField(_("Aanduiding uitgesloten kiesrecht"), max_length=200,
                                                        blank=True)
    einddatum_uitsluiting_kiesrecht = models.CharField(_("Einddatum uitsluiting kiesrecht"), max_length=200, blank=True)
    gemeente_waar_de_gegevens_over_kiesrecht_aan_het_document_ontleend_zijn = models.CharField(
        _("Gemeente waar de gegevens over kiesrecht aan het document ontleend zijn"), max_length=200, blank=True)
    datum_van_de_ontlening_van_de_gegevens_over_kiesrecht = models.CharField(
        _("Datum van de ontlening van de gegevens over kiesrecht"), max_length=200, blank=True)
    beschrijving_van_het_document_waaraan_de_gegevens_over_kiesrecht_ontleend_zijn = models.CharField(
        _("Beschrijving van het document waaraan de gegevens over kiesrecht ontleend zijn"), max_length=200, blank=True)
