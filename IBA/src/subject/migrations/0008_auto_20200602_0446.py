# Generated by Django 3.0.6 on 2020-06-01 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0007_auto_20200602_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollmentbba',
            name='course_1',
            field=models.ForeignKey(limit_choices_to={'offered_to_BBA': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course1', to='subject.Courses'),
        ),
        migrations.AlterField(
            model_name='enrollmentbba',
            name='course_2',
            field=models.ForeignKey(limit_choices_to={'offered_to_BBA': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course2', to='subject.Courses'),
        ),
        migrations.AlterField(
            model_name='enrollmentbba',
            name='course_3',
            field=models.ForeignKey(limit_choices_to={'offered_to_BBA': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course3', to='subject.Courses'),
        ),
        migrations.AlterField(
            model_name='enrollmentbba',
            name='course_4',
            field=models.ForeignKey(limit_choices_to={'offered_to_BBA': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course4', to='subject.Courses'),
        ),
        migrations.AlterField(
            model_name='enrollmentbba',
            name='course_5',
            field=models.ForeignKey(limit_choices_to={'offered_to_BBA': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course5', to='subject.Courses'),
        ),
    ]
