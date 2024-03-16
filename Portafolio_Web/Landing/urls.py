from django.urls import path, include
from .views import *

urlpatterns = [
    path('',llamar_plantilla , name="home"),
]
