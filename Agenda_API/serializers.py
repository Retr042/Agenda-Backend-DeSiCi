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
    direccion = DireccionSerializer()
    telefonos = TelefonoSerializer(many=True)
    class Meta:
        model = Contacto
        fields = ['nombre', 'apellidos', 'fotografia', 'fecha_nac', 'direccion', 'telefonos']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'Contacto' : data
        }

    def create(self, validated_data):

        direccion_data =  validated_data.pop('direccion') 
        telefonos_data = validated_data.pop('telefonos')  

        contacto = Contacto.objects.create(**validated_data)

        Direccion.objects.create(contacto=contacto,**direccion_data)

        for tel_data in telefonos_data:
            Telefono.objects.create(contacto=contacto, **tel_data)
        return contacto
    
    def update(self, instance, validated_data):
        direccion_data = validated_data.pop('direccion', None)
        telefonos_data = validated_data.pop('telefonos', None)

        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellidos = validated_data.get('apellidos', instance.apellidos)
        instance.fotografia = validated_data.get('fotografia', instance.fotografia)
        instance.fecha_nac = validated_data.get('fecha_nac', instance.fecha_nac)
        instance.save()

        if direccion_data:
            direccion = instance.direccion
            for attr, value in direccion_data.items():
                setattr(direccion, attr, value)
            direccion.save()
        if telefonos_data is not None:
            instance.telefonos.all().delete()
            for tel in telefonos_data:
                Telefono.objects.create(contacto=instance, **tel)
            return instance            