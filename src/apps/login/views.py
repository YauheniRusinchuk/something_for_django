from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

class Login(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'login/login.html', {})

    def post(self, request, *args, **kwargs):
        email       = request.POST.get('email')
        password    = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home_page')
        else:
            return redirect('login:login_page')
