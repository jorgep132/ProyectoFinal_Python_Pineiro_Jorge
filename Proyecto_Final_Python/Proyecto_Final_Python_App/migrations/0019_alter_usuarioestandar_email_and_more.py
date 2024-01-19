# Generated by Django 5.0 on 2024-01-19 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto_Final_Python_App', '0018_alter_usuarioestandar_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarioestandar',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='usuarioestandar',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
