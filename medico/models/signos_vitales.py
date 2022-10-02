from django.db import models
from .user import User
from .paciente import Paciente
from .familiar import Familiar 
from .personal_medico import personal_medico


class signos_vitales (models.Model):
    ID_signos_vitales = models (primary_key=True,unique=True,max_length=70)
    CC_Paciente = models. ForeignKey (Paciente, related_name='signos_vitales', on_delete=models.CASCADE)
    CC_familiar = models. ForeignKey (Familiar, related_name='signos_vitales', on_delete=models.CASCADE)
    CC_Pmedico = models.ForeignKey (personal_medico, related_name='signos_vitales', on_delete=models.CASCADE)
    Oximetria = models. CharField ('Oxi',max_length=70)
    Frecuencia_respiratoria = models. CharField ('Frecr',max_length=70)
    Frecuencia_cardiaca = models. CharField ('Frecc',max_length=70)
    Temperatura = models. CharField ('Tem',max_length=70)
    Presion_arterial = models. CharField ('Pres',max_length=70)
    Glicemia = models. CharField ('Gli',max_length=70)
  
 