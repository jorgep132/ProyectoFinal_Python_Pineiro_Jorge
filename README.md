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
Vistas, o páginas, a las que podemos navegar dentro de la web.
***

**Inicio**:
  - Descripción: Vista del inicio, index o home, de la web. Es lo primero que se encuentra el usuario al ingresar a la página.
  - Contenido:
    - Slide con tres juegos (elegidos por mi) a modo de presentación.
    - Sidebar con un TOP de los 4 juegos con mayor metacritic registrados en la web.
    - Próximos lanzamientos, ordenados por fecha de salida.

**Administrar lanzamientos**:
  - Descripción: Vista con el listado de todos los lanzamientos con sus atributos, y acciones sobre estos.
  - Atributos:
    - lanzamiento.title: Titulo del lanzamiento
    - lanzamiento.fecha: Fecha de salida
    - lanzamiento.trailer: Link con un trailer oficial.
- Acciones:
  - Editar: editar lanzamientos cargados
  - Borrar: borrar lanzamientos cargados
  - Agregar lanzamiento: agregar un nuevo lanzamiento
  
3. **Estudiantes**:
  - Descripción: Este modelo contiene un formulario de carga de datos de estudiantes:
  - Atributos:
    - nombre_estudiante
    - apellido_estudiante
    - email_estudiante
4. **Entregables**:
  - Descripción: Este modelo contiene un formulario de carga de datos de las entregas de los estudiantes:
  - Atributos:
    - nombre_estudiantes
    - fecha_entrga
    - entregado
    - 
Estos modelos son fundamentales para el funcionamiento del proyecto, ya que abarcan aspectos clave como la información de los estudiantes, los detalles de los cursos y el seguimiento de las entregas.

***
## Utilización
***
Seguí estos pasos para probar la funcionalidad del programa:
1. **Inicio/Index:**
   - Ubica el modelo "Inicio" en el directorio `Entrega3/models`.
   - Ejecuta el formulario de búsqueda de cursos utilizando el número de camada del curso.

2. **Carga de Datos de Cursos:**
   - Ubica el modelo "Cursos" en `Entrega3/models`.
   - Utiliza el formulario de carga de datos de cursos en la interfaz de administrador o la ruta específica.

3. **Carga de Datos de Estudiantes:**
   - Ubica el modelo "Estudiantes" en `Entrega3/models`.
   - Utiliza el formulario de carga de datos de cursos en la interfaz de administrador o la ruta específica.

4. **Carga de Datos de Entregables:**
   - Ubica al modelo "Entregables" en `Entrega3/models`.
   - Utiliza el formulario de carga de datos de cursos en la interfaz de administrador o la ruta específica.

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
   $ git clone [jorgep132/Tercer-Pre-Entrega-Jorge-Pineiro](https://github.com/jorgep132/Tercer-Pre-Entrega-Jorge-Pineiro)
2. Navega al directorio del proyecto:
  $ cd path/to/the/project
3. Instala las dependencias:
  $ npm install
4. Inicia el proyecto:
  $ npm start
