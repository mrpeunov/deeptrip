from django.db import models


class Position(models.Model):
    name = models.CharField("Название позиции", max_length=32)
    lat = models.FloatField("Широта")
    lon = models.FloatField("Долгота")

    def __str__(self):
        return "Точка '{}'".format(self.name)

    class Meta:
        verbose_name = "точка на карте"
        verbose_name_plural = "точки на карте"
