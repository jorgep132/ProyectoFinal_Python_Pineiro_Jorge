from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from Proyecto_Final_Python_App.models import Juegos
from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.


def index(request):
    return render(request, 'index.html')

def lista_juegos(request):
    return render(request, 'lista_juegos.html')

def prince_of_persia_the_lost_crown(request):
    return render(request, 'prince_of_persia_the_lost_crown.html')

def persona3_reload(request):
    return render(request, 'persona3_reload.html')

def ffvii_rebirth(request):
    return render(request, 'ffvii_rebirth.html')

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

