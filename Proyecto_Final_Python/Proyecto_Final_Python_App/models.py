from django.db import models


# Create your models here.

from django.db import models

class Juegos(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/')
    url = models.CharField(max_length=255, default='/default-url/')

    def __str__(self):
        return self.title