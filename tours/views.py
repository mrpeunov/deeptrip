import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import MultipleObjectMixin

from articles.models import Article
from tours.models import *
from base.services import FooterAndMenuTemplateView
from rest_framework.viewsets import ModelViewSet
from tours.serializers import TourSerializer
from tours.services.get_cities import get_cities_for_city
from tours.services.get_tours import get_tours


def get_more_tours(request):
    """"""
    if not request.is_ajax():
        pass
    if request.method != 'GET':
        pass

    page = int(request.GET.get("page"))
    city = City.objects.get(slug=request.GET.get("city_slug"))
    touts_list = get_tours(page, city)

    return render(request, 'city/elements/ajax_tours.html',
                  {'tours': touts_list, 'page': page})


class CityPage(FooterAndMenuTemplateView):
    """
    Страница города
    """
    template_name = 'city/city.html'

    def add_in_context(self, context):
        context['tour_page_number'] = 0
        context['city'] = City.objects.get(slug=context['city_slug'])
        context['tours'] = get_tours(context['tour_page_number'], context['city'])
        context['cities'] = get_cities_for_city(context['city_slug'])
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

