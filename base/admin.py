from django.contrib import admin
from .models import *


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ('site_name',)


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
