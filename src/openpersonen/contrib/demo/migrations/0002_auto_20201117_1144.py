# Generated by Django 2.2.15 on 2020-11-17 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("demo", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="kind",
            options={"verbose_name": "Kind", "verbose_name_plural": "Kinderen"},
        ),
        migrations.AlterModelOptions(
            name="ouder",
            options={"verbose_name": "Ouder", "verbose_name_plural": "Ouders"},
        ),
        migrations.AlterModelOptions(
            name="persoon",
            options={"verbose_name": "Persoon", "verbose_name_plural": "Personen"},
        ),
    ]