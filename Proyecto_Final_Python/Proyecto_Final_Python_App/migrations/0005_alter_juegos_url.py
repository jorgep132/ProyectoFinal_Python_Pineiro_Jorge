# Generated by Django 5.0 on 2024-01-17 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto_Final_Python_App', '0004_juegos_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juegos',
            name='url',
            field=models.CharField(default='/default-url/', max_length=255),
        ),
    ]
