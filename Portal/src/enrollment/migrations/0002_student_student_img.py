# Generated by Django 3.0.7 on 2020-06-05 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
