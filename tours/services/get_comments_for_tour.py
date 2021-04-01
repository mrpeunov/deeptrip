from typing import Dict, Union
from django.db.models import QuerySet

from tours.models import Tour, Comment


def get_comments_for_tour(page: int, tour: Tour) -> Dict[str, Union[list, bool]]:
    """
    Показывает дополнительные комментарии пользователю
    :param page: страница комментариев
    :param tour: экскрусия
    :return: словаь со списком и информацией об оставшихся
    """
    all_tour_comments = get_all_comments(tour)

    maximum = all_tour_comments.count()

    start = get_start_number(page)
    finish = get_finish_number(page, maximum)

    more = True
    if finish == maximum:
        more = False

    print(all_tour_comments[start:finish])
    print(start, finish)

    return {'list': all_tour_comments[start:finish],
            'more': more}


def get_all_comments(tour: Tour) -> QuerySet[Comment]:
    """
    Возвращается все необхоимые комментарии
    :param tour: экскурсия
    """
    return Comment.objects.filter(tour=tour, show=True).order_by("-date")


def get_start_number(page: int) -> int:
    """
    Вычисляет стартовый номер
    :param page: страница
    :return: итоговый номер
    """
    if page == 0:
        return 0
    return 6 + (page - 1) * 10


def get_finish_number(page: int, maximum: int) -> int:
    """
    Вычисляет финишный номер
    :param page: страница
    :param maximum: максимальный номер
    :return: финишный номер
    """
    if page == 0:
        if maximum < 6:
            return maximum
        else:
            return 6
    else:
        finish = 6 + page * 10
        if finish < maximum:
            return finish
        else:
            return maximum
