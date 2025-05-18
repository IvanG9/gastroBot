#!/bin/bash

echo "=== [startup.sh] Iniciando script de arranque ==="

echo "Paso 1: Migraciones de base de datos"
python gastrobot/manage.py migrate --noinput || {
    echo "❌ Error en migrate"
    exit 1
}

echo "Paso 2: Recolectando archivos estáticos"
python gastrobot/manage.py collectstatic --noinput || {
    echo "❌ Error en collectstatic"
    exit 1
}

echo "Paso 3: Lanzando gunicorn..."
gunicorn gastrobot.wsgi:application --bind=0.0.0.0:8000 --timeout 600 || {
    echo "❌ Error al iniciar gunicorn"
    exit 1
}

echo "✅ [startup.sh] Servidor iniciado correctamente"