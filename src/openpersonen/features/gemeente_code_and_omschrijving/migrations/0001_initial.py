# Generated by Django 2.2.15 on 2020-12-04 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GemeenteCodeAndOmschrijving",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.IntegerField()),
                ("omschrijving", models.CharField(max_length=200)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]