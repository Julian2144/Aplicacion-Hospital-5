from django.db import models
from.user import User 

class personal_medico (models.Model):
    id_Pmedico = models. CharField (primary_key=True,unique=True,max_length=50),
    Nombre = models. CharField ('Nomb',max_length=50)
    Apellido = models. CharField ('Apell',max_length=50)
    Cargo = models. CharField ('Carg',max_length=50)
    Celular = models. CharField ('Cel',max_length=50)
    Correo = models. EmailField ('Email',max_length=50)
    Especialidad = models. CharField ('Espe',max_length=50)
    Paciente_Asignado = models. CharField ('Paciente',max_length=50)
    idUser = models.ForeignKey(User, related_name='historia_clinica', on_delete=models.CASCADE)
    id = models.ForeignKey(User, related_name='Paciente', on_delete=models.CASCADE)