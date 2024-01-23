from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django import forms
from django.urls import reverse
from Proyecto_Final_Python_App.models import Juegos, UsuarioEstandar, Comentario, Lanzamiento
from .forms import JuegosForm, UsuarioEstandarForm, AgregarComentarioForm, ActualizarComentarioForm, LanzamientoForm
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import ListView
from datetime import datetime, date


def index(request):
    '''
    Vista del inicio (index) de la web.
        
    '''
    fecha_actual = datetime.now() # Mostramos la fecha actual en el footer de la web.
    
    query = request.GET.get('q') # Definimos query para el buscador de la web.
    
    # Otenemos todos los juegos, y los ordenamos por metacritic, de mas alto a mas bajo, luego se mostrara del lado derecho de la web.
    juegos = Juegos.objects.all().order_by('-metacritic')
    
    # Obtenemos los lanzamientos (juegos que saldrán este año) y los ordenamos por fecha de lanzamiento, de menor a myor.
    lanzamientos = Lanzamiento.objects.all().order_by('fecha')

    if query:
        # Filtra los juegos por título antes de limitar a los 4 primeros, dado que solo se mostrará esa cantidad a la derecha, de mayor a menor.
        juegos = Juegos.objects.filter(title__icontains=query).order_by('-metacritic')

        # Condicional para enviarmos a la página del juego, si tenemos alguna coincidencia con la búsqueda. Si no encuentra nada, nos mandará al index.
        if juegos.count() == 1:
            juego = juegos.first()
            return redirect('detalles_juego', juego_id=juego.id)
        else :
            return redirect('index')

    # Limita la consulta a los 4 primeros juegos con mayor Metacritic.
    juegos = juegos[:4]

    context = {'juegos': juegos, 'query': query, 'fecha_actual': fecha_actual, 'lanzamientos':lanzamientos}
    return render(request, 'index.html', context)


# Bloque lanzamientos y las vistas para su CRUD #
def administrar_lanzamientos(request):
    '''
    Vista para ver y administrar los lanzamientos.
    '''
    lanzamientos = Lanzamiento.objects.all()
    return render(request, 'administrar_lanzamientos.html', {'lanzamientos': lanzamientos})

def agregar_lanzamientos(request):
    '''
    Vista para agregar lanzamientos.
    '''
    if request.method == 'POST':
        form = LanzamientoForm(request.POST, request.FILES)
        if form.is_valid():
            # Guardar los datos si el formulario es válido
            form.save()
            # Limpiar el formulario para campos vacíos
            form = LanzamientoForm()
    else:
        # Si no es una solicitud POST, crear un nuevo formulario en blanco.
        form = LanzamientoForm()

    return render(request, 'agregar_lanzamientos.html', {'form': form})


def editar_lanzamiento(request, lanzamiento_title):
    '''
    Vista para editar los lanzamientos.
    '''
    lanzamiento = get_object_or_404(Lanzamiento, title=lanzamiento_title) # Obtiene los lanzamientos

    if request.method == 'POST':
        form = LanzamientoForm(request.POST, request.FILES, instance=lanzamiento)
        if form.is_valid():
            # Si es valido, guaarda los datos.
            form.save()
            # Nos redirige nuevamente a administrar_lanzamientos, por si queremos editar, borrar o agregar otro.
            return redirect('administrar_lanzamientos')
    else:
        form = LanzamientoForm(instance=lanzamiento)

    return render(request, 'editar_lanzamiento.html', {'form': form, 'lanzamiento': lanzamiento})

def borrar_lanzamiento(request, lanzamiento_title):
    '''
    Vista para lanzamientos
    '''
    lanzamiento = get_object_or_404(Lanzamiento, title=lanzamiento_title)
    lanzamiento.delete()
    return redirect('administrar_lanzamientos')
# Fin bloque lanzamiento #



# Bloque juegos, incluyendo su CRUD #
def administrar_juegos(request):
    '''
    Vista para ver los juegos en la base de datos, editarlos, agregar o borrar (ABM)
    '''
    juegos = Juegos.objects.all().order_by('title') # Obtiene los juegos y los ordena por titulo en orden alfbético
    return render(request, 'administrar_juegos.html', {'juegos': juegos})

def agregar_juegos(request):
    '''
    Vista para agregar juegos.
    '''
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
    '''
    Vista para editar juegos.
    '''
    juego = get_object_or_404(Juegos, id=juego_id)

    if request.method == 'POST':
        form = JuegosForm(request.POST, request.FILES, instance=juego)
        if form.is_valid():
            # Si es valido, guarda los cambios.
            form.save()
            # Nos redirige nuevamente a ABM de juegos
            return redirect('administrar_juegos')
    else:
        # Al editar, establece el campo 'id' como no editable y oculto, dado que es una clave primaria. 
        # Realice este paso extra para evitar problemas de integridad en la base de datos.
        form = JuegosForm(instance=juego)
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['id'].widget = forms.HiddenInput()

    return render(request, 'editar_juego.html', {'form': form, 'juego': juego})

def borrar_juego(request, juego_id):
    '''
    Vista para borrar juegos.
    '''
    juego = get_object_or_404(Juegos, id=juego_id)
    juego.delete()
    return redirect('administrar_juegos')



# Clase vista para ver los juegos #
class VistaJuegosLista(View):
    nombre_template = 'lista_juegos_A-Z.html'
    # Limitamos a 6 juegos por página.
    juegos_por_pag = 6

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        
        # Obtén todos los juegos ordenados alfabéticamente, tomando como valor el titulo.
        order_option = request.GET.get('order_option', 'asc')
        if order_option == 'asc':
            juegos = Juegos.objects.all().order_by('title')
        elif order_option == 'desc':
            juegos = Juegos.objects.all().order_by('-title')
        else:
            juegos = Juegos.objects.all().order_by('title')

        # Buscador
        if query:
            # Filtra los juegos por título
            juegos = juegos.filter(title__icontains=query)

            if juegos.count() == 1:
                juego = juegos.first()
                return redirect('detalles_juego', juego_id=juego.id)
            else:
                return redirect(reverse('lista_juegos_A-Z'))
            
        # Mostrará unicamente los 4 juegos con mayor metacritic, en el lado derecho de la pantalla.
        mejores_juegos = Juegos.objects.all().order_by('-metacritic')[:4]

        # Paginamos, dado que solo se verán 6 por página.
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



# Clase vista para ver los juegos al revés, para poder ordenarlos de la Z a la A#
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
    juego = get_object_or_404(Juegos, id=juego_id)
    comentarios = Comentario.objects.filter(juego=juego)

    if request.method == 'POST':
        form = AgregarComentarioForm(request.POST)
        if form.is_valid():
            comentario_texto = form.cleaned_data['comentario']

            # No es necesario guardar el juego aquí, ya que solo estamos añadiendo un comentario
            # juego.save()

            if comentario_texto:
                # Crear el comentario asociado al juego
                Comentario.objects.create(juego=juego, autor=request.user.username, contenido=comentario_texto)

            # Redirigir a la página de detalles del juego después de procesar el formulario
            return HttpResponseRedirect(request.path_info)

    else:
        form = AgregarComentarioForm()

    return render(request, 'detalles_juegos.html', {'juego': juego, 'form': form, 'comentarios': comentarios})
# Fin del bloque juegos #




# Bloque de usuarios, CRUD #
def registro_usuario(request):
    '''
    Vista para registrarse en la web como usuario.
    '''
    
    # Agregamos el buscador
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

        # Validamos los posibles inconvenientes que podemos tener a la hora de iniciar sesion, y en base a eso arrojamos un error.
        errors = {}
        
        # Verificamos si estan todos los campos completos
        if not email or not username or not password:
            errors['error_mail'] = 'Todos los campos son obligatorios.'
        
        # Verificamos si el mail esta en uso
        if UsuarioEstandar.objects.filter(email=email).exists():
            errors['error_mail'] = 'Este correo electrónico ya está en uso.'

        # Verificamos si el usuario esta en uso, y también que cumpla cantidad de caracteres requeridos.
        if UsuarioEstandar.objects.filter(username=username).exists():
            errors['error_username'] = 'Este nombre de usuario ya está en uso.'
        elif len(username) < 6 or len(username) > 12:
            errors['error_username'] = 'El nombre de usuario debe tener entre 6 y 12 caracteres.'

        # Verificamos si la contraseña cumple con la longitud de caracteres
        if len(password) < 8 or len(password) > 16:
            errors['error_password'] = 'La contraseña debe tener entre 8 y 16 caracteres.'

        # Si hay errores, lo devuelve en base a cual sea, o cuales.
        if errors:
            return render(request, 'registro.html', {'errors': errors})

        # SI es admin, se crea un superuser, sino no.
        if is_admin:
            usuario_estandar = UsuarioEstandar.objects.create_superuser(username=username, email=email, password=password)
        else:
            usuario_estandar = UsuarioEstandar.objects.create_user(username=username, email=email, password=password)

        return redirect('iniciar_sesion')

    return render(request, 'registro.html')


# Decorador para la funcion de login
def redirect_authenticated_user(view_func):
    '''
    Decorador para no poder acceder a /iniciar_sesion si ya estamos logueados.
    '''
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index') 
        return view_func(request, *args, **kwargs)
    return wrapper

@redirect_authenticated_user
def login_usuario(request):
    '''
    Vista para iniciar sesion (login)
    '''
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



def administrar_usuarios(request):
    '''
    Vista para agregar, modificar o borrar usuarios (ABM)
    '''
    usuarios = UsuarioEstandar.objects.all()
    return render(request, 'administrar_usuarios.html', {'usuarios': usuarios})


def agregar_usuarios(request):
    '''
    Vista para agregar usuarios.
    '''
    if request.method == 'POST':
        form = UsuarioEstandarForm(request.POST, request.FILES)
        if form.is_valid():
            # Obtiene los datos del usuario, sin guardarlos.
            usuario = form.save(commit=False)
            # Hashea la contraseña antes de guardarla, para evitar errores a la hora de iniciar sesion, ya que si quiero utilizar la contraseña como texto plano
            # genera inconsistencias por la forma en la que trabaja Django con las auth.
            usuario.password = make_password(form.cleaned_data['password'])
            
            # Verifica si el usuario es administrador (superuser) o un usuario estándar. 
            # No tendrá importancia para efectuar cambios en el CRUD de las vistas.
            if form.cleaned_data['is_superuser']:
                usuario.is_staff = True
            
            # Guarda el usuario
            usuario.save()

            # Limpiar el formulario para campos vacíos
            form = UsuarioEstandarForm()
    else:
        # Si no es una solicitud POST, crear un nuevo formulario en blanco
        form = UsuarioEstandarForm()

    return render(request, 'agregar_usuarios.html', {'form': form})


def editar_usuario(request, usuario_username):
    '''
    Vista para editar usuarios
    '''
    usuario = get_object_or_404(UsuarioEstandar, username=usuario_username)

    if request.method == 'POST':
        form = UsuarioEstandarForm(request.POST, request.FILES, instance=usuario)
        
        if form.is_valid():
            # Hasheamos nuevamente la password.
            usuario.password = make_password(form.cleaned_data['password'])
            form.save()
            # Guardamos los cambios.
            return redirect('administrar_usuarios') 
    else:
        form = UsuarioEstandarForm(instance=usuario)

    return render(request, 'editar_usuario.html', {'form': form, 'usuario': usuario})

def borrar_usuario(request, usuario_username):
    '''
    Vista para borrar usuarios
    '''
    usuario = get_object_or_404(UsuarioEstandar, username=usuario_username)
    usuario.delete()
    return redirect('administrar_usuarios')
# Fin del bloque usuarios y su CRUD #


# Bloque de comentarios, CRUD #
class ActualizarComentarioView(View):
    '''
    Vista clase para actualizar los comentarios en la web.
    '''
    template_name = 'actualizar_comentario.html'

    def get(self, request, comentario_id):
        comentario = get_object_or_404(Comentario, id=comentario_id)
        form = ActualizarComentarioForm(instance=comentario)
        return render(request, self.template_name, {'form': form, 'comentario': comentario})

    def post(self, request, comentario_id):
        comentario = get_object_or_404(Comentario, id=comentario_id)
        form = ActualizarComentarioForm(request.POST, instance=comentario)

        if form.is_valid():
            form.save()
            return redirect('detalles_juego', juego_id=comentario.juego.id)

        return render(request, self.template_name, {'form': form, 'comentario': comentario})
    
class EliminarComentarioView(View):
    '''
    Vista clase para eliminar comentarios
    '''
    def get(self, request, comentario_id):
        comentario = get_object_or_404(Comentario, id=comentario_id)
        juego_id = comentario.juego.id
        comentario.delete()
        return redirect('detalles_juego', juego_id=juego_id)
# Fin del bloque de comentarios #





