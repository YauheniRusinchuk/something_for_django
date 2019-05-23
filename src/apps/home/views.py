from django.views import View
from django.shortcuts import render, redirect
from src.models.twit.models import Twit
from src.models.profile.models import Profile


class Home(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login:login_page')
        twits = Twit.objects.filter(profile__in=request.user.profile.followers.all())
        return render(request, 'home/index.html', {'twits': twits})


    def post(self, request, *args, **kwargs):
        twit = Twit(profile=request.user.profile, text=request.POST.get('text'))
        twit.save()
        return redirect('home:home_page')
