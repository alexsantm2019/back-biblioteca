from rest_framework import serializers
from . import models

class UsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Usuario
		fields = ('cedula', 'nombre', 'apellido', 'fecha_nacimiento', 'telefono', 'correo', 'es_superusuario', 'genero', 'nacionalidad', 'etnia', 'discapacidad', 'recibir_informacion')