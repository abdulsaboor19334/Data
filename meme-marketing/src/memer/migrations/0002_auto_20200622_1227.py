# Generated by Django 3.0.7 on 2020-06-22 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='memeimages',
            options={'verbose_name_plural': 'Meme Images'},
        ),
        migrations.AlterField(
            model_name='meme',
            name='score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
