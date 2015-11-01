from django.contrib.auth import get_user_model
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from listings.models import GatheringCenter, Resource


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['gathering_centers'] = GatheringCenter.objects.filter(published=True)
        context['resources'] = Resource.objects.filter(published=True)
        return context


class LoginView(TemplateView):
    template_name = 'login.html'


class ProfileView(DetailView):
    model = get_user_model()
    context_object_name = 'profile'
    template_name = 'accounts/profile.html'

    def get_object(self, queryset=None):
        return self.request.user
