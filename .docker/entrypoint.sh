#!/bin/bash
set -e

cd /app

if [ ! -f "manage.py" ]; then
  django-admin startproject config .
fi

exec python manage.py runserver 0.0.0.0:8000