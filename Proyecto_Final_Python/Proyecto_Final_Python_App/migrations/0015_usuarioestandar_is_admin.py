# Generated by Django 5.0 on 2024-01-19 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto_Final_Python_App', '0014_alter_usuarioestandar_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarioestandar',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
