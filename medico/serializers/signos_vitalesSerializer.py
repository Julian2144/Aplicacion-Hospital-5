from medico.models.user import User
from rest_framework import serializers
from medico.models.account import Account
from medico.serializers.accountSerializer import AccountSerializer

class signos_vitalesSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = User
        fields = ['Oximetria', 'Frecuencia_respiratoria', 'Frecuencia_cardiaca', 
                'Temperatura', 'Presion_arterial', 'Glicemia', 'Paciente_Asignado', 
                'Familiar_Asignado', 'Medico_Asignado']

