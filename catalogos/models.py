# from rest_framework import serializers
from django.db import models

# Create your models here.

class Catalogo(models.Model):
    
    catalogo = models.CharField(max_length=50)    
    estado = models.CharField(max_length=10)    
    
    class Meta:
        db_table = 'catalogos'
        managed = True
        verbose_name = 'catalogo'
        verbose_name_plural = 'catalogo'
   
