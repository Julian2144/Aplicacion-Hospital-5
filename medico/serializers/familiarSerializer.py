from medico.models.familiar import Familiar
from rest_framework import serializers


class familiarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = ['nombre', 'apellido', 'celular', 'correo', 'direccion', 
        'ciudad', 'paciente_asignado','parentesco']