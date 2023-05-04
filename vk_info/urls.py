from django.urls import path

from vk_info.views import *

urlpatterns = [
    path('show/<slug:vk_slug>/', VkInfoPage.as_view(), name='vk_home'),
    path('create_vk_profile/', create_vk_profile, name='create_vk_profile')
]