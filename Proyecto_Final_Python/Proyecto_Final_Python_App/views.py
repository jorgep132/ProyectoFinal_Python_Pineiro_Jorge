from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from Proyecto_Final_Python_App.models import Juegos, UsuarioEstandar
from .forms import JuegosForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import ListView


def index(request):
    query = request.GET.get('q')

    # Obtén todos los juegos con mayor Metacritic ordenados de mayor a menor
    juegos = Juegos.objects.all().order_by('-metacritic')

    if query:
        # Filtra los juegos por título antes de limitar a los 4 primeros
        juegos = Juegos.objects.filter(title__icontains=query).order_by('-metacritic')

        if juegos.count() == 1:
            juego = juegos.first()
            return redirect('detalles_juego', juego_id=juego.id)
        else :
            return redirect('index')

    # Limita la consulta a los 4 primeros juegos con mayor Metacritic
    juegos = juegos[:4]

    context = {'juegos': juegos, 'query': query}
    return render(request, 'index.html', context)

##### Crear juegos desde la pag #########
def administrar_juegos(request):
    juegos = Juegos.objects.all()
    return render(request, 'administrar_juegos.html', {'juegos': juegos})


def agregar_juegos(request):
    if request.method == 'POST':
        form = JuegosForm(request.POST, request.FILES)
        if form.is_valid():
            # Guardar los datos si el formulario es válido
            form.save()
            # Limpiar el formulario para campos vacíos
            form = JuegosForm()
    else:
        # Si no es una solicitud POST, crear un nuevo formulario en blanco
        form = JuegosForm()

    return render(request, 'agregar_juegos.html', {'form': form})


def editar_juego(request, juego_id):
    juego = get_object_or_404(Juegos, id=juego_id)
    
    if request.method == 'POST':
        form = JuegosForm(request.POST, request.FILES, instance=juego)
        if form.is_valid():
            form.save()
            return redirect('administrar_juegos')
    else:
        form = JuegosForm(instance=juego)

    return render(request, 'editar_juego.html', {'form': form, 'juego': juego})

def borrar_juego(request, juego_id):
    juego = get_object_or_404(Juegos, id=juego_id)
    juego.delete()
    return redirect('administrar_juegos')



##########################################


### Manejo de usuarios ###

def usuarios_lista(request):
    usuarios = UsuarioEstandar.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})


class VistaJuegosLista(View):
    nombre_template = 'lista_juegos_A-Z.html'
    juegos_por_pag = 6

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        
        # Obtén todos los juegos ordenados alfabéticamente por título
        order_option = request.GET.get('order_option', 'asc')
        if order_option == 'asc':
            juegos = Juegos.objects.all().order_by('title')
        elif order_option == 'desc':
            juegos = Juegos.objects.all().order_by('-title')
        else:
            juegos = Juegos.objects.all().order_by('title')

        if query:
            # Filtra los juegos por título
            juegos = juegos.filter(title__icontains=query)

            if juegos.count() == 1:
                juego = juegos.first()
                return redirect('detalles_juego', juego_id=juego.id)

        # Limita la consulta a los 4 primeros juegos alfabéticamente
        mejores_juegos = Juegos.objects.all().order_by('-metacritic')[:4]

        paginator = Paginator(juegos, self.juegos_por_pag)
        page = request.GET.get('page')

        try:
            juegos_pagina = paginator.page(page)
        except PageNotAnInteger:
            juegos_pagina = paginator.page(1)
        except EmptyPage:
            juegos_pagina = paginator.page(paginator.num_pages)

        context = {
            'juegos_lista': juegos_pagina,
            'mejores_juegos': mejores_juegos,
            'query': query,
        }

        return render(request, self.nombre_template, context)



class VistaJuegosListaAlReves(View):
    nombre_template = 'lista_juegos_A-Z.html'
    juegos_por_pag = 6

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        juegos_total = Juegos.objects.all().order_by('title').reverse()  
        
        # Obtén todos los juegos con mayor Metacritic ordenados de mayor a menor
        juegos = Juegos.objects.all().order_by('-title')

        if query:
            # Filtra los juegos por título
            juegos = juegos.filter(title__icontains=query).order_by('-metacritic')

            if juegos.count() == 1:
                juego = juegos.first()
                return redirect('detalles_juego', juego_id=juego.id)

        # Limita la consulta a los 4 primeros juegos con mayor Metacritic
        mejores_juegos = Juegos.objects.all().order_by('-metacritic')[:4]

        paginator = Paginator(juegos, self.juegos_por_pag)
        page = request.GET.get('page')

        try:
            juegos_pagina = paginator.page(page)
        except PageNotAnInteger:
            juegos_pagina = paginator.page(1)
        except EmptyPage:
            juegos_pagina = paginator.page(paginator.num_pages)

        context = {
            'juegos_lista': juegos_pagina,
            'mejores_juegos': mejores_juegos,
            'query': query,
        }

        return render(request, self.nombre_template, context)
    
    
def detalles_juego(request, juego_id):
    juego = Juegos.objects.get(id=juego_id)
    return render(request, 'detalles_juegos.html', {'juego': juego})


def registro_usuario(request):
    query = request.GET.get('q')
    
    if query:
        juegos = Juegos.objects.filter(title__icontains=query)
        
        if juegos.count() == 1:
            juego = juegos.first()
            return redirect('detalles_juego', juego_id=juego.id)
        else:
            return redirect('registro')
    
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



