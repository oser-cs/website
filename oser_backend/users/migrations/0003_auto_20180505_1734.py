# Generated by Django 2.0.4 on 2018-05-05 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_student_registration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='registration',
        ),
        migrations.RemoveField(
            model_name='student',
            name='school',
        ),
        migrations.RemoveField(
            model_name='student',
            name='tutoring_group',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='user',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Tutor',
        ),
    ]