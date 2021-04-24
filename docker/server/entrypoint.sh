#!/bin/sh

python manage.py migrate
python manage.py collectstatic --no-input
gunicorn -w 3 -b :8000 backend.config.wsgi:application