from django.urls import path
from . import views
# from .views import get_usuarios

urlpatterns = [
    path('saludo/', views.saludar, name='saludo'),
    # path('buscar_usuario/<str:cedula>/', views.buscar_usuario, name='buscar_usuario'),
    path('buscar_usuario', views.buscar_usuario, name='buscar_usuario'),
    path('get_usuarios/', views.get_usuarios, name='get_usuarios'),
    path('crear_usuario', views.crear_usuario, name='crear_usuario'),
]