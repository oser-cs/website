# Generated by Django 2.0.3 on 2018-04-11 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase_site', '0011_article_introduction'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-active', '-pinned', '-published'), 'verbose_name': 'article'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='archived',
        ),
        migrations.AddField(
            model_name='article',
            name='active',
            field=models.BooleanField(default=True, help_text="Décocher pour que l'article soit archivé. Il ne sera alors plus affiché sur le site.", verbose_name='actif'),
        ),
    ]