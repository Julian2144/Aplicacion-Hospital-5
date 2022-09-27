from django.db import models
from.user import User
from.familiar import Familiar 

class Paciente (models.Model):
    id_Paciente = models. CharField (primary_key=True,unique=True,max_length=50)
    Nombre = models. CharField ('Nom',max_length=50)
    Apellido = models. CharField ('Apell',max_length=50)
    Celular = models. CharField ('Cel',max_length=50)
    Correo = models. EmailField ('Email',max_length=50)
    Direccion = models. CharField ('Dir',max_length=50)
    Ciudad = models. CharField ('Icu',max_length=50)
    Fecha_Nacimiento = models. CharField ('Nacimiento',max_length=50)
    Genero = models. CharField ('Gen',max_length=50)
    idUser = models.ForeignKey(User, related_name='familiar', on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, related_name='historia_clinica', on_delete=models.CASCADE)