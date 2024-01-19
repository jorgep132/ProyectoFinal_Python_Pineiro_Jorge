from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, AbstractUser
from django.core.validators import  MaxValueValidator


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
    desarrolladora = models.CharField(max_length=32, default='')
    lanzamiento = models.CharField(max_length=32, default='')
    metacritic = models.IntegerField(validators=[MaxValueValidator(100)], default=0)
    duracion = models.CharField(max_length=32, default='')
    plataforma = models.CharField(max_length=32, default='')
    trailer = models.URLField(default='')
    tienda = models.URLField(default='')

    def __str__(self):
        return self.title
    
    
# class UsuarioEstandarManager(BaseUserManager):
#     def create_user(self, username, email, password=None, **extra_fields):

#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

# class UsuarioEstandar(AbstractBaseUser):
#     username = models.CharField(max_length=12, unique=True)
#     email = models.EmailField(max_length=64, unique=True)
#     password = models.CharField(max_length=16)

#     objects = UsuarioEstandarManager()

#     def __str__(self):
#         return self.username

# class UsuarioEstandarManager(BaseUserManager):
#     def create_user(self, username, email, password=None, **extra_fields):
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

# class UsuarioEstandar(AbstractBaseUser):
#     username = models.CharField(max_length=12, unique=True)
#     email = models.EmailField(max_length=64, unique=True)
#     # Utiliza el campo de contraseña proporcionado por AbstractBaseUser
#     password = models.CharField(max_length=16)
    
#     # Campos adicionales si es necesario
#     # ...

#     objects = UsuarioEstandarManager()

#     USERNAME_FIELD = 'username'
#     EMAIL_FIELD = 'email'
#     REQUIRED_FIELDS = ['email']  # Añade aquí cualquier campo adicional requerido al crear un usuario

#     def __str__(self):
#         return self.username


# class UsuarioEstandarManager(BaseUserManager):
#     def create_user(self, username, email, password=None, is_admin=False, **extra_fields):
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, is_admin=is_admin, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password=None, **extra_fields):
#         return self.create_user(username, email, password, is_admin=True, **extra_fields)

# class UsuarioEstandar(AbstractBaseUser):
#     username = models.CharField(max_length=12, unique=True)
#     email = models.EmailField(max_length=64, unique=True)
#     password = models.CharField(max_length=16)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     objects = UsuarioEstandarManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']

#     def __str__(self):
#         return self.username


# class UsuarioEstandarManager(BaseUserManager):
#     def create_user(self, username, email, password=None, is_staff=False, is_superuser=False, **extra_fields):
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password=None, **extra_fields):
#         return self.create_user(username, email, password, is_staff=True, is_superuser=True, **extra_fields)

# class UsuarioEstandar(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=12, unique=True)
#     email = models.EmailField(max_length=64, unique=True)
#     password = models.CharField(max_length=16)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     objects = UsuarioEstandarManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']

#     def __str__(self):
#         return self.username

#     # Implementar los métodos necesarios para PermissionsMixin
#     def has_perm(self, perm, obj=None):
#         return self.is_superuser

#     def has_module_perms(self, app_label):
#         return self.is_superuser


# class UsuarioEstandarManager(BaseUserManager):
#     def create_user(self, username, email, password=None, **extra_fields):
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(username, email, password, **extra_fields)

# class UsuarioEstandar(AbstractUser, PermissionsMixin):
#     email = models.EmailField(max_length=64, unique=True)
#     is_staff = models.BooleanField(default=False)

#     objects = UsuarioEstandarManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']

#     def __str__(self):
#         return self.username


# class UsuarioEstandarManager(BaseUserManager):
#     def create_user(self, username, email, password=None, **extra_fields):
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')


class UsuarioEstandarManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

class UsuarioEstandar(AbstractUser):
    objects = UsuarioEstandarManager()

    def __str__(self):
        return self.username