from medico.models.historia_clinica import historia_clinica
from rest_framework import serializers


class historia_clinicaSerializer(serializers.ModelSerializer):
       class Meta:
        model = historia_clinica
        fields = ['enfermedades_actuales', 'cirugias', 'Alergia', 
                'peso', 'medicamentos', 'sugerencia_de_Cuidado', 'Diagnostico']
 