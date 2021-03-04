from django.http import HttpResponse
from django.shortcuts import render

from articles.models import Article
from tours.models import *
from base.services import FooterAndMenuTemplateView
from tours.services.get_articles import get_articles

from tours.services.get_cities import get_cities_for_city
from tours.services.filters import get_count_tours, get_filters_queryset
from tours.services.get_h2 import get_h2
from tours.services.get_tours import get_tours, get_maximum


class CityPage(FooterAndMenuTemplateView):
    """
    Страница города
    """
    template_name = 'city/city.html'

    def add_in_context(self, context):
        context['tour_page_number'] = 0
        context['city'] = City.objects.get(slug=context['city_slug'])
        result_dict = get_tours(context['tour_page_number'], context['city'])
        context['tours'] = result_dict['list']
        context['more'] = result_dict['more']
        context['maximum'] = get_maximum(context['city'])
        context['cities'] = get_cities_for_city(context['city'])
        context['categories'] = get_filters_queryset(context['city'])
        context['magazine'] = get_articles(context['city'])
        context['h2'] = get_h2()


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
        context['recommended_tours'] = RecommendedTour.objects.filter(main=tour)


class MapPage(FooterAndMenuTemplateView):
    """
    Страница карт
    """
    template_name = "map/maps.html"

    def add_in_context(self, context):
        pass

# api


def get_more_tours(request):
    """
    обработка AJAX
    :param request: запрос
    :return: словарь из html-кода и bool отвечаюещго на вопрос есть ли ещё экскурсии
    """
    if not request.is_ajax():
        return HttpResponse(status=401)

    if request.method != 'GET':
        return HttpResponse(status=401)

    # номер страницы, которую нужно вернуть
    page = int(request.GET.get("page"))

    # город
    city = City.objects.get(slug=request.GET.get("city_slug"))
    result_dict = get_tours(page, city)

    # рендерим html
    response = render(request, 'city/elements/ajax_tours.html',
                      {'tours': result_dict['list'], 'page': page})

    # добавим куки который будет отвечать
    # за отображение кнопки показать ещё (bool, if true - показываем)
    response.set_cookie('more', result_dict['more'])

    return response


def get_count_tours_for_filter_list(request):
    if not request.is_ajax():
        return HttpResponse(status=401)

    if request.method != 'GET':
        return HttpResponse(status=401)

    # получаем список категорий
    list_category = request.GET.getlist('checked_array[]')

    # получаем city slug
    city_slug = request.GET.get('city_slug')

    # запрашиваем количество
    count = get_count_tours(list_category, city_slug)

    return HttpResponse(count)
