from django.urls import path
from . import views

app_name = "recetas"

urlpatterns = [
  path("detalle/", views.generar_receta_view, name="generar_receta"),
  path('guardar/', views.guardar_receta, name='guardar_receta'),
  path('mis-recetas/', views.mis_recetas_view, name='mis_recetas'),
  path('detalle-guardada/<int:receta_id>/', views.detalle_receta_view, name='detalle_receta_guardada'),
  path('editar/<int:receta_id>/', views.editar_receta_view, name='editar_receta'),
  path('eliminar/<int:receta_id>/', views.eliminar_receta_view, name='eliminar_receta'),
  path('receta/<int:receta_id>/publicar/', views.publicar_receta, name='publicar_receta'),
  path('explorar/', views.recetas_publicas, name='explorar_recetas'),
  path('receta/<int:receta_id>/despublicar/', views.despublicar_receta, name='despublicar_receta'),
  path('favorito/agregar/<int:receta_id>/', views.agregar_favorito, name='agregar_favorito'),
  path('favorito/eliminar/<int:receta_id>/', views.eliminar_favorito, name='eliminar_favorito'),
  path('favoritos/', views.ver_favoritos, name='favoritos'),
  path("test-openai/", views.test_openai, name="test_openai"),
  path('crear/', views.crear_receta, name='nueva_receta'),

]
