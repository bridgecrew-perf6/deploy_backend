web: gunicorn eng_backend.wsgi
celery: celery -A eng_backend worker --pool=solo -l info
release: python manage.py makemigrations --noinput
release: python manage.py migrate --noinput
