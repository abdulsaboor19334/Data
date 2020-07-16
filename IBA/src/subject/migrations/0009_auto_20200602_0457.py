# Generated by Django 3.0.6 on 2020-06-01 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0008_auto_20200602_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollmentbba',
            name='course_1',
            field=models.ForeignKey(limit_choices_to={'offered_to_BBA': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course1_bba', to='subject.Courses'),
        ),
        migrations.AlterField(
            model_name='enrollmentbba',
            name='course_2',
            field=models.ForeignKey(limit_choices_to={'offered_to_BBA': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course2_bba', to='subject.Courses'),
        ),
        migrations.AlterField(
            model_name='enrollmentbba',
            name='course_3',
            field=models.ForeignKey(limit_choices_to={'offered_to_BBA': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course3_bba', to='subject.Courses'),
        ),
        migrations.AlterField(
            model_name='enrollmentbba',
            name='course_4',
            field=models.ForeignKey(limit_choices_to={'offered_to_BBA': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course4_bba', to='subject.Courses'),
        ),
        migrations.AlterField(
            model_name='enrollmentbba',
            name='course_5',
            field=models.ForeignKey(limit_choices_to={'offered_to_BBA': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course5_bba', to='subject.Courses'),
        ),
        migrations.CreateModel(
            name='EnrollmentAcf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_1', models.ForeignKey(limit_choices_to={'offered_to_acf': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course1_acf', to='subject.Courses')),
                ('course_2', models.ForeignKey(limit_choices_to={'offered_to_acf': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course2_acf', to='subject.Courses')),
                ('course_3', models.ForeignKey(limit_choices_to={'offered_to_acf': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course3_acf', to='subject.Courses')),
                ('course_4', models.ForeignKey(limit_choices_to={'offered_to_acf': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course4_acf', to='subject.Courses')),
                ('course_5', models.ForeignKey(limit_choices_to={'offered_to_acf': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course5_acf', to='subject.Courses')),
            ],
        ),
    ]