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
from django.db.models.functions import Cast
from django.db.models import DateField
from django.db.models import Count, Func
from django.db.models import CharField
from django.db.models.functions import ExtractYear, ExtractMonth
from django.db import connection

# class ExtractMonthName(Func):
#     function = 'EXTRACT'
#     template = '%(function)s(MONTH FROM %(expressions)s)'
#     output_field = CharField()

# class ExtractMonthName(Func):
#     function = 'EXTRACT'
#     template = '%(function)s(MONTH FROM %(expressions)s)'    

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
       
@api_view(['GET'])
def reporte_mes(request):
    # Consulta SQL para obtener el reporte de visitas por mes y catálogo
    query = """
    SELECT
        EXTRACT(YEAR FROM TO_DATE(visitas.fecha, 'YYYY-MM-DD')) AS year,
        EXTRACT(MONTH FROM TO_DATE(visitas.fecha, 'YYYY-MM-DD')) AS month,
        catalogos.id AS catalogoId,
        catalogos.catalogo AS nombre_catalogo,
        COUNT(visitas.id) AS num_visitas
    FROM
        catalogos
    LEFT OUTER JOIN
        visitas ON catalogos.id = visitas."catalogoId"
    GROUP BY
        year, month, catalogos.id
    ORDER BY
        year, month, catalogos.id
    """

    # Ejecutar la consulta y obtener los resultados
    with connection.cursor() as cursor:
        cursor.execute(query)
        reporte = cursor.fetchall()

    # Mapear los números de mes a los nombres de mes correspondientes
    meses = {
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre'
    }

    # Convertir los resultados en un formato JSON adecuado
    reporte_con_meses = []
    for visita in reporte:
        year = visita[0]
        month = visita[1]
        catalogoId = visita[2]
        nombre_catalogo = visita[3]
        num_visitas = visita[4]
        if month is not None:
            reporte_con_meses.append({
                'year': int(year),
                'catalogoId': catalogoId,
                'catalogo': nombre_catalogo,
                'visitas_por_mes': {meses.get(month, 'Desconocido'): num_visitas}
            })

    # Estructurar los datos para enviar como respuesta JSON
    datos_tabla = []
    for catalogo in set([visita['catalogoId'] for visita in reporte_con_meses]):
        fila_catalogo = {'catalogoId': catalogo, 'catalogo': '', 'visitas_por_mes': {}}
        for visita in reporte_con_meses:
            if visita['catalogoId'] == catalogo:
                fila_catalogo['catalogo'] = visita['catalogo']
                fila_catalogo['year'] = visita['year']
                fila_catalogo['visitas_por_mes'].update(visita['visitas_por_mes'])
        datos_tabla.append(fila_catalogo)         

    return JsonResponse(datos_tabla, safe=False)






