web: gunicorn eng_backend.wsgi
worker:  celery worker -A eng_backend -l info -c 4
release: python manage.py makemigrations --noinput
release: python manage.py migrate --noinput
