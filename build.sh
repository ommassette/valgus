#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# This line creates the user using the variables you just saved
python manage.py createsuperuser --no-input || true