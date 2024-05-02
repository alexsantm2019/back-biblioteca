# from rest_framework import serializers
from django.db import models

# Create your models here.

class Usuario(models.Model):
    # id = models.SmallIntegerField()
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=50)
    institucion = models.CharField(max_length=100)
    # es_superusuario = models.IntegerField(default=0)  # Suponiendo que 0 representa un usuario no superusuario y 1 representa un superusuario
    es_superusuario = models.IntegerField(default=0, null=True)
    genero = models.CharField(max_length=10)
    nacionalidad = models.CharField(max_length=50)
    etnia = models.CharField(max_length=50)
    discapacidad = models.CharField(max_length=5)
    recibir_informacion = models.CharField(max_length=5)

    class Meta:
        db_table = 'usuarios'
        managed = True
        verbose_name = 'usuario'
        verbose_name_plural = 'usuario'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"       