from django.urls import path

from analytics.views import index


urlpatterns = [
    path('show/<slug:analytics_slug>/', index)
]