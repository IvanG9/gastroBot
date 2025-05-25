from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from recetas.models import Receta, Favorito
from usuarios.models import Perfil 
from django.contrib.auth import get_user_model

# Create your views here.
def home_view(request):
    recetas = [
        {"nombre": "Arroz con Leche", "imagen_url": "media/defaults/recipe1.jpg"},
        {"nombre": "Arroz con Pollo", "imagen_url": "media/defaults/recipe2.jpg"},
        {"nombre": "Paella Valenciana", "imagen_url": "media/defaults/recipe3.jpg"},
        {"nombre": "Pizza Margarita", "imagen_url": "media/defaults/recipe4.jpg"},
    ]

    planes = [
        {"nombre": "Gratis", "beneficios": [
            "Almacenar 20 recetas", "3 libros de cocina", "Importador estándar",
            "3 generaciones de recetas AI al mes", "Lista de la compra básica", "Planificador de comidas"
        ]},
        {"nombre": "Plus", "beneficios": [
            "Todas las funciones gratuitas", "Recetas ilimitadas", "Listas ilimitadas",
            "50 escaneos/mes", "15 recetas AI/mes", "Exportar PDF"
        ]},
        {"nombre": "Pro", "beneficios": [
            "Todo lo anterior", "IA ilimitada", "Escáner Pro", "Importador Pro",
            "Preferencias AI", "Foto a receta", "Análisis nutricional"
        ]}
    ]

    return render(request, "core/home.html", {
        "recetas": recetas,
        "planes": planes
    })


def dashboard_view(request):
    user = request.user
    recetas_creadas = Receta.objects.filter(autor=user).count()
    recetas_favoritas = Favorito.objects.filter(user=user).count()
    ultima_receta = Receta.objects.filter(autor=user).order_by('-fecha_creacion').first()

    perfil = getattr(user, 'perfil', None)

    perfil_completo = (
        perfil and
        perfil.nombre and
        perfil.apellidos and
        perfil.pais and
        perfil.imagen and
        not perfil.imagen.name.endswith('defaults/default_user.png')
    )

    return render(request, 'core/dashboard.html', {
        'recetas_creadas': recetas_creadas,
        'recetas_favoritas': recetas_favoritas,
        'ultima_receta': ultima_receta,
        'perfil_completo': perfil_completo,
    })