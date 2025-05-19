#!/bin/bash
set -e

cd theme
npm install
cd ..

python manage.py tailwind build
python manage.py collectstatic --noinput
python manage.py migrate