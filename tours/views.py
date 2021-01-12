from django.http import HttpResponse
from django.shortcuts import render

from tours.models import Tour
from base.models import City


def tours_filter_page(request, city):
    """
    Страница на которой показывается фильтр экскурсий
    """
    city = City.objects.get(slug=city)
    return HttpResponse("Все экскурсии в {}".format(city.name))


def tour_page(request, city, slug):
    """
    Страница одной экскурсии
    """
    tour = Tour.objects.get(slug=slug, city__slug=city)
    return HttpResponse("Экскурсия {}".format(tour.title))
