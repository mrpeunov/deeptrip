from django.http import HttpResponse
from django.shortcuts import render, redirect
from tours.models import Tour, Category
from base.models import City
from base.services import FooterAndMenuTemplateView


class CityPage(FooterAndMenuTemplateView):
    """
    Страница города !! нужна ли здест эта вьюхашшш
    """
    template_name = 'base/city.html'

    def add_in_context(self, context):
        context['city'] = City.objects.get(slug=context['city_slug'])
        context['tours'] = Tour.objects.all()


class ToursFilterPage(FooterAndMenuTemplateView):
    """
    Страница на которой показывается фильтр экскурсий
    """
    template_name = 'tours/filter.html'

    def add_in_context(self, context):
        context['city'] = City.objects.get(slug=context['city_slug'])
        context['tours'] = Tour.objects.all()


class TourPage(FooterAndMenuTemplateView):
    """
    Страница одной экскурсии
    """
    template_name = 'tours/tour.html'

    def add_in_context(self, context):
        context['tour'] = Tour.objects.get(
            city__slug=context['city_slug'],
            slug=context['tour_slug'])


class CategoriesPage(FooterAndMenuTemplateView):
    """
    Страница всех категорий
    """
    template_name = "tours/categories.html"

    def add_in_context(self, context):
        context['city'] = City.objects.get(slug=context['city_slug'])
        context['categories'] = Category.objects.all()


class CategoryPage(FooterAndMenuTemplateView):
    """
    Страница категории
    """
    template_name = "tours/categories.html"

    def add_in_context(self, context):
        context['category'] = Category.objects.get(slug=context['category_slug'], city__slug=context['city_slug'])


class MapsPage(FooterAndMenuTemplateView):
    """
    Страница карт
    """
    template_name = "tours/maps.html"

    def add_in_context(self, context):
        pass
