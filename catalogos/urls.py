from django.urls import path
from . import views
# from .views import get_usuarios

urlpatterns = [    
    path('get_catalogos', views.get_catalogos, name='get_catalogos'),    
]