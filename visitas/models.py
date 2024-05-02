# from rest_framework import serializers
from django.db import models
from usuarios.models import Usuario
from catalogos.models import Catalogo

# Create your models here.

class Visita(models.Model):
    userId = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='userId')
    catalogoId = models.ForeignKey(Catalogo, on_delete=models.CASCADE, db_column='catalogoId')
    taller = models.CharField(max_length=100) 
    actividad = models.CharField(max_length=100)    
    fecha = models.DateTimeField()    

    class Meta:
        db_table = 'visitas'
        managed = True
        verbose_name = 'visitas'
        verbose_name_plural = 'viista'