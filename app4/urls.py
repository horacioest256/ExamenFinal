from django.urls import path, include
from . import views

app_name = 'app4'

urlpatterns = [
    path('', views.ingresoUsuario, name='ingresoUsuario'),
    path('informacionUsuario',views.informacionUsuario,name='informacionUsuario'),
    path('cerrarSesion',views.cerrarSesion,name='cerrarSesion'),
    path('ejemploJs',views.ejemploJs,name='ejemploJs')
]