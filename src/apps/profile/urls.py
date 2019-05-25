from django.urls import path
from .views import DetailProfile


app_name = 'profile'



urlpatterns = [
    path('<slug:slug>/', DetailProfile.as_view(), name='profile_page')
]
