from django.views.generic.detail import DetailView
from src.models.profile.models import Profile


class DetailProfile(DetailView):
    model           = Profile
    template_name   = 'profile/detail.html'
    slug_url_kwarg  = 'slug'
