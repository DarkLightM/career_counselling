from django.http import HttpResponseForbidden
from django.shortcuts import render

from analytics.models import Analytics
from profiles.models import Profile


def index(request, profile_slug, analytics_slug):
    profile = Profile.objects.get(slug=profile_slug)
    analytics = Analytics.objects.get(slug=analytics_slug)
    if profile.analytics_id == analytics.pk:
        return render(request, 'analytics/index.html', {'analytics': analytics})
    else:
        return HttpResponseForbidden('<h1>Невозможно просмотреть данные клиента, несвязанного с данным профилем</h1>')
