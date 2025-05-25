# Python
import re
import requests

# Django
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.utils import timezone
from django.http import Http404
from django.contrib import messages

# App interna
from .models import Receta, Favorito
from .forms import RecetaForm
from asistente.services import ask_groq, generar_imagen_receta

# Test OpenAI
import openai
from django.http import JsonResponse
import os
from django.db.models import Q
from django.template.loader import render_to_string

def receta_view(request):
    receta = {...}  # El JSON generado por Groq
    return render(request, 'recetas/detalle.html', {'receta': receta})

def generar_receta_view(request):
    receta = None
    error = None
    mensaje = ""

    if request.method in ["POST", "GET"]:
        mensaje = request.POST.get("message", "") if request.method == "POST" else request.GET.get("q", "")

        if mensaje:
            resultado = ask_groq(mensaje)

            if "error" in resultado:
                error = resultado["error"]
            else:
                titulo = resultado.get("titulo")
                if titulo:
                    imagen_url = generar_imagen_receta(titulo)
                    resultado["imagen_url"] = imagen_url

                receta = resultado

    return render(request, "recetas/detalle.html", {
        "receta": receta,
        "error": error,
        "mensaje": mensaje
    })

@login_required
def guardar_receta(request):
    if request.method == 'POST':
        # Extraer campos
        titulo = request.POST.get('titulo', '')
        descripcion = request.POST.get('descripcion', '')
        tiempo_preparacion = request.POST.get('tiempo_preparacion', '')

        # Convertir listas separadas por `;` para guardar en base de datos
        ingredientes = request.POST.get('ingredientes', '').split(';')
        pasos = request.POST.get('pasos', '').split(';')

        receta = Receta.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            tiempo_preparacion=tiempo_preparacion,
            ingredientes=";".join([i.strip() for i in ingredientes]),
            pasos=";".join([p.strip() for p in pasos]),
            autor=request.user
        )

        # Guardar imagen si viene desde IA
        imagen_url = request.POST.get('imagen_url')
        if imagen_url:
            descargar_imagen_y_guardar(imagen_url, receta)

        return redirect('recetas:mis_recetas')


@login_required
def mis_recetas_view(request):
    recetas = Receta.objects.filter(autor=request.user).order_by('-fecha_creacion')
    return render(request, 'recetas/mis_recetas_view.html', {'recetas': recetas})

@login_required
def detalle_receta_view(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)

    if not receta.publicada and receta.autor != request.user:
        raise Http404("No tienes permiso para ver esta receta.")

    ingredientes = [i.strip() for i in receta.ingredientes.split(';')]
    pasos = [re.sub(r'^\s*\d+[\.\)]\s*', '', p.strip()) for p in receta.pasos.split(';')]

    es_favorita = receta.favoritos.filter(user=request.user).exists()

    return render(request, 'recetas/detalle_guardada.html', {
        'receta': receta,
        'ingredientes': ingredientes,
        'pasos': pasos,
        'es_favorita': es_favorita
    })

@login_required
def editar_receta_view(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id, autor=request.user)

    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES, instance=receta)

        ingredientes = request.POST.get('ingredientes', '')
        pasos = request.POST.get('pasos', '')

        if form.is_valid():
            receta = form.save(commit=False)
            receta.ingredientes = ingredientes
            receta.pasos = pasos
            receta.save()
            return redirect('recetas:detalle_receta_guardada', receta_id=receta.id)
    else:
        form = RecetaForm(instance=receta)

    ingredientes_lista = [i.strip() for i in receta.ingredientes.split(';')] if receta.ingredientes else []
    pasos_lista = [p.strip() for p in receta.pasos.split(';')] if receta.pasos else []

    return render(request, 'recetas/editar_receta.html', {
        'form': form,
        'receta': receta,
        'ingredientes_lista': ingredientes_lista,
        'pasos_lista': pasos_lista,
        'ingredientes': ingredientes_lista,
        'pasos': pasos_lista,
    })


@login_required
def eliminar_receta_view(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id, autor=request.user)

    if request.method == 'POST':
        receta.delete()
        messages.success(request, "Receta eliminada correctamente.")
        return redirect('recetas:mis_recetas')

    return render(request, 'recetas/eliminar_receta.html', {'receta': receta})

def descargar_imagen_y_guardar(url, receta_obj):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            nombre_archivo = f"{receta_obj.titulo.replace(' ', '_')}.jpg"
            receta_obj.imagen.save(nombre_archivo, ContentFile(response.content), save=True)
    except Exception as e:
        print("\u274c Error guardando imagen local:", e)

@login_required
def publicar_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id, autor=request.user)
    receta.publicada = True
    receta.fecha_publicacion = timezone.now()
    receta.save()
    return redirect('recetas:detalle_receta_guardada', receta.id)

@login_required
def recetas_publicas(request):
    recetas = Receta.objects.filter(publicada=True).order_by('-fecha_publicacion')
    return render(request, 'recetas/explorar_recetas.html', {
        'recetas': recetas
    })

@login_required
def despublicar_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id, autor=request.user)
    receta.publicada = False
    receta.fecha_publicacion = None
    receta.save()
    return redirect('recetas:detalle_receta_guardada', receta.id)

@login_required
def agregar_favorito(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    Favorito.objects.get_or_create(user=request.user, receta=receta)
    messages.success(request, "Receta añadida a favoritos.")
    return redirect('recetas:detalle_receta_guardada', receta_id=receta.id)

@login_required
def eliminar_favorito(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    Favorito.objects.filter(user=request.user, receta=receta).delete()
    messages.success(request, "Receta eliminada de favoritos.")

    next_url = request.GET.get('next')
    if next_url:
        return redirect(next_url)
    return redirect('recetas:detalle_receta_guardada', receta_id=receta.id)

@login_required
def ver_favoritos(request):
    recetas = Receta.objects.filter(favoritos__user=request.user).distinct()
    return render(request, 'recetas/ver_favoritos.html', {'recetas': recetas})

def test_openai(request):
    try:
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.models.list()
        return JsonResponse({"ok": True, "models": [m.id for m in response.data]})
    except Exception as e:
        return JsonResponse({"ok": False, "error": str(e)})
    
@login_required
def crear_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES)
        ingredientes = request.POST.get('ingredientes', '')
        pasos = request.POST.get('pasos', '')

        if form.is_valid():
            receta = form.save(commit=False)
            receta.autor = request.user
            receta.ingredientes = ingredientes
            receta.pasos = pasos
            receta.save()
            return redirect('recetas:detalle_receta_guardada', receta_id=receta.id)
    else:
        form = RecetaForm()

    return render(request, 'recetas/crear_receta.html', {
        'form': form,
    })

@login_required
def explorar_recetas(request):
    recetas = Receta.objects.filter(publicada=True).order_by('-fecha_publicacion')
    return render(request, 'recetas/explorar.html', {
        'recetas': recetas
    })

@login_required
def buscar_recetas_ajax(request):
    q = request.GET.get('q', '')
    recetas = Receta.objects.filter(publicada=True)

    if q:
        recetas = recetas.filter(
            Q(titulo__icontains=q) |
            Q(descripcion__icontains=q) |
            Q(ingredientes__icontains=q)
        )

    html = render_to_string('recetas/_recetas_listado.html', {'recetas': recetas})
    return JsonResponse({'html': html})