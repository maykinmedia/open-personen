# Generated by Django 2.2.15 on 2021-04-16 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stufbg', '0003_auto_20201117_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stufbgclient',
            name='ontvanger_organisatie',
            field=models.CharField(blank=True, max_length=200, verbose_name='organisatie'),
        ),
        migrations.AlterField(
            model_name='stufbgclient',
            name='zender_organisatie',
            field=models.CharField(blank=True, max_length=200, verbose_name='organisatie'),
        ),
    ]
