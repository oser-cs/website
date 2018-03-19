# Generated by Django 2.0.3 on 2018-03-19 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0007_auto_20180304_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='fact_sheet',
            field=models.FileField(blank=True, help_text='Formats supportés : PDF', null=True, upload_to='visits/fact_sheets/', verbose_name='fiche sortie'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='image',
            field=models.ImageField(blank=True, help_text='Une illustration représentative de la sortie. Dimensions : ???x???', null=True, upload_to='visits/images/', verbose_name='illustration'),
        ),
    ]
