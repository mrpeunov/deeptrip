from django.contrib import admin
from .models import *


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'views', 'comments')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
