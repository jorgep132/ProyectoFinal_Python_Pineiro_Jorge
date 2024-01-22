from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from Proyecto_Final_Python_App.views import index, detalles_juego, registro_usuario, login_usuario, administrar_usuarios, agregar_usuarios, editar_usuario, borrar_usuario, agregar_juegos,editar_juego, borrar_juego, administrar_juegos, ActualizarComentarioView, EliminarComentarioView, VistaJuegosLista, VistaJuegosListaAlReves



urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='index'),
    path('lista_juegos_A-Z/', VistaJuegosLista.as_view(), name='lista_juegos_A-Z'),
    path('lista_juegos_Z-A/', VistaJuegosListaAlReves.as_view(), name='lista_juegos_Z-A'),
    path('detalles_juego/<str:juego_id>/', detalles_juego, name='detalles_juego'),
    path('iniciar_sesion/', login_usuario, name='iniciar_sesion'),
    path('registro/', registro_usuario, name='registro'),
    path('cerrar_sesion/', LogoutView.as_view(next_page='index'), name='cerrar_sesion'),
    path('administrar_usuarios/', administrar_usuarios, name='administrar_usuarios'),
    path('administrar_usuarios/agregar_usuarios', agregar_usuarios, name='agregar_usuarios'),
    path('administrar_usuarios/editar_usuario/<str:usuario_username>', editar_usuario, name='editar_usuario'),
    path('administrar_usuarios/borrar_usuario/<str:usuario_username>', borrar_usuario, name='borrar_usuario'),
    path('administrar_juegos/', administrar_juegos, name='administrar_juegos'),
    path('administrar_juegos/agregar_juegos/', agregar_juegos, name='agregar_juegos'),
    path('administrar_juegos/editar_juego/<str:juego_id>/', editar_juego, name='editar_juego'),
    path('administrar_juegos/borrar_juego/<str:juego_id>/', borrar_juego, name='borrar_juego'),
    path('actualizar_comentario/<int:comentario_id>/', ActualizarComentarioView.as_view(), name='actualizar_comentario'),
    path('eliminar_comentario/<int:comentario_id>/', EliminarComentarioView.as_view(), name='eliminar_comentario'),
    
]
 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)