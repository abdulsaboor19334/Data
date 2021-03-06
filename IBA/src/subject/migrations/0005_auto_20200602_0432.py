# Generated by Django 3.0.6 on 2020-06-01 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0004_auto_20200602_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='enrolled_students',
            field=models.ManyToManyField(blank=True, to='subject.Student'),
        ),
        migrations.CreateModel(
            name='EnrollmentBBA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_1', models.ForeignKey(limit_choices_to={'offerend_to': 'BBA'}, on_delete=django.db.models.deletion.CASCADE, related_name='course1', to='subject.Courses')),
                ('course_2', models.ForeignKey(limit_choices_to={'offerend_to': 'BBA'}, on_delete=django.db.models.deletion.CASCADE, related_name='course2', to='subject.Courses')),
                ('course_3', models.ForeignKey(limit_choices_to={'offerend_to': 'BBA'}, on_delete=django.db.models.deletion.CASCADE, related_name='course3', to='subject.Courses')),
                ('course_4', models.ForeignKey(limit_choices_to={'offerend_to': 'BBA'}, on_delete=django.db.models.deletion.CASCADE, related_name='course4', to='subject.Courses')),
                ('course_5', models.ForeignKey(limit_choices_to={'offerend_to': 'BBA'}, on_delete=django.db.models.deletion.CASCADE, related_name='course5', to='subject.Courses')),
            ],
        ),
    ]
