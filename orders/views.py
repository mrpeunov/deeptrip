import datetime

from django.http import HttpResponse
from django.shortcuts import render

from orders.models import Order
from tours.models import Tour, Position, Variable, Rate


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
    month = int(request.POST.get('date_tour[month]')) + 1
    year = int(request.POST.get('date_tour[year]'))
    order.date_tour = datetime.date(year, month, day)

    order.start_tour = request.POST.get("start_tour")

    variables = Variable.objects.filter(tour=order.tour)

    for variable in variables:
        if variable.type == 'r' and request.POST.get('rate'):
            order.rate = Rate.objects.get(variable=variable, name=request.POST.get('rate'))
        if variable.type == 'g' and request.POST.get('group'):
            order.group = Rate.objects.get(variable=variable, name=request.POST.get('group'))
        if variable.type == 'c' and request.POST.get('children'):
            order.children = Rate.objects.get(variable=variable, name=request.POST.get('children'))

    order.amount = int(request.POST.get('amount'))
    order.prepay = int(request.POST.get('prepay'))
    order.payment = order.amount - order.prepay
    print(request.POST.get('transfer'))
    order.transfer = request.POST.get('transfer')
    order.place = Position.objects.last()

    order.commission_percent = order.tour.commission
    order.commission_money = order.amount * order.commission_percent / 100

    order.save()
    return HttpResponse("OK")

