from typing import List

from tours.models import City
from django.db.models import Q


def _query_to_columns(query):
    доделать
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


def get_cities_for_city(city_slug: str) -> List[List[City]]:
    """получаем в"""
    wait_count_objects = 8

    city = City.objects.get(slug=city_slug)

    # запрашиваем 8 городов из кластера
    cities_query = City.objects.filter(cluster=city.cluster).order_by('name')[:wait_count_objects]
    really_count_objects = len(cities_query)
    if len(cities_query) != wait_count_objects:
        # если полученно менее 8 городов, то дополняем до 8 по возможности
        cities_query |= City.objects.filter(~Q(cluster=city.cluster))[:wait_count_objects - really_count_objects]
    return _query_to_columns(cities_query)




