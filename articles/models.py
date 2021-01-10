from django.db import models
from tours.models import Tour
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField("Название", max_length=64)
    content = RichTextField("Контент")
    date = models.DateField("Дата", auto_now=True)
    views = models.IntegerField("Количество просмотров", default=0)
    comments = models.IntegerField("Количество комментов", default=0)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.PROTECT)
    name = models.CharField("Имя пользователя", max_length=32)
    content = models.TextField("Текст комментария")
    date = models.DateField("Дата", auto_now=True)

