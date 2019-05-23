from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task
from config.celery import app

@app.task
def get_email(msg):
    print("CELERY")
    send_mail('test', msg, settings.EMAIL_HOST_USER, ['ruevgal@gmail.com'], fail_silently=False)
