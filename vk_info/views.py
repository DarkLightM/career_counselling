from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import DetailView

from .models import VkInfo
from profiles.models import Profile


class VkInfoPage(DetailView):
    model = VkInfo
    context_object_name = 'vk'
    template_name = 'vk_info/index.html'
    slug_url_kwarg = 'vk_slug'

    def get_object(self, queryset=None):
        profile = Profile.objects.get(slug=self.kwargs['profile_slug'])
        vk_info = VkInfo.objects.get(slug=self.kwargs['vk_slug'])
        if profile.vk_info_id != vk_info.pk:
            self.template_name = 'profiles/error.html'
        return VkInfo.objects.get(slug=self.kwargs['vk_slug'])


def create_vk_profile(request, profile_slug):
    return render(request, 'vk_info/create_vk_profile.html')
