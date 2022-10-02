from django.db import models
from.user import User
from.paciente import Paciente
from.historia_clinica import historia_clinica
from.signos_vitales import signos_vitales

class Familiar (models.Model):
    CC_familiar = models (primary_key=True,unique=True,max_length=70)
    CC_Paciente = models.ForeignKey(Paciente, related_name='familiar', on_delete=models.CASCADE)
    ID_historia_clinica  = models.ForeignKey(historia_clinica, related_name='familiar', on_delete=models.CASCADE)
    ID_signos_vitales = models.ForeignKey(signos_vitales, related_name='signos_vitales', on_delete=models.CASCADE)
    Nombre = models. CharField ('Nom',max_length=50)
    Apellido = models. CharField ('Apell',max_length=50)
    Celular = models. CharField ('Cel',max_length=50)
    Correo = models. EmailField ('Email',max_length=50)
    Direccion = models. CharField ('Dir',max_length=50)
    Ciudad = models. CharField ('Icu',max_length=50)
    Paciente_Asignado = models. CharField ('Paciente',max_length=50)
    Parentesco = models. CharField ('Par',max_length=50)
   