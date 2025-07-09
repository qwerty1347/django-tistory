#!/bin/bash
set -e

echo ">>> ENTRYPOINT SCRIPT START <<<"
cd /app

if [ ! -f "manage.py" ]; then
  django-admin startproject tistory .
fi

echo ">>> ENTRYPOINT SCRIPT END <<<"

exec python manage.py runserver 0.0.0.0:8000