import os
from celery import Celery
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eng_backend.settings')

app = Celery('eng_backend')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.update(BROKER_URL='amqps://gwewsfku:1Ek9hM3tes4wOaXJQ0D-YNbndmjGX2WO@sparrow.rmq.cloudamqp.com/gwewsfku')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')