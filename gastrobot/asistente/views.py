from django.shortcuts import render
from .services import ask_groq  # Suponiendo que tienes esto en servicios

def asistente_view(request):
    response = None
    if request.method == 'POST':
        mensaje = request.POST.get('message', '')
        response = ask_groq(mensaje)
    return render(request, 'asistente/asistente.html', {'response': response})