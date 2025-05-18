from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    ingredientes = models.TextField()
    pasos = models.TextField()
    tiempo_preparacion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='recetas/', blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recetas')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    publicada = models.BooleanField(default=False)
    fecha_publicacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.titulo

class Favorito(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoritos')
    receta = models.ForeignKey('Receta', on_delete=models.CASCADE, related_name='favoritos')
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'receta')  # evita duplicados

    def __str__(self):
        return f"{self.user.username} ❤️ {self.receta.titulo}"