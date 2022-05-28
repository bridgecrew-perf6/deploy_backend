web: gunicorn eng_backend.wsgi
worker: celery worker --app=tasks.app
release: python manage.py makemigrations --noinput
release: python manage.py migrate --noinput
