from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import TextField
from django.urls import reverse
from base.models import City


class Category(models.Model):
    city = models.ForeignKey(City, on_delete=models.PROTECT, blank=True, default=1)
    title = models.CharField("Название категории", max_length=32)
    description = RichTextField("Описание категории")
    seo_title = models.CharField("Заговок страницы (SEO)", max_length=64)
    seo_description = models.CharField("Описание страницы (SEO)", max_length=128)
    important = models.BooleanField("Показывать в числе первых")
    slug = models.SlugField("Slug (название в URL)", max_length=16, unique=True)

    def __str__(self):
        return "Категория '{}'".format(self.title)

    def get_absolute_url(self):
        return reverse('tour_page', args=[str(self.city.slug), str(self.slug)])

    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "категории"


class Position(models.Model):
    name = models.CharField("Название позиции", max_length=32)
    lat = models.FloatField("Широта")
    lon = models.FloatField("Долгота")

    def __str__(self):
        return "Точка '{}'".format(self.name)

    class Meta:
        verbose_name = "точка на карте"
        verbose_name_plural = "точки на карте"


class Offer(models.Model):
    COLOR_CHOICES = (
        ("#4dc05e", "Зелёный"),
        ("#ec4159", "Красный")
    )

    text = models.CharField("Текст предложения", max_length=32)
    color = models.CharField("Цвет", max_length=7, choices=COLOR_CHOICES)

    def __str__(self):
        return "Специальное предложение '{}'".format(self.text)

    class Meta:
        verbose_name = "специальное предложение"
        verbose_name_plural = "специальные предложение"


class Town(models.Model):
    city = models.ForeignKey(City, on_delete=models.PROTECT, blank=True, default=1)
    name = models.CharField("Название", max_length=64)
    description = TextField("Описание")
    seo_title = models.CharField("Заговок страницы (SEO)", max_length=64)
    h1 = models.CharField("Заговок h1", max_length=64)
    h2 = models.CharField("Заговок h2", max_length=64)
    image = models.ImageField(null=True)

    def __str__(self):
        return "Район '{}'".format(self.name)

    class Meta:
        verbose_name = "район"
        verbose_name_plural = "районы"


class Tour(models.Model):
    GROUP_CHOICES = (
        (True, "Групповая"),
        (False, "Одиночная")
    )
    city = models.ForeignKey(City, on_delete=models.PROTECT, blank=True, default=1)

    title = models.CharField("Название экскурсии", max_length=64)
    slug = models.SlugField("Slug (название в URL)", max_length=64, unique=True)

    seo_title = models.CharField("Заговок страницы (SEO)", max_length=64)
    seo_description = models.CharField("Описание страницы (SEO)", max_length=128)

    description = TextField("Описание экскурсии")
    include = RichTextField("Включено")

    seat_request = models.BooleanField("Показывать блок 'Запросить места'", default=True)
    count_comment = models.SmallIntegerField('Количество отзывов', default=0)
    rating = models.FloatField("Рейтинг", validators=[MinValueValidator(0), MaxValueValidator(5)], default=5)
    price = models.PositiveIntegerField("Цена (для главной)")
    group = models.BooleanField("Тип", choices=GROUP_CHOICES)
    time = models.CharField("Продолжительность экскурсии", max_length=32)
    image = models.ImageField("Основная фотография")
    offer = models.ForeignKey(Offer, on_delete=models.PROTECT, blank=True)
    towns = models.ManyToManyField(Town, verbose_name="Районы")
    categories = models.ManyToManyField(Category, verbose_name="Категории")
    positions = models.ManyToManyField(Position, verbose_name="Точки на карте")
    notes = models.CharField("Примечания", max_length=64, default="Пусто")

    def __str__(self):
        return "Экскурсия '{}'".format(self.title)

    def get_absolute_url(self):
        return reverse('tour_page', args=[str(self.city.slug), str(self.slug)])

    class Meta:
        verbose_name = "экскурсию"
        verbose_name_plural = "экскурсии"


class Like(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.PROTECT)
    session_id = models.CharField(max_length=256)


class Comment(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.PROTECT)
    name = models.CharField("Имя пользователя", max_length=32)
    content = models.TextField("Текст комментария")
    date = models.DateField("Дата", auto_now=True)
    grade = models.SmallIntegerField("Рейтинг", validators=[MinValueValidator(0), MaxValueValidator(5)], default=5)
    show = models.BooleanField("Отображать", default=True)

    def __str__(self):
        return "Отзыв от '{}'".format(self.name)

    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = "отзывы"


class ImageItem(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.PROTECT)
    image = models.ImageField("Дополнительная фотография")
    description = models.CharField("Описание фотографии", max_length=128)

    def __str__(self):
        return "Дополнительная фотография к туру {} № {}".format(self.tour, self.id)

    class Meta:
        verbose_name = "дополнительная фотография"
        verbose_name_plural = "дополнительные фотографии"


class RecommendedTour(models.Model):
    main = models.ForeignKey(Tour, verbose_name="Основная экскурсия", related_name="tour_main",
                             on_delete=models.PROTECT)
    add = models.ForeignKey(Tour, verbose_name="Рекомендованная экскурсия", related_name="tour_add",
                            on_delete=models.PROTECT)

    def __str__(self):
        return "Рекомендованная экскурсия {} {}".format(self.main, self.add)

    class Meta:
        verbose_name = "Рекомендованная экскурсия"
        verbose_name_plural = "Рекомендованные экскурсии"
