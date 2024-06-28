# Generated by Django 4.2.13 on 2024-06-28 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0002_remove_movie_excerpt_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(error_messages={'unique': 'This title already exists.'}, max_length=200, unique=True),
        ),
    ]
