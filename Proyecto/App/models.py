from django.db import models

# Create your models here.
class Profe(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=30)

class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    dni = models.IntegerField()
    
class Sede(models.Model):
    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=30)

class Clase(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    codigo = models.IntegerField()
