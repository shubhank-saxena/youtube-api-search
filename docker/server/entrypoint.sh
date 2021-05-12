#!/usr/bin/env bash

python manage.py makemigrations
python manage.py createcachetable
python manage.py migrate
python manage.py startservice

gunicorn backend.config.wsgi:application --bind 0.0.0.0:8000 --daemon

python manage.py qcluster