from medico.models.user import User
from rest_framework import serializers
from medico.models.account import Account
from medico.serializers.accountSerializer import AccountSerializer

class familiarSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = User
        fields = ['nombre', 'apellido', 'celular', 'correo', 'direccion', 'ciudad']