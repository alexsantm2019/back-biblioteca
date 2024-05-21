from rest_framework import serializers
from . import models

class UsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Usuario
		fields = ('id','cedula', 'nombre', 'apellido', 'fecha_nacimiento', 'telefono', 'correo',  'institucion', 'es_superusuario', 'genero', 'nacionalidad', 'etnia', 'discapacidad', 'recibir_informacion', 'es_superusuario')


	def validate_cedula(self, value):
		if models.Usuario.objects.filter(cedula=value).exists():
			raise serializers.ValidationError("La cédula ya existe.")
		return value