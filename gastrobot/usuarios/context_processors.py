from .models import Perfil

def perfil_usuario(request):
    if request.user.is_authenticated:
        try:
            return {'perfil': request.user.perfil}
        except Perfil.DoesNotExist:
            return {'perfil': None}
    return {'perfil': None}
