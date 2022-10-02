from medico.models.signos_vitales import signos_vitales
from rest_framework import serializers

class signos_vitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = signos_vitales
        fields = ['oximetria', 'frecuencia_respiratoria', 'frecuencia_cardiaca', 
                'femperatura', 'presion_arterial', 'glicemia', 'paciente_asignado', 
                'familiar_asignado', 'medico_asignado']

