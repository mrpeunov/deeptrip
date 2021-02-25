import datetime


def get_h2() -> str:
    """
    возвращает h2 заголовок для страницы города
    :return: готовый h2
    """
    now = datetime.datetime.now()
    month = now.month - 1
    first_month = get_month_str(month)
    last_month = get_month_str((month + 1) % 12)
    if month != 11:
        return "В {} и {} {}".format(first_month, last_month, now.year)
    else:
        return "В {} {} и {} {}".format(first_month, now.year, last_month, now.year + 1)


def get_month_str(month: int) -> str:
    month_array = ("январе",
                   "феврале",
                   "марте",
                   "апреле",
                   "мае",
                   "июне",
                   "июле",
                   "августе",
                   "сентябре",
                   "октябре",
                   "ноябре",
                   "декабре")

    return month_array[month]
