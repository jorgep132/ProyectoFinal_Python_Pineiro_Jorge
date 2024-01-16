from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def detalles_juegos(request):
    return render(request, 'detalles_juegos.html')

def categoria_juegos(request):
    return render(request,'categoria_juegos.html')

def prince_of_persia_the_lost_crown(request):
    return render(request, 'prince_of_persia_the_lost_crown.html')
