from medico.models.personal_medico import personal_medico
from rest_framework import serializers
from medico.models.account import Account
from medico.serializers.accountSerializer import AccountSerializer

class personal_medicoSerializer(serializers.ModelSerializer):
    acount = AccountSerializer()
    class Meta:
        model = personal_medico
        fields = ['nombre', 'apellido', 'cargo', 'celular', 'correo', 'especialidad', 'paciente_asignado']

         