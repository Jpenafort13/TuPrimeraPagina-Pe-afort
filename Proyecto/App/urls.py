from django.urls import path
from App.views import *

urlpatterns = [
    #URLs principales
    path('', inicio, name="home"),
    
    #URLs formularios
    path('profeForm/', profeForm, name='profeForm'),
    path('alumnoForm/', alumnoForm, name='alumnoForm'),
    path('sedeForm/', sedeForm, name='sedeForm'),
    path('claseForm/', claseForm, name='claseForm'),
    path('buscarClase/', buscarClase, name='buscarClase')
]