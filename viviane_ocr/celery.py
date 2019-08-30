import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'viviane_ocr.settings') #1
app = Celery('viviane_ocr') #2
app.config_from_object('django.conf:settings') #3
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS) #4