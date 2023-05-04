from django.contrib import admin
from .models import *


class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Analytics, AnalyticsAdmin)
