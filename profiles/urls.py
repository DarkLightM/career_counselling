from django.urls import path, include

from profiles.views import *

urlpatterns = [
    path('', Profiles.as_view(), name='profiles'),
    path('create_client/', CreateClient.as_view(), name='create_client'),
    path('create_profile/', CreateProfile.as_view(), name='create_profile'),
    path('profile/<slug:profile_slug>/', profile_info, name='profile'),
    path('profile/<slug:profile_slug>/client/<slug:client_slug>', ClientInfo.as_view(), name='client'),
    path('profile/<slug:profile_slug>/transcribers/', include('transcriber.urls')),
    path('profile/<slug:profile_slug>/vk_info/', include('vk_info.urls')),
    path('profile/<slug:profile_slug>/analytics/', include('analytics.urls')),
]
