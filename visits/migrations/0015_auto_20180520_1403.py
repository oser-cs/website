# Generated by Django 2.0.4 on 2018-05-20 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0014_auto_20180520_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participations', to=settings.AUTH_USER_MODEL, verbose_name='utilisateur'),
        ),
        migrations.AlterField(
            model_name='participation',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participations', to='visits.Visit', verbose_name='sortie'),
        ),
    ]