from django.urls import path
from . import views

urlpatterns = [
    path('gastroBot/', views.asistente_view, name='asistente'),
]
