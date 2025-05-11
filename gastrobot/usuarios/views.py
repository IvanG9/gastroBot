from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroForm, LoginForm

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})


def registro(request):
    print("Vista registro llamada")  # <- Comprobación

    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            print("Formulario válido")  # <- Comprobación
            form.save()
            return redirect('login')
        else:
            print(form.errors)  # <- Ver errores
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('login')