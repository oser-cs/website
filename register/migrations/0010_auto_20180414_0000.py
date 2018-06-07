# Generated by Django 2.0.3 on 2018-04-13 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0009_auto_20180408_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Prénom du contact (50 caractères max).', max_length=50, verbose_name='prénom')),
                ('last_name', models.CharField(help_text='Nom du contact (50 caractères max).', max_length=50, verbose_name='nom')),
                ('contact', models.CharField(help_text='Téléphone, adresse email…', max_length=100)),
            ],
            options={
                'verbose_name': "contact d'urgence",
                'verbose_name_plural': "contacts d'urgence",
                'ordering': ('last_name', 'first_name'),
            },
        ),
        migrations.AlterField(
            model_name='registration',
            name='emergency_contact',
            field=models.ForeignKey(blank=True, help_text="Contact en cas d'urgence.", null=True, on_delete=django.db.models.deletion.CASCADE, to='register.EmergencyContact', verbose_name="contact d'urgence"),
        ),
    ]