from typing import List
from tours.models import City
from django.db.models import Q, QuerySet


def _query_to_columns(query: List[City]) -> List[List[City]]:
    """преобразуем в список, состоящий из списков по 2 элемента для отображения в слайдере"""
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


def get_cities_for_city(city: City) -> List[List[City]]:
    """
    Возвращает список городов в определенном виде
    :param city_slug:
    :return: список, состоящий из списков по 2 элемента
    """
    # ожидаем получить 8 городов
    wait_count_objects = 8

    city_slug = city.slug

    # запрашиваем 8 городов с количество экускурсий >0 из кластера полученного города,
    # кроме самого этого города и сортируем по важности
    cities_query = list(
        City.objects.filter(
            Q(cluster=city.cluster) &
            ~Q(slug=city_slug) &
            ~Q(tours_count=0)).order_by('-importance')[:wait_count_objects])
    really_count_objects = len(cities_query)

    # если менее 8 городов, то дополняем список экскурсиями из кластера полученного города
    # с 0 экскурсий и сортируем по важности
    if really_count_objects != wait_count_objects:
        cities_query += list(City.objects.filter(
            Q(cluster=city.cluster) &
            ~Q(slug=city_slug) &
            Q(tours_count=0)).order_by('-importance')[:wait_count_objects - really_count_objects])
        really_count_objects = len(cities_query)

    # если менее 8 городов, то дополняем до 8 из городов других кластеров
    if really_count_objects != wait_count_objects:
        cities_query += list(City.objects.filter(~Q(cluster=city.cluster)).order_by('-importance')
                             [:wait_count_objects - really_count_objects])

    return _query_to_columns(cities_query)
