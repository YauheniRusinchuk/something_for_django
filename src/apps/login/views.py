from django.views import View
from django.shortcuts import render

class Login(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'login/login.html', {})
