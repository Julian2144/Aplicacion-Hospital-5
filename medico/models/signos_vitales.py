from django.db import models
from.user import User
from.familiar import Familiar 
from.paciente import Paciente

class signos_vitales (models.Model):
    id = models. CharField (primary_key=True,unique=True,max_length=70)
    Oximetria = models. CharField ('Oxi',max_length=70)
    Frecuencia_respiratoria = models. CharField ('Frecr',max_length=70)
    Frecuencia_cardiaca = models. CharField ('Frecc',max_length=70)
    Temperatura = models. CharField ('Tem',max_length=70)
    Presion_arterial = models. CharField ('Pres',max_length=70)
    Glicemia = models. CharField ('Gli',max_length=70)
    Paciente_Asignado = models. CharField ('Paciente',max_length=70)
    Familiar_Asignado = models. CharField ('Familiar',max_length=70)
    Medico_Asignado = models. CharField ('personal_medico',max_length=70)
    iduser = models.ForeignKey(User, related_name='Paciente', on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, related_name='familiar', on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, related_name='personal_medico', on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, related_name='historia_clinica', on_delete=models.CASCADE)