# Generated by Django 2.0.6 on 2018-06-15 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicforms', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'réponse'},
        ),
        migrations.AlterModelOptions(
            name='form',
            options={'ordering': ('-created',), 'verbose_name': 'formulaire'},
        ),
        migrations.AlterModelOptions(
            name='formentry',
            options={'ordering': ('-submitted',), 'verbose_name': 'entrée de formulaire', 'verbose_name_plural': 'entrées de formulaire'},
        ),
    ]
