# Generated by Django 3.0.7 on 2020-07-05 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20200705_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
