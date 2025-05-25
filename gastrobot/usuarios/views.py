from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import PerfilForm, RegistroForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import Perfil
from django.core.files.storage import default_storage
import os

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

def registro(request):
    print("Vista registro llamada")

    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            print("Formulario válido")
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

@login_required
def editar_perfil(request):
    perfil = request.user.perfil
    form = PerfilForm(request.POST or None, request.FILES or None, instance=perfil)

    if request.method == 'POST':
        if form.is_valid():
            # Eliminar imagen anterior si se sube una nueva
            nueva_imagen = form.cleaned_data.get('imagen')
            if nueva_imagen and perfil.imagen and perfil.imagen.name != nueva_imagen.name:
                if default_storage.exists(perfil.imagen.name):
                    default_storage.delete(perfil.imagen.name)

            # Eliminar imagen si el usuario marcó la opción de borrarla (si existe esta lógica en el template)
            if 'eliminar_imagen' in request.POST:
                if perfil.imagen and default_storage.exists(perfil.imagen.name):
                    default_storage.delete(perfil.imagen.name)
                perfil.imagen = None

            form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('perfil')

    return render(request, 'usuarios/editar_perfil.html', {'form': form, 'perfil': perfil})

@login_required
def ver_perfil(request):
    perfil = request.user.perfil
    return render(request, 'usuarios/perfil.html', {'perfil': perfil})
