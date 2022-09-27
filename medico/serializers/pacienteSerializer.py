from medico.models.user import User
from rest_framework import serializers
from medico.models.account import Account
from medico.serializers.accountSerializer import AccountSerializer

class pacienteSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = User
        fields = ['Nombre', 'Apellido ', 'Celular', 'Correo', 'Direccion', 'Ciudad','Fecha_Nacimiento', 'Genero' ]

         
    
     
     
    
    
    
    