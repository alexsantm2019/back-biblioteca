from rest_framework import serializers
from . import models

class VisitaSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Visita
		fields = ('userId', 'catalogoId', 'taller', 'actividad', 'fecha')