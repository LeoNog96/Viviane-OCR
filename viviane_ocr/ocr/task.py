from celery import shared_task
from . import services


@shared_task(queue='default')
def ocr_task(file):
    services.ocr_run(file)