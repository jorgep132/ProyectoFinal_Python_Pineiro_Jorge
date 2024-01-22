# Generated by Django 5.0 on 2024-01-22 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto_Final_Python_App', '0022_alter_juegos_lanzamiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proximamente',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=50)),
                ('image', models.ImageField(upload_to='media/img/juegos')),
                ('lanzamiento', models.DateField()),
            ],
        ),
    ]
