from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
from celery.task.control import revoke


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bethemillionaire.settings")

app = Celery('proj')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

"""app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'multiply_two_numbers',
        'schedule': 5.0,
        'args': (16, 16)
    },
}"""


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
