from django.core.mail import send_mail
from django.conf import settings
from config.celery import app

@app.task
def get_email(email):
    send_mail('Hi, You are registered in our service, thanks ',
              'Thank you for being with us)',
              settings.EMAIL_HOST_USER,
              [email],
              fail_silently=False
    )
