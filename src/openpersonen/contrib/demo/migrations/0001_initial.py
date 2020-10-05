# Generated by Django 2.2.15 on 2020-10-05 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persoon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_nummer_persoon', models.CharField(blank=True, max_length=200, verbose_name='A-nummer persoon')),
                ('burgerservicenummer_persoon', models.CharField(blank=True, max_length=200, verbose_name='Burgerservicenummer persoon')),
                ('voornamen_persoon', models.CharField(blank=True, max_length=200, verbose_name='Voornamen persoon')),
                ('adellijke_titel_predikaat_persoon', models.CharField(blank=True, max_length=200, verbose_name='Adellijke titel/predikaat persoon')),
                ('voorvoegsel_geslachtsnaam_persoon', models.CharField(blank=True, max_length=200, verbose_name='Voorvoegsel geslachtsnaam persoon')),
                ('geslachtsnaam_persoon', models.CharField(blank=True, max_length=200, verbose_name='Geslachtsnaam persoon')),
                ('geboortedatum_persoon', models.CharField(blank=True, help_text='Format YYYYMMDD', max_length=200, verbose_name='Geboortedatum persoon')),
                ('geboorteplaats_persoon', models.CharField(blank=True, max_length=200, verbose_name='Geboorteplaats persoon')),
                ('geboorteland_persoon', models.CharField(blank=True, help_text='Four digit code', max_length=200, verbose_name='Geboorteland persoon')),
                ('geslachtsaanduiding', models.CharField(blank=True, help_text='M for mannen and V for vrouwen', max_length=1, verbose_name='Geslachtsaanduiding')),
                ('vorig_a_nummer', models.CharField(blank=True, max_length=200, verbose_name='Vorig A-nummer')),
                ('volgend_a_nummer', models.CharField(blank=True, max_length=200, verbose_name='Volgend A-nummer')),
                ('aanduiding_naamgebruik', models.CharField(blank=True, max_length=1, verbose_name='Aanduiding naamgebruik')),
                ('registergemeente_akte_waaraan_gegevens', models.CharField(blank=True, help_text='Four digit code', max_length=200, verbose_name='Registergemeente akte waaraan gegevens over persoon ontleend zijn')),
                ('aktenummer_van_de_akte', models.CharField(blank=True, max_length=7, verbose_name='Aktenummer van de akte waaraan gegevens over persoon ontleend zijn')),
                ('gemeente_waar_de_gegevens_over_persoon', models.CharField(blank=True, help_text='Four digit code', max_length=200, verbose_name='Gemeente waar de gegevens over persoon aan het document ontleend zijn')),
                ('datum_van_de_ontlening_van_de_gegevens_over_persoon', models.CharField(blank=True, help_text='Format YYYYMMDD', max_length=200, verbose_name='Datum van de ontlening van de gegevens over persoon')),
                ('beschrijving_van_het_document', models.CharField(blank=True, max_length=200, verbose_name='Beschrijving van het document waaraan de gegevens over persoon ontleend zijn')),
                ('aanduiding_gegevens_in_onderzoek', models.CharField(blank=True, help_text='Six digit code', max_length=6, verbose_name='Aanduiding gegevens in onderzoek')),
                ('datum_ingang_onderzoek', models.CharField(blank=True, help_text='Format YYYYMMDD', max_length=200, verbose_name='Datum ingang onderzoek')),
                ('datum_einde_onderzoek', models.CharField(blank=True, help_text='Format YYYYMMDD', max_length=200, verbose_name='Datum einde onderzoek')),
                ('indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde', models.CharField(blank=True, max_length=200, verbose_name='Indicatie onjuist dan wel strijdigheid met de openbare orde')),
                ('ingangsdatum_geldigheid_met_betrekking', models.CharField(blank=True, help_text='Format YYYYMMDD', max_length=200, verbose_name='Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Persoon')),
                ('datum_van_opneming_met_betrekking', models.CharField(blank=True, help_text='Format YYYYMMDD', max_length=200, verbose_name='Datum van opneming met betrekking tot de elementen van de categorie Persoon')),
                ('rni_deelnemer', models.CharField(blank=True, max_length=200, verbose_name='RNI-deelnemer')),
            ],
        ),
        migrations.CreateModel(
            name='Verblijfstitel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aanduiding_verblijfstitel', models.CharField(blank=True, max_length=200, verbose_name='Aanduiding verblijfstitel')),
                ('datum_einde_verblijfstitel', models.CharField(blank=True, max_length=200, verbose_name='Datum einde verblijfstitel')),
                ('ingangsdatum_verblijfstitel', models.CharField(blank=True, max_length=200, verbose_name='Ingangsdatum verblijfstitel')),
                ('aanduiding_gegevens_in_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Aanduiding gegevens in onderzoek')),
                ('datum_ingang_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Datum ingang onderzoek')),
                ('datum_einde_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Datum einde onderzoek')),
                ('indicatie_onjuist', models.CharField(blank=True, max_length=200, verbose_name='Indicatie onjuist')),
                ('ingangsdatum_geldigheid_met_betrekking', models.CharField(blank=True, max_length=200, verbose_name='Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Verblijfstitel')),
                ('datum_van_opneming_met_betrekking', models.CharField(blank=True, max_length=200, verbose_name='Datum van opneming met betrekking tot de elementen van de categorie Verblijfstitel')),
                ('persoon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='demo.Persoon')),
            ],
        ),
        migrations.CreateModel(
            name='Verblijfplaats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gemeente_van_inschrijving', models.CharField(blank=True, max_length=200, verbose_name='Gemeente van inschrijving')),
                ('datum_inschrijving_in_de_gemeente', models.CharField(blank=True, max_length=200, verbose_name='Datum inschrijving in de gemeente')),
                ('functie_adres', models.CharField(blank=True, max_length=200, verbose_name='Functie adres')),
                ('gemeentedeel', models.CharField(blank=True, max_length=200, verbose_name='Gemeentedeel')),
                ('datum_aanvang_adreshouding', models.CharField(blank=True, max_length=200, verbose_name='Datum aanvang adreshouding')),
                ('straatnaam', models.CharField(blank=True, max_length=200, verbose_name='Straatnaam')),
                ('naam_openbare_ruimte', models.CharField(blank=True, max_length=200, verbose_name='Naam openbare ruimte')),
                ('huisnummer', models.CharField(blank=True, max_length=200, verbose_name='Huisnummer')),
                ('huisletter', models.CharField(blank=True, max_length=200, verbose_name='Huisletter')),
                ('huisnummertoevoeging', models.CharField(blank=True, max_length=200, verbose_name='Huisnummertoevoeging')),
                ('aanduiding_bij_huisnummer', models.CharField(blank=True, max_length=200, verbose_name='Aanduiding bij huisnummer')),
                ('postcode', models.CharField(blank=True, max_length=200, verbose_name='Postcode')),
                ('woonplaatsnaam', models.CharField(blank=True, max_length=200, verbose_name='Woonplaatsnaam')),
                ('identificatiecode_verblijfplaats', models.CharField(blank=True, max_length=200, verbose_name='Identificatiecode verblijfplaats')),
                ('identificatiecode_nummeraanduiding', models.CharField(blank=True, max_length=200, verbose_name='Identificatiecode nummeraanduiding')),
                ('locatiebeschrijving', models.CharField(blank=True, max_length=200, verbose_name='Locatiebeschrijving')),
                ('land_adres_buitenland', models.CharField(blank=True, max_length=200, verbose_name='Land adres buitenland')),
                ('datum_aanvang_adres_buitenland', models.CharField(blank=True, max_length=200, verbose_name='Datum aanvang adres buitenland')),
                ('regel_1_adres_buitenland', models.CharField(blank=True, max_length=200, verbose_name='Regel 1 adres buitenland')),
                ('regel_2_adres_buitenland', models.CharField(blank=True, max_length=200, verbose_name='Regel 2 adres buitenland')),
                ('regel_3_adres_buitenland', models.CharField(blank=True, max_length=200, verbose_name='Regel 3 adres buitenland')),
                ('land_vanwaar_ingeschreven', models.CharField(blank=True, max_length=200, verbose_name='Land vanwaar ingeschreven')),
                ('datum_vestiging_in_nederland', models.CharField(blank=True, max_length=200, verbose_name='Datum vestiging in Nederland')),
                ('omschrijving_van_de_aangifte_adreshouding', models.CharField(blank=True, max_length=200, verbose_name='Omschrijving van de aangifte adreshouding')),
                ('indicatie_document', models.CharField(blank=True, max_length=200, verbose_name='Indicatie document')),
                ('aanduiding_gegevens_in_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Aanduiding gegevens in onderzoek')),
                ('datum_ingang_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Datum ingang onderzoek')),
                ('datum_einde_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Datum einde onderzoek')),
                ('indicatie_onjuist', models.CharField(blank=True, max_length=200, verbose_name='Indicatie onjuist')),
                ('ingangsdatum_geldigheid_met_betrekking', models.CharField(blank=True, max_length=200, verbose_name='Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Verblijfplaats')),
                ('datum_van_opneming_met_betrekking', models.CharField(blank=True, max_length=200, verbose_name='Datum van opneming met betrekking tot de elementen van de categorie Verblijfplaats')),
                ('rni_deelnemer', models.CharField(blank=True, max_length=200, verbose_name='RNI-deelnemer')),
                ('omschrijving_verdrag', models.CharField(blank=True, max_length=200, verbose_name='Omschrijving verdrag')),
                ('persoon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='demo.Persoon')),
            ],
        ),
        migrations.CreateModel(
            name='Reisdocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soort_nederlands_reisdocument', models.CharField(blank=True, max_length=200, verbose_name='Soort Nederlands reisdocument')),
                ('nummer_nederlands_reisdocument', models.CharField(blank=True, max_length=200, verbose_name='Nummer Nederlands reisdocument')),
                ('datum_uitgifte_nederlands_reisdocument', models.CharField(blank=True, max_length=200, verbose_name='Datum uitgifte Nederlands reisdocument')),
                ('autoriteit_van_afgifte_nederlands_reisdocument', models.CharField(blank=True, max_length=200, verbose_name='Autoriteit van afgifte Nederlands reisdocument')),
                ('datum_einde_geldigheid_nederlands_reisdocument', models.CharField(blank=True, max_length=200, verbose_name='Datum einde geldigheid Nederlands reisdocument')),
                ('datum_inhouding_dan_wel_vermissing_nederlands_reisdocument', models.CharField(blank=True, max_length=200, verbose_name='Datum inhouding dan wel vermissing Nederlands reisdocument')),
                ('aanduiding_inhouding_dan_wel_vermissing_nederlands_reisdocument', models.CharField(blank=True, max_length=200, verbose_name='Aanduiding inhouding dan wel vermissing Nederlands reisdocument')),
                ('signalering_met_betrekking', models.CharField(blank=True, max_length=200, verbose_name='Signalering met betrekking tot verstrekken Nederlands reisdocument')),
                ('gemeente_waar_het_paspoortdossier_zich_bevindt', models.CharField(blank=True, max_length=200, verbose_name='Gemeente waar het paspoortdossier zich bevindt')),
                ('datum_van_opname_in_het_paspoortdossier', models.CharField(blank=True, max_length=200, verbose_name='Datum van opname in het paspoortdossier')),
                ('beschrijving_dossier', models.CharField(blank=True, max_length=200, verbose_name='Beschrijving dossier waarin de aanvullende paspoortgegevens zich bevinden')),
                ('aanduiding_gegevens_in_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Aanduiding gegevens in onderzoek')),
                ('datum_ingang_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Datum ingang onderzoek')),
                ('datum_einde_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Datum einde onderzoek')),
                ('datum_van_ingang_geldigheid_met_betrekking', models.CharField(blank=True, max_length=200, verbose_name='Datum van ingang geldigheid met betrekking tot de elementen van de categorie Reisdocument')),
                ('datum_van_opneming_met_betrekking', models.CharField(blank=True, max_length=200, verbose_name='Datum van opneming met betrekking tot de elementen van de categorie Reisdocument')),
                ('persoon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='demo.Persoon')),
            ],
        ),
        migrations.CreateModel(
            name='Partnerschap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_nummer_echtgenoot_geregistreerd_partner', models.CharField(blank=True, max_length=200, verbose_name='A-nummer echtgenoot/geregistreerd partner')),
                ('burgerservicenummer_echtgenoot_geregistreerd_partner', models.CharField(blank=True, max_length=200, verbose_name='Burgerservicenummer echtgenoot/geregistreerd partner')),
                ('voornamen_echtgenoot_geregistreerd_partner', models.CharField(blank=True, max_length=200, verbose_name='Voornamen echtgenoot/geregistreerd partner')),
                ('adellijke_titel_predikaat_echtgenoot_geregistreerd_partner', models.CharField(blank=True, max_length=200, verbose_name='Adellijke titel/predikaat echtgenoot/geregistreerd partner')),
                ('voorvoegsel_geslachtsnaam_echtgenoot_geregistreerd_partner', models.CharField(blank=True, max_length=200, verbose_name='Voorvoegsel geslachtsnaam echtgenoot/geregistreerd partner')),
                ('geslachtsnaam_echtgenoot_geregistreerd_partner', models.CharField(blank=True, max_length=200, verbose_name='Geslachtsnaam echtgenoot/geregistreerd partner')),
                ('geboortedatum_echtgenoot_geregistreerd_partner', models.CharField(blank=True, max_length=200, verbose_name='Geboortedatum echtgenoot/geregistreerd partner')),
                ('geboorteplaats_echtgenoot_geregistreerd_partner', models.CharField(blank=True, max_length=200, verbose_name='Geboorteplaats echtgenoot/geregistreerd partner')),
                ('geboorteland_echtgenoot_geregistreerd_partner', models.CharField(blank=True, max_length=200, verbose_name='Geboorteland echtgenoot/geregistreerd partner')),
                ('geslachtsaanduiding_echtgenoot_geregistreerd_partner', models.CharField(blank=True, max_length=200, verbose_name='Geslachtsaanduiding echtgenoot/geregistreerd partner')),
                ('datum_huwelijkssluiting_aangaan_geregistreerd_partnerschap', models.CharField(blank=True, max_length=200, verbose_name='Datum huwelijkssluiting/aangaan geregistreerd partnerschap')),
                ('plaats_huwelijkssluiting_aangaan_geregistreerd_partnerschap', models.CharField(blank=True, max_length=200, verbose_name='Plaats huwelijkssluiting/aangaan geregistreerd partnerschap')),
                ('land_huwelijkssluiting_aangaan_geregistreerd_partnerschap', models.CharField(blank=True, max_length=200, verbose_name='Land huwelijkssluiting/aangaan geregistreerd partnerschap')),
                ('datum_ontbinding_huwelijk_geregistreerd_partnerschap', models.CharField(blank=True, max_length=200, verbose_name='Datum ontbinding huwelijk/geregistreerd partnerschap')),
                ('plaats_ontbinding_huwelijk_geregistreerd_partnerschap', models.CharField(blank=True, max_length=200, verbose_name='Plaats ontbinding huwelijk/geregistreerd partnerschap')),
                ('land_ontbinding_huwelijk_geregistreerd_partnerschap', models.CharField(blank=True, max_length=200, verbose_name='Land ontbinding huwelijk/geregistreerd partnerschap')),
                ('reden_ontbinding_huwelijk_geregistreerd_partnerschap', models.CharField(blank=True, max_length=200, verbose_name='Reden ontbinding huwelijk/geregistreerd partnerschap')),
                ('soort_verbintenis', models.CharField(blank=True, max_length=200, verbose_name='Soort verbintenis')),
                ('registergemeente_akte_waaraan_gegevens', models.CharField(blank=True, max_length=200, verbose_name='Registergemeente akte waaraan gegevens over huwelijk/geregistreerd partnerschap ontleend zijn')),
                ('aktenummer_van_de_akte_waaraan_gegevens', models.CharField(blank=True, max_length=200, verbose_name='Aktenummer van de akte waaraan gegevens over huwelijk/geregistreerd partnerschap ontleend zijn')),
                ('gemeente_waar_de_gegevens_over_huwelijk', models.CharField(blank=True, max_length=200, verbose_name='Gemeente waar de gegevens over huwelijk/geregistreerd partnerschap aan het document ontleend zijn')),
                ('datum_van_de_ontlening_van_de_gegevens', models.CharField(blank=True, max_length=200, verbose_name='Datum van de ontlening van de gegevens over huwelijk/geregistreerd partnerschap')),
                ('beschrijving_van_het_document_waaraan_de_gegevens', models.CharField(blank=True, max_length=200, verbose_name='Beschrijving van het document waaraan de gegevens over huwelijk/ geregistreerd partnerschap ontleend zijn')),
                ('aanduiding_gegevens_in_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Aanduiding gegevens in onderzoek')),
                ('datum_ingang_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Datum ingang onderzoek')),
                ('datum_einde_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Datum einde onderzoek')),
                ('indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde', models.CharField(blank=True, max_length=200, verbose_name='Indicatie onjuist dan wel strijdigheid met de openbare orde')),
                ('ingangsdatum_geldigheid_met_betrekking', models.CharField(blank=True, max_length=200, verbose_name='Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Huwelijk/geregistreerd part')),
                ('datum_van_opneming_met_betrekking', models.CharField(blank=True, max_length=200, verbose_name='Datum van opneming met betrekking tot de elementen van de categorie Huwelijk/geregistreerd partnersc')),
                ('persoon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='demo.Persoon')),
            ],
        ),
        migrations.CreateModel(
            name='Overlijden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum_overlijden', models.CharField(blank=True, max_length=200, verbose_name='Datum overlijden')),
                ('plaats_overlijden', models.CharField(blank=True, max_length=200, verbose_name='Plaats overlijden')),
                ('land_overlijden', models.CharField(blank=True, max_length=200, verbose_name='Land overlijden')),
                ('registergemeente_akte_waaraan_gegevens', models.CharField(blank=True, max_length=200, verbose_name='Registergemeente akte waaraan gegevens over overlijden ontleend zijn')),
                ('aktenummer_van_de_akte_waaraan_gegevens', models.CharField(blank=True, max_length=200, verbose_name='Aktenummer van de akte waaraan gegevens over overlijden ontleend zijn')),
                ('gemeente_waar_de_gegevens_over_overlijden', models.CharField(blank=True, max_length=200, verbose_name='Gemeente waar de gegevens over overlijden aan het document ontleend zijn')),
                ('datum_van_de_ontlening_van_de_gegevens_over_overlijden', models.CharField(blank=True, max_length=200, verbose_name='Datum van de ontlening van de gegevens over overlijden')),
                ('beschrijving_van_het_document_waaraan_de_gegevens', models.CharField(blank=True, max_length=200, verbose_name='Beschrijving van het document waaraan de gegevens over overlijden ontleend zijn')),
                ('aanduiding_gegevens_in_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Aanduiding gegevens in onderzoek')),
                ('datum_ingang_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Datum ingang onderzoek')),
                ('datum_einde_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Datum einde onderzoek')),
                ('indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde', models.CharField(blank=True, max_length=200, verbose_name='Indicatie onjuist dan wel strijdigheid met de openbare orde')),
                ('ingangsdatum_geldigheid_met_betrekking', models.CharField(blank=True, max_length=200, verbose_name='Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Overlijden')),
                ('datum_van_opneming_met_betrekking', models.CharField(blank=True, max_length=200, verbose_name='Datum van opneming met betrekking tot de elementen van de categorie Overlijden')),
                ('rni_deelnemer', models.CharField(blank=True, max_length=200, verbose_name='RNI-deelnemer')),
                ('persoon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='demo.Persoon')),
            ],
        ),
        migrations.CreateModel(
            name='Ouder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_nummer_ouder', models.CharField(blank=True, max_length=200, verbose_name='A-nummer ouder')),
                ('burgerservicenummer_ouder', models.CharField(blank=True, max_length=200, verbose_name='Burgerservicenummer ouder')),
                ('voornamen_ouder', models.CharField(blank=True, max_length=200, verbose_name='Voornamen ouder')),
                ('adellijke_titel_predikaat_ouder', models.CharField(blank=True, max_length=200, verbose_name='Adellijke titel/predikaat ouder')),
                ('voorvoegsel_geslachtsnaam_ouder', models.CharField(blank=True, max_length=200, verbose_name='Voorvoegsel geslachtsnaam ouder')),
                ('geslachtsnaam_ouder', models.CharField(blank=True, max_length=200, verbose_name='Geslachtsnaam ouder')),
                ('geboortedatum_ouder', models.CharField(blank=True, help_text='Format YYYYMMDD', max_length=200, verbose_name='Geboortedatum ouder')),
                ('geboorteplaats_ouder', models.CharField(blank=True, max_length=200, verbose_name='Geboorteplaats ouder')),
                ('geboorteland_ouder', models.CharField(blank=True, help_text='Four digit code', max_length=200, verbose_name='Geboorteland ouder')),
                ('geslachtsaanduiding_ouder', models.CharField(blank=True, help_text='M for mannen and V for vrouwen', max_length=1, verbose_name='Geslachtsaanduiding ouder')),
                ('datum_ingang_familierechtelijke_betrekking_ouder', models.CharField(blank=True, help_text='Four digit code', max_length=200, verbose_name='Datum ingang familierechtelijke betrekking ouder')),
                ('registergemeente_akte_waaraan_gegevens_over_ouder_ontleend_zijn', models.CharField(blank=True, help_text='Four digit code', max_length=200, verbose_name='Registergemeente akte waaraan gegevens over ouder ontleend zijn')),
                ('aktenummer_van_de_akte_waaraan_gegevens', models.CharField(blank=True, max_length=200, verbose_name='Aktenummer van de akte waaraan gegevens over ouder ontleend zijn')),
                ('gemeente_waar_de_gegevens_over_ouder', models.CharField(blank=True, help_text='Four digit code', max_length=200, verbose_name='Gemeente waar de gegevens over ouder aan het document ontleend zijn')),
                ('datum_van_de_ontlening_van_de_gegevens_over_ouder', models.CharField(blank=True, max_length=200, verbose_name='Datum van de ontlening van de gegevens over ouder')),
                ('beschrijving_van_het_document_waaraan_de_gegevens', models.CharField(blank=True, max_length=200, verbose_name='Beschrijving van het document waaraan de gegevens over ouder ontleend zijn')),
                ('aanduiding_gegevens_in_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Aanduiding gegevens in onderzoek')),
                ('datum_ingang_onderzoek', models.CharField(blank=True, help_text='Format YYYYMMDD', max_length=200, verbose_name='Datum ingang onderzoek')),
                ('datum_einde_onderzoek', models.CharField(blank=True, help_text='Format YYYYMMDD', max_length=200, verbose_name='Datum einde onderzoek')),
                ('indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde', models.CharField(blank=True, help_text='One digit code', max_length=1, verbose_name='Indicatie onjuist dan wel strijdigheid met de openbare orde')),
                ('ingangsdatum_geldigheid_met_betrekking', models.CharField(blank=True, help_text='Format YYYYMMDD', max_length=200, verbose_name='Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Ouder')),
                ('datum_van_opneming_met_betrekking', models.CharField(blank=True, help_text='Format YYYYMMDD', max_length=200, verbose_name='Datum van opneming met betrekking tot de elementen van de categorie Ouder')),
                ('persoon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='demo.Persoon')),
            ],
        ),
        migrations.CreateModel(
            name='Nationaliteit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationaliteit', models.CharField(blank=True, help_text='Four digit code', max_length=200, verbose_name='Nationaliteit')),
                ('reden_opname_nationaliteit', models.CharField(blank=True, help_text='Three digit code', max_length=3, verbose_name='Reden opname nationaliteit')),
                ('reden_beeindigen_nationaliteit', models.CharField(blank=True, help_text='Three digit code', max_length=3, verbose_name='Reden beëindigen nationaliteit')),
                ('aanduiding_bijzonder_nederlanderschap', models.CharField(blank=True, max_length=200, verbose_name='Aanduiding bijzonder Nederlanderschap')),
                ('eu_persoonsummer', models.CharField(blank=True, max_length=200, verbose_name='EU-persoonsummer')),
                ('gemeente_waar_de_gegevens_over_nationaliteit', models.CharField(blank=True, help_text='Four digit code', max_length=200, verbose_name='Gemeente waar de gegevens over nationaliteit aan het document ontleend dan wel afgeleid zijn')),
                ('datum_van_de_ontlening', models.CharField(blank=True, help_text='Format YYYYMMDD', max_length=200, verbose_name='Datum van de ontlening dan wel afleiding van de gegevens over nationaliteit')),
                ('beschrijving_van_het_document', models.CharField(blank=True, max_length=200, verbose_name='Beschrijving van het document waaraan de gegevens over nationaliteit ontleend dan wel afgeleid zijn')),
                ('aanduiding_gegevens_in_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Aanduiding gegevens in onderzoek')),
                ('datum_ingang_onderzoek', models.CharField(blank=True, help_text='Format YYYYMMDD', max_length=200, verbose_name='Datum ingang onderzoek')),
                ('datum_einde_onderzoek', models.CharField(blank=True, help_text='Format YYYYMMDD', max_length=200, verbose_name='Datum einde onderzoek')),
                ('indicatie_onjuist', models.CharField(blank=True, max_length=200, verbose_name='Indicatie onjuist')),
                ('datum_van_ingang_geldigheid_met_betrekking', models.CharField(blank=True, help_text='Format YYYYMMDD', max_length=200, verbose_name='Datum van ingang geldigheid met betrekking tot de elementen van de categorie Nationaliteit')),
                ('datum_van_opneming_met_betrekking', models.CharField(blank=True, help_text='Format YYYYMMDD', max_length=200, verbose_name='Datum van opneming met betrekking tot de elementen van de categorie Nationaliteit')),
                ('rni_deelnemer', models.CharField(blank=True, max_length=200, verbose_name='RNI-deelnemer')),
                ('omschrijving_verdrag', models.CharField(blank=True, max_length=200, verbose_name='Omschrijving verdrag')),
                ('persoon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='demo.Persoon')),
            ],
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_nummer_kind', models.CharField(blank=True, max_length=200, verbose_name='A-nummer kind')),
                ('burgerservicenummer_kind', models.CharField(blank=True, max_length=200, verbose_name='Burgerservicenummer kind')),
                ('voornamen_kind', models.CharField(blank=True, max_length=200, verbose_name='Voornamen kind')),
                ('adellijke_titel_predikaat_kind', models.CharField(blank=True, max_length=200, verbose_name='Adellijke titel/predikaat kind')),
                ('voorvoegsel_geslachtsnaam_kind', models.CharField(blank=True, max_length=200, verbose_name='Voorvoegsel geslachtsnaam kind')),
                ('geslachtsnaam_kind', models.CharField(blank=True, max_length=200, verbose_name='Geslachtsnaam kind')),
                ('geboortedatum_kind', models.CharField(blank=True, max_length=200, verbose_name='Geboortedatum kind')),
                ('geboorteplaats_kind', models.CharField(blank=True, max_length=200, verbose_name='Geboorteplaats kind')),
                ('geboorteland_kind', models.CharField(blank=True, max_length=200, verbose_name='Geboorteland kind')),
                ('registergemeente_akte_waaraan_gegevens_over_kind_ontleend_zijn', models.CharField(blank=True, max_length=200, verbose_name='Registergemeente akte waaraan gegevens over kind ontleend zijn')),
                ('aktenummer_van_de_akte_waaraan_gegevens_over_kind_ontleend_zijn', models.CharField(blank=True, max_length=200, verbose_name='Aktenummer van de akte waaraan gegevens over kind ontleend zijn')),
                ('gemeente_waar_de_gegevens_over_kind', models.CharField(blank=True, max_length=200, verbose_name='Gemeente waar de gegevens over kind aan het document ontleend zijn')),
                ('datum_van_de_ontlening_van_de_gegevens_over_kind', models.CharField(blank=True, max_length=200, verbose_name='Datum van de ontlening van de gegevens over kind')),
                ('beschrijving_van_het_document', models.CharField(blank=True, max_length=200, verbose_name='Beschrijving van het document waaraan de gegevens over kind ontleend zijn')),
                ('aanduiding_gegevens_in_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Aanduiding gegevens in onderzoek')),
                ('datum_ingang_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Datum ingang onderzoek')),
                ('datum_einde_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Datum einde onderzoek')),
                ('indicatie_onjuist_dan_wel_strijdigheid_met_de_openbare_orde', models.CharField(blank=True, max_length=200, verbose_name='Indicatie onjuist dan wel strijdigheid met de openbare orde')),
                ('ingangsdatum_geldigheid_met_betrekking', models.CharField(blank=True, max_length=200, verbose_name='Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Kind')),
                ('datum_van_opneming_met_betrekking', models.CharField(blank=True, max_length=200, verbose_name='Datum van opneming met betrekking tot de elementen van de categorie Kind')),
                ('registratie_betrekking', models.CharField(blank=True, max_length=200, verbose_name='Registratie betrekking')),
                ('persoon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='demo.Persoon')),
            ],
        ),
        migrations.CreateModel(
            name='Kiesrecht',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aanduiding_europees_kiesrecht', models.CharField(blank=True, max_length=200, verbose_name='Aanduiding Europees kiesrecht')),
                ('datum_verzoek_of_mededeling_europees_kiesrecht', models.CharField(blank=True, max_length=200, verbose_name='Datum verzoek of mededeling Europees kiesrecht')),
                ('einddatum_uitsluiting_europees_kiesrecht', models.CharField(blank=True, max_length=200, verbose_name='Einddatum uitsluiting Europees kiesrecht')),
                ('aanduiding_uitgesloten_kiesrecht', models.CharField(blank=True, max_length=200, verbose_name='Aanduiding uitgesloten kiesrecht')),
                ('einddatum_uitsluiting_kiesrecht', models.CharField(blank=True, max_length=200, verbose_name='Einddatum uitsluiting kiesrecht')),
                ('gemeente_waar_de_gegevens_over_kiesrecht', models.CharField(blank=True, max_length=200, verbose_name='Gemeente waar de gegevens over kiesrecht aan het document ontleend zijn')),
                ('datum_van_de_ontlening_van_de_gegevens_over_kiesrecht', models.CharField(blank=True, max_length=200, verbose_name='Datum van de ontlening van de gegevens over kiesrecht')),
                ('beschrijving_van_het_document', models.CharField(blank=True, max_length=200, verbose_name='Beschrijving van het document waaraan de gegevens over kiesrecht ontleend zijn')),
                ('persoon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='demo.Persoon')),
            ],
        ),
        migrations.CreateModel(
            name='Inschrijving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum_ingang_blokkering_pl', models.CharField(blank=True, max_length=200, verbose_name='Datum ingang blokkering PL')),
                ('datum_opschorting_bijhouding', models.CharField(blank=True, max_length=200, verbose_name='Datum opschorting bijhouding')),
                ('omschrijving_reden_opschorting_bijhouding', models.CharField(blank=True, max_length=200, verbose_name='Omschrijving reden opschorting bijhouding')),
                ('datum_eerste_inschrijving_gba_rni', models.CharField(blank=True, max_length=200, verbose_name='Datum eerste inschrijving GBA/RNI')),
                ('gemeente_waar_de_pk_zich_bevindt', models.CharField(blank=True, max_length=200, verbose_name='Gemeente waar de PK zich bevindt')),
                ('indicatie_geheim', models.CharField(blank=True, max_length=200, verbose_name='Indicatie geheim')),
                ('datum_verfificatie', models.CharField(blank=True, max_length=200, verbose_name='Datum verfificatie')),
                ('omschrijving_verificatie', models.CharField(blank=True, max_length=200, verbose_name='Omschrijving verificatie')),
                ('versienummer', models.CharField(blank=True, max_length=200, verbose_name='Versienummer')),
                ('datumtijdstempel', models.CharField(blank=True, max_length=200, verbose_name='Datumtijdstempel')),
                ('pk_gegevens_volledig_meegeconverteerd', models.CharField(blank=True, max_length=200, verbose_name='PK-gegevens volledig meegeconverteerd')),
                ('rni_deelnemer', models.CharField(blank=True, max_length=200, verbose_name='RNI-deelnemer')),
                ('omschrijving_verdrag', models.CharField(blank=True, max_length=200, verbose_name='Omschrijving verdrag')),
                ('persoon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='demo.Persoon')),
            ],
        ),
        migrations.CreateModel(
            name='Gezagsverhouding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicatie_gezag_minderjarige', models.CharField(blank=True, max_length=200, verbose_name='Indicatie gezag minderjarige')),
                ('indicatie_curateleregister', models.CharField(blank=True, max_length=200, verbose_name='Indicatie curateleregister')),
                ('gemeente_waar_de_gegevens_over_gezagsverhouding', models.CharField(blank=True, max_length=200, verbose_name='Gemeente waar de gegevens over gezagsverhouding aan het document ontleend zijn')),
                ('datum_van_de_ontlening_van_de_gegevens_over_gezagsverhouding', models.CharField(blank=True, max_length=200, verbose_name='Datum van de ontlening van de gegevens over gezagsverhouding')),
                ('beschrijving_van_het_document', models.CharField(blank=True, max_length=200, verbose_name='Beschrijving van het document waaraan de gegevens over gezagsverhouding ontleend zijn')),
                ('aanduiding_gegevens_in_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Aanduiding gegevens in onderzoek')),
                ('datum_ingang_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Datum ingang onderzoek')),
                ('datum_einde_onderzoek', models.CharField(blank=True, max_length=200, verbose_name='Datum einde onderzoek')),
                ('indicatie_onjuist', models.CharField(blank=True, max_length=200, verbose_name='Indicatie onjuist')),
                ('ingangsdatum_geldigheid_met_betrekking', models.CharField(blank=True, max_length=200, verbose_name='Ingangsdatum geldigheid met betrekking tot de elementen van de categorie Gezagsverhouding')),
                ('datum_van_opneming_met_betrekking', models.CharField(blank=True, max_length=200, verbose_name='Datum van opneming met betrekking tot de elementen van de categorie Gezagsverhouding')),
                ('persoon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='demo.Persoon')),
            ],
        ),
    ]
