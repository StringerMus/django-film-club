# Generated by Django 4.2.13 on 2024-06-29 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='excerpt',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
