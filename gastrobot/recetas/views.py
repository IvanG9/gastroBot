from django.shortcuts import render
from asistente.services import ask_groq

def receta_view(request):
    receta = {...}  # El JSON generado por tu modelo
    return render(request, 'recetas/detalle.html', {'receta': receta})

def generar_receta_view(request):
    receta = None
    error = None
    loading = False
    mensaje = ""

    if request.method == "POST":
        print(request.POST)
        mensaje = request.POST.get("message", "")
        loading = True
        if mensaje:
            resultado = ask_groq(mensaje)
            if "error" in resultado:
                error = resultado["error"]
            else:
                receta = resultado
            loading = False
    elif request.method == "GET":
        mensaje = request.GET.get("q", "")
        loading = True
        if mensaje:
            resultado = ask_groq(mensaje)
            if "error" in resultado:
                error = resultado["error"]
            else:
                receta = resultado
            loading = False
            print("GET recibido:")
            print(request.GET)

    return render(request, "recetas/detalle.html", {
        "receta": receta,
        "error": error,
        "loading": loading,
        "mensaje": mensaje
    })
