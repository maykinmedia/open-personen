# Generated by Django 2.2.15 on 2020-09-03 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StufBGClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ontvanger_organisatie', models.CharField(max_length=200)),
                ('ontvanger_administratie', models.CharField(max_length=200)),
                ('ontvanger_applicatie', models.CharField(max_length=200)),
                ('ontvanger_gebruiker', models.CharField(max_length=200)),
                ('zender_organisatie', models.CharField(max_length=200)),
                ('zender_administratie', models.CharField(max_length=200)),
                ('zender_applicatie', models.CharField(max_length=200)),
                ('zender_gebruiker', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('user', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Stuf BG Client',
            },
        ),
    ]