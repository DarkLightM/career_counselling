from django.contrib import admin
from .models import *


class TranscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile')
    list_display_links = ('name', 'profile')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name', 'profile')}


admin.site.register(Transcriber, TranscriberAdmin)
