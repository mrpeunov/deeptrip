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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city'] = City.objects.get(slug=context['city_slug'])
        context['tours'] = Tour.objects.all()
        return context


class ToursFilterPage(FooterAndMenuTemplateView):
    """
    Страница на которой показывается фильтр экскурсий
    """
    template_name = 'tours/filter.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city'] = City.objects.get(slug=context['city_slug'])
        context['tours'] = Tour.objects.all()
        return context


def tour_page(request, city_slug, tour_slug):
    """
    Страница одной экскурсии
    """
    tour = Tour.objects.get(city__slug=city_slug, slug=tour_slug)
    return render(request, 'tours/tour.html', locals())


def categories_page(request, city_slug):
    return HttpResponse("Все категории")


def category_page(request, city_slug, category_slug):
    """
    Страница категорий
    """
    category = Category.objects.get(city__slug=city_slug, slug=category_slug)
    return HttpResponse(category)


def maps_page(request, city_slug):
    return HttpResponse("Старица карт")
