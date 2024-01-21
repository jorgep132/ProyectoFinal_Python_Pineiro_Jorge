from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from Proyecto_Final_Python_App.views import index, detalles_juego, registro_usuario, login_usuario, usuarios_lista, agregar_juegos, VistaJuegosLista, VistaJuegosListaAlReves



urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='index'),
    path('lista_juegos_A-Z/', VistaJuegosLista.as_view(), name='lista_juegos_A-Z'),
    path('lista_juegos_Z-A/', VistaJuegosListaAlReves.as_view(), name='lista_juegos_Z-A'),
    path('detalles_juego/<str:juego_id>/', detalles_juego, name='detalles_juego'),
    path('iniciar_sesion/', login_usuario, name='iniciar_sesion'),
    path('registro/', registro_usuario, name='registro'),
    path('cerrar_sesion/', LogoutView.as_view(next_page='index'), name='cerrar_sesion'),
    path('usuarios/', usuarios_lista, name='usuarios'),
    path('agregar_juegos/', agregar_juegos, name='agregar_juegos'),
    
]
 

