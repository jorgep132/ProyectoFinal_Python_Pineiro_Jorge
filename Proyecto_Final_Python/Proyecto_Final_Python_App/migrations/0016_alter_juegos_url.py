# Generated by Django 5.0 on 2024-01-21 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto_Final_Python_App', '0015_delete_borrarusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juegos',
            name='url',
            field=models.SlugField(editable=False, max_length=255, unique=True),
        ),
    ]
