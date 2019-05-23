# from django.db.models import signals
# from src.apps.tasks.task import get_email
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#
#
# def user_post_save(sender, instance, signal, *args, **kwargs):
#     if instance:
#         print("INSTANCE")
#         #get_email.delay("SYKI")
#
# signals.post_save.connect(user_post_save, sender=User)
