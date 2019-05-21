from django.views import View
from django.shortcuts import render, redirect

class Home(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login:login_page')
        return render(request, 'home/index.html', {})
