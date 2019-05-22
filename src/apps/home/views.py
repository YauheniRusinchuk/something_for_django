from django.views import View
from django.shortcuts import render, redirect
from src.models.twit.models import Twit


class Home(View):

    def get(self, request, *args, **kwargs):
        twits = Twit.objects.all()
        if not request.user.is_authenticated:
            return redirect('login:login_page')
        return render(request, 'home/index.html', {'twits': twits})
