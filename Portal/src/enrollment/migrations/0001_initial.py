# Generated by Django 3.0.7 on 2020-06-04 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('course_code', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('course_name', models.CharField(max_length=100)),
                ('offered_to_BBA', models.BooleanField(default=False)),
                ('offered_to_acf', models.BooleanField(default=False)),
                ('offered_to_eco', models.BooleanField(default=False)),
                ('offered_to_ecomath', models.BooleanField(default=False)),
                ('instructor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('erp', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('enrolled_in', models.DateTimeField(auto_now_add=True)),
                ('major', models.CharField(choices=[('acf', 'Accounting and Finance'), ('eco', ' BS ecnomics'), ('bba', 'BBA'), ('ecomath', 'Ecnomics and Math')], default='none', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EnrollmentBBA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_1', models.ForeignKey(limit_choices_to={'offered_to_BBA': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course1_bba', to='enrollment.Courses')),
                ('choice_2', models.ForeignKey(limit_choices_to={'offered_to_BBA': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course2_bba', to='enrollment.Courses')),
                ('choice_3', models.ForeignKey(limit_choices_to={'offered_to_BBA': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course3_bba', to='enrollment.Courses')),
                ('choice_4', models.ForeignKey(limit_choices_to={'offered_to_BBA': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course4_bba', to='enrollment.Courses')),
                ('choice_5', models.ForeignKey(limit_choices_to={'offered_to_BBA': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course5_bba', to='enrollment.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='EnrollmentAcf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_1', models.ForeignKey(limit_choices_to={'offered_to_acf': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course1_acf', to='enrollment.Courses')),
                ('course_2', models.ForeignKey(limit_choices_to={'offered_to_acf': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course2_acf', to='enrollment.Courses')),
                ('course_3', models.ForeignKey(limit_choices_to={'offered_to_acf': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course3_acf', to='enrollment.Courses')),
                ('course_4', models.ForeignKey(limit_choices_to={'offered_to_acf': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course4_acf', to='enrollment.Courses')),
                ('course_5', models.ForeignKey(limit_choices_to={'offered_to_acf': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course5_acf', to='enrollment.Courses')),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='enrolled_students',
            field=models.ManyToManyField(blank=True, to='enrollment.Student'),
        ),
    ]
