from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Catalogo
from .serializers import CatalogoSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime
import json
from rest_framework.parsers import JSONParser

@api_view(['GET'])
def get_catalogos(request):
    catalogos = Catalogo.objects.all()
    serializer = CatalogoSerializer(catalogos, many=True)
    return JsonResponse(serializer.data, safe=False) 

# @api_view(['POST'])
# def buscar_usuario(request):
#     if request.method == 'POST':
#         try:
#             cedula = request.data.get('cedula', None)
#             if cedula:
#                 usuario = Usuario.objects.get(cedula=cedula)
#                 serializer = UsuarioSerializer(usuario)
#                 return JsonResponse(serializer.data)
#             else:
#                 return JsonResponse({'error': 'Se requiere identificación'}, status=400)
#         except Usuario.DoesNotExist:
#             return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
#     else:
#         return JsonResponse({'error': 'Se esperaba una solicitud POST'}, status=405)


# @api_view(['POST'])
# def crear_usuario(request):	
#     if request.method == 'POST':
#         serializer = UsuarioSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        


# @api_view(['PUT'])
# def editar_usuario(request, usuario_id):
#     try:
#         usuario = Usuario.objects.get(pk=usuario_id)
#     except Usuario.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = UsuarioSerializer(usuario, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        


# @api_view(['DELETE'])
# def eliminar_usuario(request, usuario_id):
#     try:
#         usuario = Usuario.objects.get(pk=usuario_id)
#     except Usuario.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'DELETE':
#         usuario.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)        