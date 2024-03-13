from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
# Create your views here.


def llamar_plantilla(request):
    nombre = "amadeus"
    apellido = "ovlac"
    diccionario = {"nombre": nombre,"apellido": apellido}
    plantilla = loader.get_template('test.html')
    miContexto = Context(diccionario)
    respuesta = plantilla.render(miContexto)
    return HttpResponse(respuesta)