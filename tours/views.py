from django.http import HttpResponse
from django.shortcuts import render, redirect

from articles.models import Article
from tours.models import *
from base.models import City
from base.services import FooterAndMenuTemplateView
from rest_framework.viewsets import ModelViewSet

from tours.serializers import TourSerializer


class CityPage(FooterAndMenuTemplateView):
    """
    Страница города !! нужна ли здест эта вьюха
    """
    template_name = 'base/city.html'

    def add_in_context(self, context):
        context['city'] = City.objects.get(slug=context['city_slug'])
        context['tours'] = Tour.objects.all()
        context['towns'] = query_to_columns(Town.objects.all())
        context['categories'] = Category.objects.all()
        context['articles'] = Article.objects.all()


def query_to_columns(query):
    columns = list()
    column = list()
    i = 0
    for item in query:
        column.append(item)
        if i % 2 == 1:
            columns.append(column)
            column = list()
        i += 1
    if len(column) > 0:
        columns.append(column)
    return columns


class ToursFilterPage(FooterAndMenuTemplateView):
    """
    Страница на которой показывается фильтр экскурсий
    """
    # template_name = 'tours/../templates/Base/elements/city_filter.html'

    def add_in_context(self, context):
        context['city'] = City.objects.get(slug=context['city_slug'])
        context['tours'] = Tour.objects.all()


class TourPage(FooterAndMenuTemplateView):
    """
    Страница одной экскурсии
    """
    template_name = 'tours/tour.html'

    def add_in_context(self, context):
        tour = Tour.objects.get(
            city__slug=context['city_slug'],
            slug=context['tour_slug'])
        context['tour'] = tour
        context['comments'] = Comment.objects.filter(tour=tour)
        context['image_items'] = ImageItem.objects.filter(tour=tour)
        print(context['image_items'])
        context['recommended_tours'] = RecommendedTour.objects.filter(main=tour)


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


# api

class ToursApiView(ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

