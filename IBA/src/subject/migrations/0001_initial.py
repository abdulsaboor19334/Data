# Generated by Django 3.0.6 on 2020-06-01 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major_name', models.CharField(max_length=100)),
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
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.IntegerField()),
                ('course_name', models.CharField(max_length=100)),
                ('instructor', models.CharField(max_length=100)),
                ('enrolled_students', models.ForeignKey(limit_choices_to=45, null=True, on_delete=django.db.models.deletion.SET_NULL, to='subject.Student')),
            ],
        ),
    ]
