from typing import List
from django.db.models import QuerySet, Q
from tours.models import Tour, City


def get_tours(page: int, city: City) -> List[Tour]:
    """
    :param city: город для которого необходимо составить список экскурсий
    :param page: запрашиваемая страница
    :return: список экускурсий
    """

    # получим queryset со всеми экскурсиями принадлежащими городу
    all_city_tours = Tour.objects.filter(Q(cities__exact=city) | Q(city=city)).distinct().order_by("id")

    # отсортируем его по формуле
    all_city_tours = list(all_city_tours)
    all_city_tours.sort(key=lambda x: x.get_rating_for_city(city), reverse=True)

    # вернём обрезанный в соответсвии с номером страницы
    start = get_start_number(page)
    count = get_count(page)
    finish = start + count

    return all_city_tours[start:finish]


def get_start_number(page: int) -> int:
    """
    на 0 и на 3 странице появояется лишний блок
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
