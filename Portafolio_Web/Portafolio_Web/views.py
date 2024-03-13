from django.http import HttpResponse
import datetime

def b1(request):
    return HttpResponse("Bienvenido a mi portafolio")

def fecha(request):
    hoy = datetime.datetime.now()
    respuesta = f"""
    <html>
    <h1> Hoy es {hoy} </h1>
    </html>
    """
    
    return HttpResponse(respuesta)


def bienvenido_template(request):
    
    miHml = open("")