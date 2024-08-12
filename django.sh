#!/bin/bash

echo "================================================="
echo "================================================="
echo "================================================="
echo "Create migrations"
python manage.py makemigrations
echo "================================================="

echo "Migrate"
python manage.py migrate
echo "================================================="

echo "Collect Static Files"
python manage.py collectstatic --noinput
echo "================================================="

echo "Start Server"
gunicorn backend.wsgi:application --config gunicorn_config.py