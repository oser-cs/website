# Generated by Django 2.0.4 on 2018-05-05 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0015_auto_20180505_1403'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student', to='register.Registration', verbose_name="dossier d'inscription")),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='tutoring.School', verbose_name='lycée')),
                ('tutoring_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='tutoring.TutoringGroup', verbose_name='groupe de tutorat')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
            options={
                'verbose_name': 'lycéen',
            },
            bases=(profiles.models.ProfileMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promotion', models.IntegerField(choices=[(2020, '2020'), (2019, '2019'), (2018, '2018'), (2017, '2017'), (2016, '2016')], default=2020)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutor', to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
            options={
                'verbose_name': 'tuteur',
            },
            bases=(profiles.models.ProfileMixin, models.Model),
        ),
    ]
