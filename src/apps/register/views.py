from django.views import View
from django.shortcuts import render


class RegisterView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'register/index.html', {})
