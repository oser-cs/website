# Generated by Django 2.0.2 on 2018-03-01 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tutoring', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutortutoringgroup',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Tutor'),
        ),
        migrations.AddField(
            model_name='tutortutoringgroup',
            name='tutoring_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutoring.TutoringGroup'),
        ),
        migrations.AddField(
            model_name='tutoringsession',
            name='tutoring_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutoring_sessions', to='tutoring.TutoringGroup', verbose_name='groupe de tutorat'),
        ),
        migrations.AddField(
            model_name='tutoringgroup',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tutoring_groups', to='tutoring.School', verbose_name='lycée'),
        ),
        migrations.AddField(
            model_name='tutoringgroup',
            name='tutors',
            field=models.ManyToManyField(blank=True, related_name='tutoring_groups', through='tutoring.TutorTutoringGroup', to='users.Tutor', verbose_name='tuteurs'),
        ),
    ]
