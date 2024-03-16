from __future__ import absolute_import, unicode_literals
from celery import Celery
from django.conf import settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Profilehub.settings')
app = Celery("Profilehub")
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
