from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
# Create your views here.


def llamar_plantilla(request):
    nombre = "amadeus"
    apellido = "ovlac"
    diccionario = {"nombre": nombre,"apellido": apellido}
    plantilla = loader.get_template('test.html')
    respuesta = plantilla.render(diccionario)
    return HttpResponse(respuesta)


def sobremi(request):
    return render(request, "sobremi.html")