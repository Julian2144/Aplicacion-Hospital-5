from medico.models.user import User
from rest_framework import serializers
from medico.models.account import Account
from medico.serializers.accountSerializer import AccountSerializer

class personal_medicoSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = User
        fields = ['Nombre', 'Apellido', 'Cargo', 'Celular', 'Correo', 'Especialidad', 'Paciente_Asignado']

         