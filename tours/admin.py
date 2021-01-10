from django.contrib import admin
from .models import *


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'tours_count', 'orders_count')
    prepopulated_fields = {"slug": ("name", ), "seo_title": ("name", ), "seo_description": ("name", )}


admin.site.register(City, CityAdmin)

