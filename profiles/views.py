from django.http import *
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *
from transcriber.models import Transcriber


class Profiles(ListView):
    model = Profile
    template_name = 'profiles/index.html'
    context_object_name = 'profiles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Страница с профилями'
        return context


def profile_info(request, profile_slug):
    profile = Profile.objects.get(slug=profile_slug)
    transcribers = Transcriber.objects.filter(profile_id=profile.pk)
    print(transcribers)
    return render(request, 'profiles/profile.html', {'profile': profile, 'transcribers': transcribers})


class ClientInfo(DetailView):
    model = Client
    template_name = 'profiles/client.html'
    slug_url_kwarg = 'client_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Клиент ' + str(context['client'].name)
        return context

    def get_object(self, queryset=None):
        profile = Profile.objects.get(slug=self.kwargs['profile_slug'])
        client = Client.objects.get(slug=self.kwargs['client_slug'])
        if profile.client_id != client.pk:
            self.template_name = 'profiles/error.html'
        return Client.objects.get(slug=self.kwargs['client_slug'])


class CreateClient(CreateView):
    form_class = CreateClientForm
    template_name = 'profiles/create_client.html'


class CreateProfile(CreateView):
    form_class = CreateProfileForm
    template_name = 'profiles/create_profile.html'

