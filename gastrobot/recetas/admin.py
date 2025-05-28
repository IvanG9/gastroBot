from django.contrib import admin
from .models import Receta, Favorito

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'tiempo_preparacion', 'publicada', 'fecha_creacion')
    list_filter = ('publicada', 'fecha_creacion')
    search_fields = ('titulo', 'descripcion', 'ingredientes', 'pasos')
    date_hierarchy = 'fecha_creacion'
    ordering = ('-fecha_creacion',)

@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ('user', 'receta', 'creado')
    search_fields = ('user__username', 'receta__titulo')
    ordering = ('-creado',)