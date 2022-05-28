web: gunicorn eng_backend.wsgi
worker: celery -A  worker attendanceapp.tasks -B --loglevel=info
release: python manage.py makemigrations --noinput
release: python manage.py migrate --noinput
