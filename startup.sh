#!/bin/bash

# Salir si ocurre algún error
set -e

# Instalar dependencias de Tailwind
cd theme
npm install
cd ..

# Compilar Tailwind en modo producción
python manage.py tailwind build

# Recolectar archivos estáticos
python manage.py collectstatic --noinput

# Aplicar migraciones
python manage.py migrate

# Ejecutar servidor Gunicorn
gunicorn gastrobot.wsgi:application --bind 0.0.0.0:8000