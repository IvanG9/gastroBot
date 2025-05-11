from django.shortcuts import render

# Create your views here.
def bienvenida(request):
    """
    Render the welcome page.
    """
    return render(request, 'core/bienvenida.html')
