from django import forms

class ProfeForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    matricula = forms.CharField(max_length=30)

class AlumnoForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    dni = forms.IntegerField()
    
class SedeForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    ubicacion = forms.CharField(max_length=30)

class ClaseForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=30)
    codigo = forms.IntegerField()

