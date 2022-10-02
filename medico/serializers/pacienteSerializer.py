from medico.models.paciente import Paciente
from rest_framework import serializers

class pacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido ', 'celular', 'correo', 'direccion', 
                    'ciudad','fecha_nacimiento', 'genero' ]

         
    
     
     
    
    
    
    