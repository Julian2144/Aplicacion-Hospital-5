from pyexpat import model
from django.db import models
from .paciente import Paciente
from .personal_medico import personal_medico
from .familiar  import Familiar


class historia_clinica (models.Model):
    ID_historia_clinica = models (primary_key=True,unique=True,max_length=70)
    CC_Paciente = models. ForeignKey (Paciente, related_name='historia_clinica', on_delete=models.CASCADE)
    CC_Pmedico = models.ForeignKey (personal_medico, related_name='historia_clinica', on_delete=models.CASCADE)
    CC_familiar = models. ForeignKey (Familiar, related_name='historia_clinica', on_delete=models.CASCADE)
    Enfermedades_actuales = models. CharField ('Enfer',max_length=70)
    Cirugias = models. CharField ('Cirug',max_length=70)
    Alergia = models. CharField ('Alerg',max_length=70)
    Peso = models. CharField ('Pes',max_length=70)
    Medicamentos = models. CharField ('Medic',max_length=70)
    Sugerencia_de_Cuidado = models. CharField ('Suger',max_length=70)
    Diagnostico = models. CharField ('Diag',max_length=70)
    
