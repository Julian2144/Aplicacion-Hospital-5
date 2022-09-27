from django.db import models
from.user import User
from.paciente import Paciente

class Familiar (models.Model):
    id = models. CharField (primary_key=True,unique=True,max_length=50)
    Nombre = models. CharField ('Nom',max_length=50)
    Apellido = models. CharField ('Apell',max_length=50)
    Celular = models. CharField ('Cel',max_length=50)
    Correo = models. EmailField ('Email',max_length=50)
    Direccion = models. CharField ('Dir',max_length=50)
    Ciudad = models. CharField ('Icu',max_length=50)
    idUser = models.ForeignKey(User, related_name='paciente', on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, related_name='personal_medico', on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, related_name='signos_vitales', on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, related_name='historia_clinica', on_delete=models.CASCADE)