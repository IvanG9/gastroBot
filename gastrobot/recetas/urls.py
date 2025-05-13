from django.urls import path
from . import views

app_name = "recetas"

urlpatterns = [
  path("detalle/", views.generar_receta_view, name="generar_receta"),
]
