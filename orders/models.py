from django.db import models
from tours.models import Tour, Position, Variable, Rate


class Order(models.Model):
    name = models.CharField("Имя", max_length=32)
    phone = models.CharField("Телефон", max_length=32)
    mail = models.CharField("Почта", max_length=64, blank=True)
    tour = models.ForeignKey(Tour, verbose_name="Экскурсия", on_delete=models.PROTECT)
    date_tour = models.DateField("Дата")
    start_tour = models.TimeField("Начало")
    datetime_order = models.DateTimeField("Дата и время создания", auto_now_add=True)
    rate = models.ForeignKey(Rate, verbose_name="Тариф", related_name="rate", blank=True, on_delete=models.PROTECT)
    group = models.ForeignKey(Rate, verbose_name="Группа", related_name="group", blank=True, on_delete=models.PROTECT)
    children = models.ForeignKey(Rate, verbose_name="Дети", related_name="children", blank=True, on_delete=models.PROTECT)
    amount = models.FloatField("Общая сумма заказа")
    prepay = models.FloatField("Внесённая предоплата")
    payment = models.FloatField("Остаток оплаты")
    transfer = models.BooleanField("Трансфер")
    place = models.ForeignKey(Position, verbose_name="Место встречи", on_delete=models.PROTECT)

    commission_percent = models.IntegerField("Коммиссия (%)")
    commission_money = models.FloatField("Коммисия (рубли)")

    def __str__(self):
        return "Заказа №{} от {}".format(self.id, self.name)

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы"


