from django.http import HttpResponse
from django.shortcuts import render, redirect

from articles.models import Article
from tours.models import *
from base.services import FooterAndMenuTemplateView
from rest_framework.viewsets import ModelViewSet
from tours.serializers import TourSerializer
from tours.views_services.city import get_cities_for_city


class CityPage(FooterAndMenuTemplateView):
    """
    Страница города
    """
    template_name = 'city/city.html'

    def add_in_context(self, context):
        context['city'] = City.objects.get(slug=context['city_slug'])
        context['tours'] = Tour.objects.all()
        context['cities'] = get_cities_for_city(context['city_slug'])  # query_to_columns(City.objects.all())
        context['categories'] = Category.objects.all()
        context['magazine'] = Article.objects.all()


class FilterPage(FooterAndMenuTemplateView):
    """
    Страница на которой показывается фильтр экскурсий
    """
    template_name = 'city/elements/city_filter.html'

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


class MapPage(FooterAndMenuTemplateView):
    """
    Страница карт
    """
    template_name = "map/maps.html"

    def add_in_context(self, context):
        pass

# api


class ToursApiView(ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

