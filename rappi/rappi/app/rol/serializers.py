from rest_framework import serializers

from .models import Rol

##  creo una clase y heredero de todos los modelos del seriaalizers
class RolSerializer(serializers.ModelSerializer):

      class Meta:
        model = Rol
        fields = ('__all__')

##(fields campos para convertir, todos all en formato json)
## las veces que hace el endpoint para darle formato 
## a los datos para que se consuma con cualquier servicio
## convierte los formato en json 