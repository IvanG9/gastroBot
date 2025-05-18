#!/bin/bash
# Ejecutar migraciones y collectstatic
python gastrobot/manage.py migrate --noinput
python gastrobot/manage.py collectstatic --noinput

# Iniciar servidor gunicorn en el puerto 8000
gunicorn gastrobot.wsgi:application --bind=0.0.0.0:8000 --timeout 600
