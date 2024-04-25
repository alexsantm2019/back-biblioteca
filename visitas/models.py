# from rest_framework import serializers
from django.db import models

# Create your models here.

class Visita(models.Model):
    userId = models.SmallIntegerField()
    catalogoId = models.SmallIntegerField()
    taller = models.CharField(max_length=100) 
    actividad = models.CharField(max_length=100)    
    fecha = models.DateTimeField()    

    class Meta:
        db_table = 'visitas'
        managed = True
        verbose_name = 'visitas'
        verbose_name_plural = 'viista'

    # def __str__(self):
    #     return f"{self.nombre} {self.apellido}"       
