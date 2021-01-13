from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *


def index(request):
    """
    Главная страница
    Изначально главная страница - это страница города Сочи
    Если его нет в бд, то возвращается извещение о разработке сайта
    """
    try:
        City.objects.get(slug="sochi")
        return redirect('/sochi/')
    except City.DoesNotExist:
        return HttpResponse("Сайт в разработке")
