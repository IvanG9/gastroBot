from django.urls import path
from . import views

urlpatterns = [
   path('login/', views.iniciar_sesion, name='login'),
   path('registro/', views.registro, name='registro'),
   path('logout/', views.cerrar_sesion, name='logout'),
   path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
   path('perfil/', views.ver_perfil, name='perfil'),
]
