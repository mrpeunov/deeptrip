import datetime

from django.http import HttpResponse
from django.shortcuts import render

from orders.models import Order
from tours.models import Tour, Position


def new_order(request):
    """
    обработка AJAX
    :param request: запрос
    :return: количество экскурсий
    """
    if not request.is_ajax():
        return HttpResponse(status=401)

    if request.method != 'POST':
        return HttpResponse(status=401)

    print(request.POST)
    order = Order()

    order.name = request.POST.get("name")
    order.phone = request.POST.get("phone")
    order.mail = request.POST.get("mail")

    order.tour = Tour.objects.get(slug=request.POST.get("tour_slug"))

    day = int(request.POST.get('date_tour[day]'))
    month = int(request.POST.get('date_tour[month]'))
    year = int(request.POST.get('date_tour[year]'))
    order.date_tour = datetime.date(year, month, day)

    order.start_tour = request.POST.get("start_tour")

    order.rate = request.POST.get('rate')
    order.group = request.POST.get('group')
    order.children = request.POST.get('children')

    order.amount = int(request.POST.get('amount'))
    order.prepay = int(request.POST.get('prepay'))
    order.payment = order.amount - order.prepay
    order.transfer = False
    order.place = Position.objects.last()

    order.commission_percent = 0
    order.commission_money = 0

    order.save()
    return HttpResponse("OK")

