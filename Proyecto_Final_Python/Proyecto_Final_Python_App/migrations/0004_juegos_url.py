# Generated by Django 5.0 on 2024-01-17 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto_Final_Python_App', '0003_juegos_delete_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='juegos',
            name='url',
            field=models.URLField(default=2),
            preserve_default=False,
        ),
    ]
