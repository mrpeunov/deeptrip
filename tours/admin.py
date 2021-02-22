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


class TourCitiesInline(admin.TabularInline):
    model = Tour.cities.through
    extra = 8


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'important', 'slug')
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ("important", )


@admin.register(Cluster)
class ClusterAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Position)
class PositionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'lat', 'lon')


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('text', 'color')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'cluster', 'slug', 'importance', 'tours_count', 'orders_count')
    readonly_fields = ('tours_count', 'orders_count')
    list_editable = ('importance',)
    prepopulated_fields = {"slug": ("name", )}
    actions_on_top = False
    actions_on_bottom = True


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

    """
    def get_object(self, request, object_id, from_field=None):
        obj = super().get_object(request, object_id, from_field=from_field)
        request.report_obj = obj
        return obj

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "cities" and hasattr(request, 'report_obj'):
            kwargs["queryset"] = City.objects.filter(cluster=request.report_obj.city.cluster)
        return super(TourAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
    """


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('tour', 'name', 'content', 'date', 'grade')
