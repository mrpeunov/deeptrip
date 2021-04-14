from typing import List, Dict, Union
from django.db.models import QuerySet, Q
from tours.models import Tour, City, ImageItem


def get_tours(page: int, city: City) -> Dict[str, Union[list, bool]]:
    """
    :param city: город для которого необходимо составить список экскурсий
    :param page: запрашиваемая страница
    :return: список экускурсий
    """

    # получим queryset со всеми экскурсиями принадлежащими городу
    all_city_tours = get_all_tours(city)

    # отсортируем его по формуле
    all_city_tours = list(all_city_tours)
    all_city_tours.sort(key=lambda x: x.get_rating_for_city(city), reverse=True)

    # вернём обрезанный в соответсвии с номером страницы
    start = get_start_number(page)
    count = get_count(page)

    finish = start + count
    more = True

    # если не хватает экскурсий
    list_length = len(all_city_tours)
    if finish >= list_length:
        finish = list_length
        more = False

    return {'list': all_city_tours[start:finish],
            'more': more}


def get_start_number(page: int) -> int:
    """
    на 0 и на 3 странице появляется лишний блок
    :param page: номер страницы
    :return: номер начального лимита экскурсий
    """
    start = 0

    if 0 < page < 4:
        start = page * 18

    if page == 4:
        start = page * 18 - 1

    return start


def get_count(page: int) -> int:
    """
    на 0 и на 3 странице появояется лишний блок, потому количество меньше
    :param page: номер страницы
    :return: количество городов на странице
    """
    count = 18
    if page in (0, 3):
        count = 17
    return count


def get_all_tours(city: City) -> QuerySet[City]:
    tours = Tour.objects.filter(Q(cities__exact=city) | Q(city=city)).distinct().order_by("id")
    for tour in tours:
        tour.images = ImageItem.objects.filter(tour=tour)
    return tours


def get_maximum(city: City) -> int:
    all_city_tours = get_all_tours(city)
    return all_city_tours.count()

