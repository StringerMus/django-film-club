# Generated by Django 4.2.13 on 2024-06-28 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0003_alter_movie_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
