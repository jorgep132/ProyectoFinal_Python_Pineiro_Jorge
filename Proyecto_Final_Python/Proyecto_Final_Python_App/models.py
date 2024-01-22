from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, AbstractUser
from django.core.validators import  MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.

from django.db import models

class Juegos(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    title = models.CharField(max_length=50, default='')
    subtitle = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=512, default='')
    image = models.ImageField(upload_to='media/img/juegos')
    image2 = models.ImageField(upload_to='media/img/juegos', default='')
    url = models.SlugField(max_length=255, unique=True, editable=False)
    genero1 = models.CharField(max_length=32, default='')
    genero2 = models.CharField(max_length=32, default='')
    genero3 = models.CharField(max_length=32, default='')
    desarrolladora = models.CharField(max_length=32, default='')
    lanzamiento = models.CharField(max_length=32, default='')
    metacritic = models.IntegerField(validators=[MaxValueValidator(100)], default=0)
    duracion = models.CharField(max_length=32, default='')
    plataforma = models.CharField(max_length=32, default='')
    trailer = models.URLField(default='')
    tienda = models.URLField(default='')

    def save(self, *args, **kwargs):
    # Generar la URL automáticamente basada en el ID del juego
        self.url = f'detalles_juego/{self.id}'
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('detalles_juego', kwargs={'juego_id': self.id})
    
    def __str__(self):
        return self.title

class UsuarioEstandarManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields['is_superuser']:
            extra_fields.setdefault('is_staff', True)
        return self.create_user(username, email, password, **extra_fields)

class UsuarioEstandar(AbstractUser):
    objects = UsuarioEstandarManager()

    def __str__(self):
        return self.username
    