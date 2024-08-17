from django.shortcuts import render
from .models import Rol 

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .serializers import RolSerializer


class RolView(ListAPIView):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()


class CreateRolView(CreateAPIView):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()


class ListIdRolView(RetrieveAPIView):
    serializer_class = RolSerializer
    queryset = Rol.objects.all() 

class UpdateRolView(UpdateAPIView):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()

class DeleteRolView(DestroyAPIView):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()   
     


## consume los datos del serializer, se importa el rol,
## se crea una vista rest_framework.generics
## luego se importa la clase serializers 
## luego se crea la vista RolView
