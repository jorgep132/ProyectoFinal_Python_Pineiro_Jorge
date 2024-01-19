# Generated by Django 5.0 on 2024-01-19 12:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto_Final_Python_App', '0013_alter_usuarioestandar_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrarUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]