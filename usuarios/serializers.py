from rest_framework import serializers
from . import models

class UsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Usuario
		fields = ('id','cedula', 'nombre', 'apellido', 'fecha_nacimiento', 'telefono', 'correo',  'institucion', 'es_superusuario', 'genero', 'nacionalidad', 'etnia', 'discapacidad', 'recibir_informacion', 'es_superusuario')