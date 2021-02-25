from typing import List

from django.db.models import Q, QuerySet

from tours.models import Tour, City, Category


def get_filters_queryset(city: City) -> QuerySet[Category]:
    # queryset = Category.objects.
    pass


def get_count_tours(list_categories_str: List[str], city_slug: str) -> int:
    """
    возвращет количество экскурсий для списка категорий
    :param list_categories_str: список слагов категорий
    :param city_slug: слаг города
    :return: количество экскурсий
    """
    # создаём пустой QuerySet
    query = Tour.objects.none()

    # поочерёдно ищем подходящие экскурсии
    for item in list_categories_str:
        query |= Tour.objects.filter(
            (Q(city__slug=city_slug) | Q(cities__slug=city_slug))
            & Q(categories__slug=item)
        )

    # объединяем join-ы и считаем
    count = query.distinct().count()

    return count
