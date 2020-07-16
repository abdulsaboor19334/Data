# Generated by Django 3.0.7 on 2020-06-05 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotePad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('due', models.DateTimeField()),
                ('done', models.BooleanField(default=False)),
                ('priority', models.CharField(choices=[('L', 'LOW'), ('M', 'MEDIUM'), ('H', 'HIGH'), ('U', 'URGENT')], max_length=1)),
            ],
        ),
    ]