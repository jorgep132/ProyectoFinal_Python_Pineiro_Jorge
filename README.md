# Proyecto Final / Coderhouse Python - 50190
***
Página web sobre videojuegos, donde se pueden visualizar datos de estos y próximos lanzamientos.
***

### Información general de la web
En este proyecto podrás navegar a través de una web, completamente funcional, para encontrar información de algunos videojuegos, elegidos por opinión propio y/o por tener gran impacto en el medio.
La página consta con características generales, las cuales serán accesibles, y visualizadas, en todas las páginas que contiene (exceptuando las vistas ideadas para el CRUD/ABM de los datos)
Contenido general de la web:
  - Buscador (navbar)
  - Favicon
  - Header:
    - Acceso a las demás páginas de la web
    - Logo
    - Acceso a la administración de información (CRUD/ABM) de cada modelo.
    - Inicio de sesión mediante ícono
    - Cierre de sesión
  - Footer:
    - Acceso a las demás páginas de la web
    - Nombre del autor
    - Logo
    - Botón back to top

***
## Templates
***

**Inicio**:
  - Descripción: Inicio, index o home, de la web. Es lo primero que se encuentra el usuario al ingresar a la página.
  - Template: index.html
  - Contenido:
    - Slide con tres juegos (elegidos por mi) a modo de presentación.
    - Sidebar con un TOP de los 4 juegos con mayor metacritic registrados en la web.
    - Próximos lanzamientos, ordenados por fecha de salida.

**Administrar lanzamientos**:
  - Descripción: Listado de todos los lanzamientos con sus atributos y acciones sobre estos.
  - Template: administrar_lanzamientos.html
  - Atributos utilizados:
    - lanzamiento.title: Titulo del lanzamiento
    - lanzamiento.fecha: Fecha de salida
    - lanzamiento.trailer: Link con un trailer oficial.
  - Acciones:
    - Editar: editar lanzamientos 
    - Borrar: borrar lanzamientos 
    - Agregar lanzamiento: agregar un nuevo lanzamiento
  
**Administrar juegos**:
  - Descripción: Listado de todos los juegos con algunos de sus atributos y acciones sobre estos.
  - Template: administrar_juegos.html
  - Atributos utilizados:
    - juego.id: ID del juego. Funciona como clave primaria, es el único atributo no modificable.
    - juego.title: Título del juego.
  - Acciones:
    - Editar: editar juegos  
    - Borrar: borrar juegos 
    - Agregar lanzamiento: agregar un nuevo juego

**Administrar usuarios**:
  - Descripción: Listado de todos los usuarios con sus atributos y acciones sobre estos.
  - Template: administrar_usuarios.html
  - Atributos utilizados:
    - usuario.username: Nombre de usuario
    - usuario.password: Contraseña del usuario
    - usuario.email: Mail del usuario
    - usuario.is_superuser: Indica si el usuario es administrador o no (usuario estándar)
  - Acciones:
    - Editar: editar usuarios
    - Borrar: borrar usuarios
    - Agregar lanzamiento: agregar un nuevo usuario

**Lista de juegos (A-Z)**:
  - Descripción: Listado de juegos con su metacritic, duracion y título, ordenados de la A-Z.
  - Template: lista_juegos_A-Z.html
  - Atributos utilizados:
    - juego.title: Titulo del juego
    - juego.image2: Segunda imagen para mostrar del juego.
    - juego.metacritic: Puntuación de Metacritic
    - juego.duracion: Duración estimada del título
    - juego.genero1: Genero del juego
    - juego.genero2: Otro genero del juego
    - juego.genero3: Otro genero del juego
    - juego.url: al seleccionarlo nos lleva directamente a /detalles_juego/<str:juego_id>/ donde podremos ver la informacion del juego.
  - Acciones:
    - Ordenar por: permite ordenar los juegos por título, de la A-Z
    - Redireccionar: podemos elegir cualquier juego, y nos redireccionará a su respectiva web, con sus detalles.
    - Paginación: nos va a mostrar solamente 6 juegos por pagina, donde podemos avanzar a la siguiente y continuar con el listado.

**Lista de juegos (Z-A)**:
  - Descripción: Lista que hereda toda la información de lista_juegos_A-Z.html pero muestra los juegos ordenados de la Z a la A.
  - Template: lista_juegos_Z-A.html

**Detalles juego**
  - Descripción: Trae la información del juego a través de su ID. Muestra los comentarios que se realizaron del juego.
  - Template: detalles_juegos.html
  - URL: detalles_juego/<str:juego_id>/
  - Atributos utilizados:
    - juego.id: ID del juego. Funciona como primary key. 
    - juego.title: Titulo del juego
    - juego.subtitle: Subtitulo del juego.
    - juego.description: Breve descripción sobre el juego.
    - juego.image: Primera imagen para mostrar del juego, seria una portada.
    - juego.metacritic: Puntuación de Metacritic
    - juego.duracion: Duración estimada del título
    - juego.genero1: Genero del juego
    - juego.genero2: Otro genero del juego
    - juego.genero3: Otro genero del juego
    - juego.lanzamiento: Fecha en la que se lanzó el juego.
    - juego.plataforma: Plataforma donde se puede jugar
    - juego.desarrolladora: Empresa que desarrolló el juego.
    - comentario.contenido: Contenido del comentario.
    - comentario.autor: Autor del comentario.
    - comentario.fecha_creacion: Fecha y hora en la que se publicó el comentario.
  - Acciones:
    - Ordenar por: permite ordenar los juegos por título, de la A-Z
    - Redireccionar: podemos elegir cualquier juego, y nos redireccionará a su respectiva web, con sus detalles.
    - Paginación: nos va a mostrar solamente 6 juegos por pagina, donde podemos avanzar a la siguiente y continuar con el listado.
    - Actualizar comentario: permite modificar los comentarios
    - Borrar comentario: Permite borrar comentarios.
  
**Iniciar sesión**
  - Descripción: Login para que el usuario inicie sesión en la web.
  - Template: login.html
  - Atributos utilizados:
    - usuario.username: Toma el nombre de usuario para validarlo
    - usuario.password: Valida la contraseña del usuario.
  - Acciones:
    - Validar: valida que el usuario haya ingresado los datos correctamente. Si hay errores, se mostrarán hasta que ingrese correctamente.
    - Redirigir: Si se valida el usuario, se enviará al inicio.

**Registro**
  - Descripción: Registro de usuarios
  - Template: registro.html
  - Atributos utilizados:
    - usuario.username:  Nombre de usuario
    - usuario.password: Contraseña de usuario
    - usuario.email: Mail asignado al usuario
  - Acciones:
      - Validar: verifica que el usuario cumpla con los requisitos (cantidad de caracteres) y/o que no este en uso. Valida también que la contraseña cumpla con la longitud de caracteres.
      - Redirect: En caso de que se registre correctamente, el usuario será redirigido para iniciar sesion.

**Sobre mi**
- Descripción: Breve descripción sobre mi, un poco de información.
- Template: about.html

***
## Modelos
***
Juegos
  - Descripción: Modelo realizado para guardar la información de los juegos.
  - Atributos:
    - id = Clave primaria con el ID del juego
    - title = Título del juego
    - subtitle = Subtítulo del juego
    - description = Breve descripción del juego
    - image = Imagen del juego
    - image2 = Imagen del juego
    - url = URL asociada al juego. /detalles_juego/<str:juego_id>/ Se agrega automaticamente el ID del juego. Este campo se autocompleta.
    - genero1 = Genero del juego
    - genero2 = Genero del juego
    - genero3 = Genero del juego
    - desarrolladora = Empresa que desarrolló el juego.
    - lanzamiento = Fecha de lanzamiento
    - metacritic = Puntaje en Metacritic
    - duracion = Duración estimada del juego
    - plataforma = Plataforma donde se puede jugar
    - trailer = link al trailer del juego
    - tienda = link a la tienda oficial del juego

Lanzamiento
  - Descripción: Modelo con información de los lanzamientos.
  - Atributos:
    - title: Titulo del lanzamiento
    - image: Imagen del lanzamiento, o portada.
    - fecha: Fecha de lanzamiento.
    - trailer: Link con el trailer oficial del juego.

UsuarioEstandarManager
  - Descripción: Manejador de usuarios, utiliza BaseUserManager
  - Atributos:
    - email: Mail que tendra asociado el usuario.
    - user: Username del usuario
    - password: Contraseña del usuario
    - is_superuser: Define si el usuario sera administrador, es decir, si tendra permisos para acceder al /admin y gestionar las bases de datos.

UsuarioEstandar
  - Descripción: Utiliza AbstractUser y toma como objeto UsuarioEstandarManager

Comentario
  - Descripción: Comentarios que se pueden realizar en los detalles del juego elegido
    Atributos:
      - juego: Titulo del juego donde se va a comentar.
      - autor: Autor que realizó el comentario
      - contenido: Contendio del comentario
      - fecha_creacion: Fecha en la que se publicó el comentairo.


***
## Herramientas y tecnologías utilizadas
***
Disstintas tecnologías utilizadas:
* Visual Studio Code (https://code.visualstudio.com/): Version 1.85.1
* Python: Version 3.11.7
* Django: Version 23.3.1

***
## Instalación
Sigue el paso a paso para poder instalar el proyecto:
1. Clona el repositorio:
   $ git clone [jorgep132/Tercer-Pre-Entrega-Jorge-Pineiro](https://github.com/jorgep132/Tercer-Pre-Entrega-Jorge-Pineiro](https://github.com/jorgep132/ProyectoFinal_Python_Pineiro_Jorge))
2. Navega al directorio del proyecto:
  $ cd path/to/the/project
3. Instala las dependencias:
  $ npm install
4. Inicia el proyecto:
  $ npm start
