from rest_framework import serializers
from . import models

class CatalogoSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Catalogo
		fields = ('id', 'catalogo', 'estado')