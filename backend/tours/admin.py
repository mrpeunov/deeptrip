from django.contrib import admin
from .models import *


class ImageItemInline(admin.TabularInline):
    model = ImageItem
    extra = 1


class RecommendedTourInline(admin.TabularInline):
    model = RecommendedTour
    fk_name = "main"
    extra = 1


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'important', 'slug')
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ("important", )


@admin.register(Position)
class PositionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'lat', 'lon')


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('text', 'color')


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'notes', 'rating', 'count_comment')
    list_editable = ('notes',)
    readonly_fields = ('count_comment', 'rating')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('categories', )
    search_fields = ('title', 'notes')
    actions_on_top = False
    actions_on_bottom = True
    inlines = [ImageItemInline, RecommendedTourInline, CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('tour', 'name', 'content', 'date', 'grade')
