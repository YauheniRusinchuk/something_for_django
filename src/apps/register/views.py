from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from src.models.profile.models import Profile

User = get_user_model()


class RegisterView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'register/index.html', {})


    def post(self, request, *args, **kwargs):
        qs = User.objects.filter(email=request.POST.get('email'))
        if qs.exists():
            return redirect('register:register_page')
        user = User(email=request.POST.get('email'))
        user.set_password(request.POST.get('password'))
        user.save()
        profile = Profile(user=user, login=request.POST.get('username'))
        profile.save()
        return redirect('login:login_page')
