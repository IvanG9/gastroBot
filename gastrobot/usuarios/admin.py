from django.contrib import admin
from .models import Perfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'nombre', 'apellidos', 'pais', 'fecha_nacimiento')
    search_fields = ('user__username', 'nombre', 'apellidos', 'pais')
    list_filter = ('pais', 'fecha_nacimiento')