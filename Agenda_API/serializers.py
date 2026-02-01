from rest_framework import serializers
from .models import Contacto, Direccion, Telefono

class TelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefono  
        fields = ['alias', 'tipo', 'numero']

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion 
        fields = ['calle', 'no_ext', 'no_int', 'colonia', 'municipio', 'referencias', 'estado']     

class ContactoSerializer(serializers.ModelSerializer):
    #relaciones 
    direccion = DireccionSerializer(read_only=True)
    telefonos = TelefonoSerializer(read_only=True, many=True)
    class Meta:
        model = Contacto
        fields = ['nombre', 'apellidos', 'fotografia', 'fecha_nac', 'direccion', 'telefonos']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'Contacto' : data
        }    