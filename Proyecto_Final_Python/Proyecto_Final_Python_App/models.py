from django.db import models


# Create your models here.

from django.db import models

class Juegos(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    title = models.CharField(max_length=50, default='')
    subtitle = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=512, default='')
    image = models.ImageField(upload_to='static/img/juegos')
    image2 = models.ImageField(upload_to='static/img/juegos', default='')
    url = models.CharField(max_length=255, default='/default-url/')
    genero1 = models.CharField(max_length=32, default='')
    genero2 = models.CharField(max_length=32, default='')
    genero3 = models.CharField(max_length=32, default='')

    def __str__(self):
        return self.title