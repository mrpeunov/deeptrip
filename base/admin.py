from django.contrib import admin
from .models import *


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ('site_name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'tours_count', 'orders_count')
    prepopulated_fields = {"slug": ("name", )}
    actions_on_top = False
    actions_on_bottom = True


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
