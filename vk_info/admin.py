from django.contrib import admin

from vk_info.models import VkInfo


class VkAdmin(admin.ModelAdmin):
    list_display = ('client_url', 'client_surname', 'client_name', 'time_update')
    list_display_links = ('client_url',)
    search_fields = ('name', 'surname', 'client_url')
    prepopulated_fields = {'slug': ('client_surname', 'client_name', 'client_url')}


admin.site.register(VkInfo, VkAdmin)
