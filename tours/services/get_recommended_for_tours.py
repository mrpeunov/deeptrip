from typing import Dict

from django.db.models import Q

from tours.models import Tour, ImageItem


def get_recommended_for_tours(tour: Tour, page: int) -> Dict:
    """
    Функция получения рекоменндованых экскурсий для определнной экскурсии
    :param tour: тур для которого возвращается значение
    :param page: номер 3-следующих экскурсий
    :return: словаь в экскурсиями и информацию о том, есть ли ещё экскурсии
    """
    more = True  # всё или нет

    start = page * 3
    finish = (page + 1) * 3

    # экскурсии из того же города, той же категории
    tours = Tour.objects.filter(
        Q(cities__in=[tour.city]) &
        Q(categories__in=tour.categories.all()) &
        ~Q(id=tour.id)).order_by("id")

    # того же кластера, той же категории
    tours.union(Tour.objects.filter(
        Q(cluster=tour.cluster) &
        Q(categories__in=tour.categories.all()) &
        ~Q(id=tour.id)).order_by("id"))

    # того же города
    tours.union(Tour.objects.filter(
        Q(cities__in=[tour.city]) &
        ~Q(categories__in=tour.categories.all()) &
        ~Q(id=tour.id)).order_by("id"))

    # того же кластера
    tours |= Tour.objects.filter(
        Q(cluster=tour.cluster) &
        ~Q(categories__in=tour.categories.all()) &
        ~Q(id=tour.id)).order_by("id")

    if tours.count() <= finish:
        finish = tours.count()
        more = False

    for tour in tours:
        tour.images = ImageItem.objects.filter(tour=tour)

    return {"tours": tours[start: finish],
            "more": more}
