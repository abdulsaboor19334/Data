# Generated by Django 3.0.7 on 2020-06-12 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='detail',
            field=models.TextField(default='The detail for this book is not avalible'),
        ),
        migrations.CreateModel(
            name='Solutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution_number', models.IntegerField()),
                ('solution', models.ImageField(upload_to='')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Exercises')),
            ],
        ),
    ]