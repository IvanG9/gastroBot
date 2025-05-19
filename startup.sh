#!/bin/bash
set -e

# Instala dependencias Tailwind
python manage.py tailwind install

# Compila Tailwind
python manage.py tailwind build

# Archivos estáticos y migraciones
python manage.py collectstatic --noinput
python manage.py migrate