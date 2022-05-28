export LANG=C.UTF-8

gunicorn eng_backend.wsgi — bind=0.0.0.0 — timeout 600 config.wsgi & celery -A eng_backend worker --pool=solo -l info