# Generated by Django 5.0 on 2024-01-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto_Final_Python_App', '0021_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juegos',
            name='lanzamiento',
            field=models.DateField(),
        ),
    ]
