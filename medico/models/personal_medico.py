from django.db import models
from.user import User 
from.paciente import Paciente
from.familiar import Familiar
from.historia_clinica import historia_clinica
from.signos_vitales import signos_vitales

class personal_medico (models.Model):
    CC_Pmedico = models. CharField (primary_key=True,unique=True,max_length=50),
    CC_Paciente = models. ForeignKey (Paciente, related_name='personal_medico', on_delete=models.CASCADE)
    C_familiar = models. ForeignKey (Familiar, related_name='personal_medico', on_delete=models.CASCADE)
    ID_historia_clinica  = models.ForeignKey(historia_clinica, related_name='personal_medico', on_delete=models.CASCADE)
    ID_signos_vitales = models.ForeignKey(signos_vitales, related_name='personal_medico', on_delete=models.CASCADE)
    Nombre = models. CharField ('Nomb',max_length=50)
    Apellido = models. CharField ('Apell',max_length=50)
    Cargo = models. CharField ('Carg',max_length=50)
    Celular = models. CharField ('Cel',max_length=50)
    Correo = models. EmailField ('Email',max_length=50)
    Especialidad = models. CharField ('Espe',max_length=50)
    Paciente_Asignado = models. CharField ('Paciente',max_length=50)