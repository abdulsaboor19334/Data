# Generated by Django 3.0.6 on 2020-06-01 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0005_auto_20200602_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='offered_to',
            field=models.CharField(choices=[('acf', 'Accounting and Finance'), ('eco', ' BS ecnomics'), ('bba', 'BBA'), ('ecomath', 'Ecnomics and Math')], default='none', max_length=20),
        ),
    ]
