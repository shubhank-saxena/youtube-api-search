#!/usr/bin/env bash

python manage.py makemigrations
python manage.py createcachetable
python manage.py migrate
python manage.py startservice

python manage.py qcluster

gunicorn fampay.wsgi:application --bind 0.0.0.0:$PORT