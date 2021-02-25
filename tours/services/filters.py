from typing import List

from django.db.models import Q, QuerySet

from tours.models import Tour, City, Category


def get_filters_queryset(city: City) -> List[Category]:
    maximum = 9

    # состави queryset для города
    category_queryset = Category.objects.none()
    tour_queryset = Tour.objects.filter(Q(city=city) | Q(cities=city))
    for tour in tour_queryset:
        category_queryset |= tour.categories.all()

    # избавимся от дубликатов
    category_queryset = category_queryset.distinct()
    count = category_queryset.count()

    if count >= maximum:
        return list(category_queryset[:maximum])
    else:
        category_list = list(category_queryset)
        # дополняем до максимума
        for category in Category.objects.all():
            if category not in category_list:
                category_list.append(category)
                count += 1

                if count == maximum:
                    break
        return category_list


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
