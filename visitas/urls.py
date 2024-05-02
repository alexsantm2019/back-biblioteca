from django.urls import path
from . import views

urlpatterns = [    
    path('get_visitas', views.get_visitas, name='get_visitas'),
    path('crear_visita', views.crear_visita, name='crear_visita'),
    path('reporte_mes', views.reporte_mes, name='reporte_mes'),
]