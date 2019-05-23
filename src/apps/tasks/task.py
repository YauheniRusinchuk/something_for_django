from django.core.mail import send_mail
from config.celery import app
from django.conf import settings

@app.task
def get_email(msg):
    print("CELERY")
    send_mail('test', msg, settings.EMAIL_HOST_USER, 'ruevgal@gmail.com',fail_silently=False,)
