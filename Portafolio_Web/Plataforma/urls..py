from django.urls import path, include
from .views import *

urlpatterns = [
    path('Plataforma/', include('Plataforma.urls')),
]
