from medico.models.user import User
from rest_framework import serializers
from medico.models.account import Account
from medico.serializers.accountSerializer import AccountSerializer

class historia_clinicaSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = User
        fields = ['Enfermedades_actuales', 'Cirugias', 'Alergia', 
                'Peso', 'Medicamentos', 'Sugerencia_de_Cuidado', 'Diagnostico', 
                'Paciente_Asignado', 'Familiar_Asignado', 'Medico_Asignado']
 