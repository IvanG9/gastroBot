# Generated by Django 5.2 on 2025-05-18 19:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0002_receta_fecha_publicacion_receta_publicada'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favoritos', to='recetas.receta')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favoritos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'receta')},
            },
        ),
    ]
