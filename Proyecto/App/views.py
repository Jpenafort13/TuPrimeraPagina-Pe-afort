from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.http.request import QueryDict
from App.models import *
from App.forms import *

# Create your views here.
def inicio(request):
    return render(request, "App/index.html")


def profeForm(request):
    if request.method == 'POST':
        miFormulario = ProfeForm(request.POST) 
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            info = Profe(nombre = info['nombre'], apellido = info['apellido'], especialidad = info['especialidad'])
            info.save()
            return render(request, 'App/index.html')
    else:
        miFormulario = ProfeForm()
    return render(request, "App/profeForm.html",{'miFormulario':miFormulario})


def alumnoForm(request):
    if request.method == 'POST':
        miFormulario = AlumnoForm(request.POST) 
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            info = Alumno(nombre = info['nombre'], apellido = info['apellido'], email = info['email'], dni = info['dni'])
            info.save()
            return render(request, 'App/index.html')
    else:
        miFormulario = AlumnoForm()
    return render(request, "App/alumnoForm.html",{'miFormulario':miFormulario})


def sedeForm(request):
    if request.method == 'POST':
        miFormulario = SedeForm(request.POST) 
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            info = Sede(nombre = info['nombre'], ubicacion = info['ubicacion'])
            info.save()
            return render(request, 'App/index.html')
    else:
        miFormulario = SedeForm()
    return render(request, "App/sedeForm.html",{'miFormulario':miFormulario})


def claseForm(request):
    if request.method == 'POST':
        miFormulario = ClaseForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            info = Clase(nombre = info['nombre'], descripcion = info['descripcion'], codigo = info['codigo'])
            info.save()
            return render(request, "App/index.html")
    else:
        miFormulario = ClaseForm()
    return render(request, "App/claseForm.html", {'miFormulario':miFormulario})


# def buscarClase(request):

    if request.GET["nombre"]:
        nombre = request.GET['nombre'] 
        clases = Clase.objects.filter(nombre__icontains=nombre)
        return render(request, "App/buscarClase.html", {"clases":clases, "nombre":nombre})

    else: 
        respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)



def buscarClase(request):
    if request.GET["codigo"]:
        codigo = request.GET['codigo']
        clases = Clase.objects.filter(codigo__icontains=codigo)

        return render(request, 'App/buscarClase.html', {'clases':clases, 'codigo':codigo})
    
    else:
        respuesta = 'No enviaste datos'
        return HttpResponse(respuesta)