from django.urls import path
from .views import exit

app_name = 'exit'

urlpatterns = [
    path('', exit, name='exit_page')
]
