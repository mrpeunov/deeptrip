from django.db.models import Q

from tours.models import Tour


def get_recommended_for_tours(tour: Tour, page: int):
    more = True  # всё или нет

    start = page * 3
    finish = (page + 1) * 3

    # экскурсии из того же города, той же категории
    tours = Tour.objects.filter(
        Q(cities__in=[tour.city]) &
        Q(categories__in=tour.categories.all()) &
        ~Q(id=tour.id)).order_by("id")

    print("Шаг 1", tours)

    # того же кластера, той же категории
    tours.union(Tour.objects.filter(
        Q(cluster=tour.cluster) &
        Q(categories__in=tour.categories.all()) &
        ~Q(id=tour.id)).order_by("id"))

    print("Шаг 2", tours)

    # того же города
    tours.union(Tour.objects.filter(
        Q(cities__in=[tour.city]) &
        ~Q(categories__in=tour.categories.all()) &
        ~Q(id=tour.id)).order_by("id"))

    print("Шаг 3", tours)

    # того же кластера
    tours |= Tour.objects.filter(
        Q(cluster=tour.cluster) &
        ~Q(categories__in=tour.categories.all()) &
        ~Q(id=tour.id)).order_by("id")

    print("Шаг 4", tours)

    if tours.count() <= finish:
        finish = tours.count()
        more = False

    print(start, finish)
    print(tours[start: finish])

    return {"tours": tours[start: finish],
            "more": more}
