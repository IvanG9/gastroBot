from django.shortcuts import render

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