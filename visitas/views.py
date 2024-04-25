from django.http import HttpResponse
from django.http import JsonResponse
from .models import Visita
from .serializers import VisitaSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime
import json
from rest_framework.parsers import JSONParser

@api_view(['GET'])
def get_visitas(request):
    visitas = Visita.objects.all()
    serializer = VisitaSerializer(visitas, many=True)
    return JsonResponse(serializer.data, safe=False)    


@api_view(['POST'])
def crear_visita(request):	
    if request.method == 'POST':
        print(request.data)
        serializer = VisitaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
       