from django.contrib import admin
from .models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'second_name', 'time_update')
    list_display_links = ('name', 'surname', 'second_name')
    search_fields = ('name', 'surname')
    prepopulated_fields = {'slug': ('surname', 'name', 'second_name')}


admin.site.register(Client, ClientAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name', 'client')
    prepopulated_fields = {'slug': ('name', 'client')}


admin.site.register(Profile, ProfileAdmin)
