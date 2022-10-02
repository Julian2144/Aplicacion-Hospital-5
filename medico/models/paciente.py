from django.db import models
from.user import User
from.familiar import Familiar 
from medico.models import personal_medico
from.historia_clinica import historia_clinica
from.signos_vitales import signos_vitales


class Paciente (models.Model):
    CC_Paciente = models. CharField (primary_key=True,unique=True,max_length=50)
    CC_familiar = models.ForeignKey(Familiar, related_name='Paciente', on_delete=models.CASCADE)
    CC_Pmedico = models.ForeignKey(personal_medico, related_name='paciente', on_delete=models.CASCADE)
    ID_historia_clinica  = models.ForeignKey(historia_clinica, related_name='paciente', on_delete=models.CASCADE)
    ID_signos_vitales = models.ForeignKey(signos_vitales, related_name='paciente', on_delete=models.CASCADE)
    Nombre = models. CharField ('Nom',max_length=50)
    Apellido = models. CharField ('Apell',max_length=50)
    Celular = models. CharField ('Cel',max_length=50)
    Correo = models. EmailField ('Email',max_length=50)
    Direccion = models. CharField ('Dir',max_length=50)
    Ciudad = models. CharField ('Icu',max_length=50)
    Fecha_Nacimiento = models. CharField ('Nacimiento',max_length=50)
    Genero = models. CharField ('Gen',max_length=50)
  