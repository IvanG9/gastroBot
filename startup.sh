#!/bin/bash
set -e

cd gastrobot

#python manage.py tailwind install
#python manage.py tailwind build
python manage.py collectstatic --noinput
# python manage.py migrate