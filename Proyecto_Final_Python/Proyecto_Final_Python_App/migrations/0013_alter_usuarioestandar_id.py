# Generated by Django 5.0 on 2024-01-19 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto_Final_Python_App', '0012_usuarioestandar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarioestandar',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
