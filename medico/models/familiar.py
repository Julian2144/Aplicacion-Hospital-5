
from django.db import models
from.usuarios import  
class Familiares (models.Model):
    id = models. CharField (primary_key=True,unique=True,max_length=50)
    Nombre = models. CharField ('Nom',max_length=50)
    Apellido = models. CharField ('Apell',max_length=50)
    Celular = models. CharField ('Cel',max_length=50)
    Genero = models. CharField ('Gen',max_length=50)
    Direccion = models. CharField ('Dir',max_length=50)
    Ciudad = models. CharField ('Icu',max_length=50)
    Fecha_Nacimiento = models. CharField ('Nacimiento',max_length=50)
    Paciente_Asignado = models. CharField ('Paciente',max_length=50)
    Parentesco = models. CharField ('Par',max_length=50)
    Correo = models. CharField ('Email',max_length=50)
