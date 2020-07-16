# Generated by Django 3.0.6 on 2020-06-01 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.IntegerField()),
                ('course_name', models.CharField(max_length=100)),
                ('offered_to', models.CharField(default='none', max_length=20)),
                ('instructor', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='enrolled_students',
        ),
        migrations.DeleteModel(
            name='Major',
        ),
        migrations.AddField(
            model_name='student',
            name='major',
            field=models.CharField(choices=[('acf', 'Accounting and Finance'), ('eco', ' BS ecnomics'), ('bba', 'BBA'), ('ecomath', 'Ecnomics and Math')], default='none', max_length=100),
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.AddField(
            model_name='courses',
            name='enrolled_students',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.Student'),
        ),
    ]
