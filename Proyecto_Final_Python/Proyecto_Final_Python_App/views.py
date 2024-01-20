from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from Proyecto_Final_Python_App.models import Juegos, UsuarioEstandar
from Proyecto_Final_Python_App.forms import UsuarioEstandarForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import ListView


# Create your views here.


def index(request):
    return render(request, 'index.html')

def lista_juegos(request):
    return render(request, 'lista_juegos.html')


### Manejo de usuarios ###

def usuarios_lista(request):
    usuarios = UsuarioEstandar.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})





class VistaJuegosLista(View):
    nombre_template = 'lista_juegos_A-Z.html'
    juegos_por_pag = 6

    def get(self, request, *args, **kwargs):
        juegos_total = Juegos.objects.all().order_by('title')

        paginator = Paginator(juegos_total, self.juegos_por_pag)
        page = request.GET.get('page')

        try:
            juegos = paginator.page(page)
        except PageNotAnInteger:
            juegos = paginator.page(1)
        except EmptyPage:
            juegos = paginator.page(paginator.num_pages)

        context = {
            'juegos_lista': juegos,
        }

        return render(request, self.nombre_template, context)
    

class VistaJuegosListaAlReves(View):
    nombre_template = 'lista_juegos_Z-A.html'
    juegos_por_pag = 6

    def get(self, request, *args, **kwargs):
        juegos_total = Juegos.objects.all().order_by('title').reverse()  

        paginator = Paginator(juegos_total, self.juegos_por_pag)
        page = request.GET.get('page')

        try:
            juegos = paginator.page(page)
        except PageNotAnInteger:
            juegos = paginator.page(1)
        except EmptyPage:
            juegos = paginator.page(paginator.num_pages)

        context = {
            'juegos_lista': juegos,
        }

        return render(request, self.nombre_template, context)
    
    
def detalles_juego(request, juego_id):
    juego = Juegos.objects.get(id=juego_id)
    return render(request, 'detalles_juegos.html', {'juego': juego})

def registro_usuario(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        is_admin = request.POST.get('is_admin', False)

        errors = {}

        if not email or not username or not password:
            errors['error_mail'] = 'Todos los campos son obligatorios.'

        if UsuarioEstandar.objects.filter(email=email).exists():
            errors['error_mail'] = 'Este correo electrónico ya está en uso.'

        if UsuarioEstandar.objects.filter(username=username).exists():
            errors['error_username'] = 'Este nombre de usuario ya está en uso.'
        elif len(username) < 6 or len(username) > 12:
            errors['error_username'] = 'El nombre de usuario debe tener entre 6 y 12 caracteres.'

        if len(password) < 8 or len(password) > 16:
            errors['error_password'] = 'La contraseña debe tener entre 8 y 16 caracteres.'

        if errors:
            return render(request, 'registro.html', {'errors': errors})

        if is_admin:
            usuario_estandar = UsuarioEstandar.objects.create_superuser(username=username, email=email, password=password)
        else:
            usuario_estandar = UsuarioEstandar.objects.create_user(username=username, email=email, password=password)

        return redirect('index')

    return render(request, 'registro.html')


## Decorador para no poder acceder a la vista de iniciar_sesion si el usuario ya se encuentra logueado
def redirect_authenticated_user(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')  # Cambia 'index' por el nombre de tu vista de inicio
        return view_func(request, *args, **kwargs)
    return wrapper


@redirect_authenticated_user
def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(request, username=username, password=password)
    
        if user is not None and user.is_active:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos.'})
        
    return render(request, 'login.html')



