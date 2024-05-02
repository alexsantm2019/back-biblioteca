from rest_framework import serializers
from . import models
from usuarios.serializers import UsuarioSerializer
from catalogos.serializers import CatalogoSerializer
from usuarios.models import Usuario
from catalogos.models import Catalogo

class VisitaSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(source='userId.nombre', read_only=True)
    apellido = serializers.CharField(source='userId.apellido', read_only=True)
    catalogo = serializers.CharField(source='catalogoId.catalogo', read_only=True)

    class Meta:
        model = models.Visita
        fields = ['id', 'userId','nombre', 'apellido','catalogo', 'catalogoId','taller', 'actividad', 'fecha']