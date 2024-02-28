from django.db import models
from django import forms
# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    
    
    def __str__(self):
        return f"{self.nombre}"
    
    
class Servicios(models.Model):
    servicio = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.servicio}"
    

class Proyecto(models.Model):
    proyecto = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.proyecto}"
    

class Proyecto_Card(models.Model):
    proyecto = Proyecto.proyecto
    def __str__(self):
        return f"{self.proyecto}"
    