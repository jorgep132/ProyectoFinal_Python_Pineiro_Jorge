# Generated by Django 5.0 on 2024-01-22 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto_Final_Python_App', '0023_proximamente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proximamente',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]