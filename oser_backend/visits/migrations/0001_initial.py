# Generated by Django 2.0.2 on 2018-03-01 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nom')),
                ('address', models.CharField(help_text="L'adresse complète de ce lieu : numéro, rue ou voie, code postal, ville, pays si pertinent.", max_length=200, verbose_name='adresse')),
                ('description', markdownx.models.MarkdownxField(blank=True, default='', help_text="Une description de ce lieu : de quoi s'agit-il ? Ce champ supporte Markdown.")),
            ],
            options={
                'verbose_name': 'lieu',
                'verbose_name_plural': 'lieux',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Préciser si besoin le type de sortie (exposition, concert…) ', max_length=100, verbose_name='titre')),
                ('summary', models.CharField(blank=True, default='', help_text='Une ou deux phrases décrivant la sortie de manière attrayante.', max_length=300, verbose_name='résumé')),
                ('description', markdownx.models.MarkdownxField(blank=True, default='', help_text='Une description plus complète des activités proposées durant la sortie. Ce champ supporte Markdown.')),
                ('date', models.DateTimeField(help_text="Heure de début de la sortie. Format de l'heure : hh:mm.")),
                ('deadline', models.DateTimeField(help_text="Note : les lycéens ne pourront plus s'inscrire passé cette date. Format de l'heure : hh:mm.", verbose_name="date limite d'inscription")),
                ('image', models.ImageField(blank=True, help_text='Une illustration représentative de la sortie. Dimensions : ???x???', null=True, upload_to='', verbose_name='illustration')),
                ('fact_sheet', models.FileField(blank=True, help_text='Formats supportés : PDF', null=True, upload_to='', verbose_name='fiche sortie')),
                ('organizers_group', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group', verbose_name='organisateurs')),
            ],
            options={
                'verbose_name': 'sortie',
                'ordering': ('date',),
                'permissions': (('manage_visit', 'Can manage visit'),),
            },
        ),
        migrations.CreateModel(
            name='VisitParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present', models.NullBooleanField(verbose_name='présent')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visits.Visit', verbose_name='sortie')),
            ],
            options={
                'verbose_name': 'participant à la sortie',
                'verbose_name_plural': 'participants à la sortie',
            },
        ),
        migrations.AddField(
            model_name='visit',
            name='participants',
            field=models.ManyToManyField(through='visits.VisitParticipant', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='visit',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='visits.Place', verbose_name='lieu'),
        ),
        migrations.AlterUniqueTogether(
            name='visitparticipant',
            unique_together={('user', 'visit')},
        ),
    ]