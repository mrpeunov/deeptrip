from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import TextField, Q, QuerySet
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.urls import reverse


class Cluster(models.Model):
    name = models.CharField("Название кластера", max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Кластер"
        verbose_name_plural = "Кластеры"


class City(models.Model):
    cluster = models.ForeignKey(Cluster, on_delete=models.PROTECT, null=True)
    name = models.CharField("Название города", max_length=32)
    h1 = models.CharField("Заголовок h1", max_length=32)
    h2 = models.CharField("Заголовок h2", max_length=32)
    seo_title = models.CharField("Заговок страницы (SEO)", max_length=64)
    seo_description = models.CharField("Описание страницы (SEO)", max_length=128)
    slug = models.SlugField("Slug (название в URL)", max_length=16, unique=True)
    tours_count = models.IntegerField("Количество экскурсий в городе", default=0)
    orders_count = models.IntegerField("Количество заказов в городе", default=0)
    importance = models.PositiveIntegerField("Важность города", default=0)
    image = models.ImageField("Изображение")

    def get_absolute_url(self):
        return reverse('city_page', args=[str(self.slug)])

    def __str__(self):
        return "Город '{}'".format(self.name)

    def update_tours_count(self):
        """обновление количества экскурсий"""
        main_count = Tour.objects.filter(city=self).count()

        more_count = 0
        for item in Tour.objects.all():
            if self in item.cities.all():
                more_count += 1

        self.tours_count = main_count + more_count
        self.save()

    class Meta:
        verbose_name = "город"
        verbose_name_plural = "города"


class Category(models.Model):
    city = models.ForeignKey(City, on_delete=models.PROTECT, blank=True, null=True)
    title = models.CharField("Название категории", max_length=32)
    description = RichTextField("Описание категории")
    seo_title = models.CharField("Заговок страницы (SEO)", max_length=64)
    seo_description = models.CharField("Описание страницы (SEO)", max_length=128)
    important = models.BooleanField("Показывать в числе первых")
    slug = models.SlugField("Slug (название в URL)", max_length=16, unique=True)

    def __str__(self):
        return "Категория '{}'".format(self.title)

    def get_absolute_url(self):
        return reverse('tour_page', args=[str(self.slug), str(self.slug)])

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


class Tour(models.Model):
    GROUP_CHOICES = (
        (True, "Групповая"),
        (False, "Одиночная")
    )
    city = models.ForeignKey(City, on_delete=models.PROTECT, blank=True, default=1, related_name="main_city")
    cities = models.ManyToManyField(City, verbose_name="Дополнительные", related_name="add_cities")

    title = models.CharField("Название экскурсии", max_length=64)
    slug = models.SlugField("Slug (название в URL)", max_length=64, unique=True)

    seo_title = models.CharField("Заговок страницы (SEO)", max_length=64)
    seo_description = models.CharField("Описание страницы (SEO)", max_length=128)

    description = TextField("Описание экскурсии")
    include = RichTextField("Включено")
    price = models.PositiveIntegerField("Цена")
    image = models.ImageField("Основная фотография")
    group = models.BooleanField("Тип", choices=GROUP_CHOICES)
    time = models.CharField("Продолжительность экскурсии", max_length=32)

    seat_request = models.BooleanField("Показывать блок 'Запросить места'", default=True)
    count_comment = models.SmallIntegerField('Количество отзывов', default=0)
    rating = models.FloatField("Рейтинг", validators=[MinValueValidator(0), MaxValueValidator(5)], default=5)

    offer = models.ForeignKey(Offer, on_delete=models.PROTECT, blank=True, null=True)

    categories = models.ManyToManyField(Category, verbose_name="Категории")
    positions = models.ManyToManyField(Position, verbose_name="Точки на карте")
    notes = models.CharField("Примечания", max_length=64, default="Пусто")

    def __str__(self):
        return "Экскурсия '{}'".format(self.title)

    class Meta:
        verbose_name = "экскурсию"
        verbose_name_plural = "экскурсии"

    def get_absolute_url(self):
        return reverse('tour_page', args=[str(self.city.slug), str(self.slug)])

    def save(self, *args, **kwargs):
        self.city.update_tours_count()


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
