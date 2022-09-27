
from django.db import models
from.user import User 
class historia_clinica (models.Model):
    id = models. CharField (primary_key=True,unique=True,max_length=70)
    Enfermedades_actuales = models. CharField ('Enfer',max_length=70)
    Cirugias = models. CharField ('Cirug',max_length=70)
    Alergia = models. CharField ('Alerg',max_length=70)
    Peso = models. CharField ('Pes',max_length=70)
    Medicamentos = models. CharField ('Medic',max_length=70)
    Sugerencia_de_Cuidado = models. CharField ('Suger',max_length=70)
    Diagnostico = models. CharField ('Diag',max_length=70)
    Paciente_Asignado = models. CharField ('Paciente',max_length=70)
    Familiar_Asignado = models. CharField ('Familiar',max_length=70)
    Medico_Asignado = models. CharField ('Personal_medico',max_length=70)
    idUser = models.ForeignKey(User, related_name='paciente', on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, related_name='personal_medico', on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, related_name='signos_vitales', on_delete=models.CASCADE)
    
