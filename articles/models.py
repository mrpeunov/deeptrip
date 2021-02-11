from django.db import models
from tours.models import Tour
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField("Название", max_length=64)
    content = RichTextField("Контент")
    date = models.DateField("Дата", auto_now=True)
    views = models.IntegerField("Количество просмотров", default=0)
    comments = models.IntegerField("Количество комментов", default=0)
    image = models.ImageField("Изображение")

    def __str__(self):
        return "Статья {}".format(self.title)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.PROTECT)
    name = models.CharField("Имя пользователя", max_length=32)
    content = models.TextField("Текст комментария")
    date = models.DateField("Дата", auto_now=True)

    def __str__(self):
        return "Комментарий от {}".format(self.name)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комметарии"
