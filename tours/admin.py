from django.contrib import admin
import nested_admin.nested as nested

from .models import *
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


class ImageItemInline(admin.TabularInline):
    sortable_options = 'variable'
    model = ImageItem
    extra = 1


class CommentInline(admin.TabularInline):
    sortable_options = 'name'
    model = Comment
    extra = 1


class TourCitiesInline(admin.TabularInline):
    model = Tour.cities.through
    extra = 8


class RateInline(nested.NestedTabularInline):
    model = Rate
    sortable_field_name = 'variable'
    extra = 1


class VariableInline(nested.NestedTabularInline):
    model = Variable
    extra = 1
    sortable_field_name = 'tour'
    inlines = [RateInline]


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


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'cluster', 'slug', 'importance', 'tours_count', 'orders_count')
    readonly_fields = ('tours_count', 'orders_count')
    list_editable = ('importance',)
    prepopulated_fields = {"slug": ("name", )}
    actions_on_top = False
    actions_on_bottom = True


@admin.register(Tour)
class TourAdmin(nested.NestedModelAdmin, DynamicArrayMixin):
    list_display = ('title', 'notes', 'rating', 'count_comment')
    list_editable = ('notes',)
    readonly_fields = ('count_comment', 'rating')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('categories', 'cities')
    search_fields = ('title', 'notes')
    actions_on_top = False
    actions_on_bottom = True
    inlines = [VariableInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('tour', 'name', 'content', 'date', 'grade', 'show')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'tour', 'date', 'email', 'phone', 'answer', 'note')
    readonly_fields = ['date']


@admin.register(Variable)
class VariableAdmin(nested.NestedModelAdmin):
    inlines = [RateInline]


@admin.register(Rate)
class RateAdmin(nested.NestedModelAdmin):
    list_display = ('price', )
