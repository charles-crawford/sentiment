import os
from celery import Celery

PKG_NAME = os.path.dirname(os.path.realpath(__file__)).split("/")[-2]


def make_celery(app_name=PKG_NAME):
    backend = os.getenv('CELERY_BROKER_URL')
    broker = os.getenv('CELERY_RESULT_BACKEND')
    include = ['application.utils.utils']
    return Celery(app_name, backend=backend, broker=broker, include=include)


celery = make_celery()
