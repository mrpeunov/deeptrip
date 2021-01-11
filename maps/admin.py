from django.contrib import admin
from .models import *


@admin.register(Position)
class PositionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'lat', 'lon')
