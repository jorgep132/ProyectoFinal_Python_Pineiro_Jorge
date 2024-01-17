# Generated by Django 5.0 on 2024-01-17 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto_Final_Python_App', '0002_product_delete_categoriajuego'),
    ]

    operations = [
        migrations.CreateModel(
            name='Juegos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='product_images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
