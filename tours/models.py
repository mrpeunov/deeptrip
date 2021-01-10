from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from maps.models import Position


class City(models.Model):
    name = models.CharField("Название города", max_length=32)
    seo_title = models.CharField("Заговок страницы (SEO)", max_length=64)
    seo_description = models.CharField("Заголовок страницы (SEO)", max_length=128)
    slug = models.SlugField("Slug (название в URL)", max_length=16)
    tours_count = models.IntegerField("Количество туров в городе", default=0)
    orders_count = models.IntegerField("Количество заказов в городе", default=0)
    image_city = models.ImageField("Изображение")


class Category(models.Model):
    title = models.CharField("Название категории", max_length=32)
    description = RichTextField("Описание категории")
    seo_title = models.CharField("Заговок страницы (SEO)", max_length=64)
    seo_description = models.CharField("Заголовок страницы (SEO)", max_length=128)
    important = models.BooleanField("Показывать в числе первых")
    slug = models.SlugField("Slug (название в URL)", max_length=16)


class Offer(models.Model):
    COLOR_CHOICES = (
        ("#4dc05e", "Зелёный"),
        ("#ec4159", "Красный")
    )

    text = models.CharField("Текст предложения", max_length=32)
    color = models.CharField("Цвет", max_length=7, choices=COLOR_CHOICES)


class Tour(models.Model):
    GROUP_CHOICES = (
        (True, "Групповая"),
        (False, "Одиночная")
    )
    city = models.ForeignKey(City, on_delete=models.PROTECT, blank=True, default=1)

    title = models.CharField("Название страницы", max_length=64)
    slug = models.SlugField("Slug (название в URL)", max_length=16)

    description = RichTextField("Описание категории")
    include = RichTextField("Описание категории")

    seo_title = models.CharField("Заговок страницы (SEO)", max_length=64)
    seo_description = models.CharField("Заголовок страницы (SEO)", max_length=128)
    seat_request = models.BooleanField("Показывать блок 'Запросить места'", default=True)
    count_comment = models.SmallIntegerField('Количество отзывов', default=0)
    rating = models.FloatField("Рейтинг", validators=[MinValueValidator(0), MaxValueValidator(5)], default=5)
    price = models.PositiveIntegerField("Цена (для главной)")
    group = models.BooleanField("Тип", choices=GROUP_CHOICES)
    time = models.TimeField("Продолжительность экскурсии")
    image = models.ImageField("Основная фотография")
    offer = models.ForeignKey(Offer, on_delete=models.PROTECT, null=True, default=True)
    categories = models.ManyToManyField(Category)
    positions = models.ManyToManyField(Position)


class Comment(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.PROTECT)
    name = models.CharField("Имя пользователя", max_length=32)
    content = models.TextField("Текст комментария")
    date = models.DateField("Дата", auto_now=True)
    grade = models.SmallIntegerField("Рейтинг", validators=[MinValueValidator(0), MaxValueValidator(5)], default=5)


class ImageItem(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.PROTECT)
    image = models.ImageField("Основная фотография")
    description = models.TextField("Описание фотографии", max_length=128)


class RecommendedTour(models.Model):
    main = models.ForeignKey(Tour, related_name="tour_main", on_delete=models.PROTECT)
    add = models.ForeignKey(Tour, related_name="tour_add", on_delete=models.PROTECT)
