# Generated by Django 2.0.6 on 2018-06-15 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicforms', '0005_question_help_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='help_text',
            field=models.CharField(blank=True, default='', help_text='Apporte des précisions sur la question', max_length=300, verbose_name='aide'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(help_text='intitulé de la question', max_length=300, verbose_name='intitulé'),
        ),
    ]
