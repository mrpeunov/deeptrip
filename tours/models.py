from django_better_admin_arrayfield.models.fields import ArrayField
from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg
from django.urls import reverse
from smart_selects.db_fields import ChainedManyToManyField, ChainedForeignKey


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
            if (self != item.city) & (self in item.cities.all()):
                more_count += 1

        self.tours_count = main_count + more_count
        self.save()

    def get_tours_count_str(self) -> str:
        count = self.tours_count

        if (count % 10 == 1) and count != 11:
            return "{} экскурсия".format(count)

        if 2 <= count % 10 <= 4 and count not in (12, 13, 14):
            return "{} экскурсии".format(count)

        if 5 <= count % 10 or \
                count % 10 in (0, 1) or \
                count in (12, 13, 14):
            return "{} экскурсий".format(count)

    class Meta:
        verbose_name = "город"
        verbose_name_plural = "города"


class Category(models.Model):
    title = models.CharField("Название категории", max_length=32)
    description = RichTextField("Описание категории")
    seo_title = models.CharField("Заговок страницы (SEO)", max_length=64)
    seo_description = models.CharField("Описание страницы (SEO)", max_length=128)
    important = models.BooleanField("Показывать в числе первых")  # нужно ли?
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


class Period(models.Model):
    title = models.CharField("Название периода", max_length=32)
    january = models.BooleanField("Январь")
    february = models.BooleanField("Февраль")
    march = models.BooleanField("Март")
    april = models.BooleanField("Апрель")
    may = models.BooleanField("Май")
    june = models.BooleanField("Июнь")
    july = models.BooleanField("Июль")
    august = models.BooleanField("Август")
    september = models.BooleanField("Сентябрь")
    october = models.BooleanField("Октябрь")
    november = models.BooleanField("Ноябрь")
    december = models.BooleanField("Декабрь")

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name = "период работы"
        verbose_name_plural = "периоды работы"


class Tour(models.Model):
    GROUP_CHOICES = (
        (True, "Групповая"),
        (False, "Одиночная")
    )

    TRANSFER_CHOICES = (
        ("y", "Есть"),
        ("n", "Нет"),
        ("yn", "Есть + Нет")
    )

    title = models.CharField("Название экскурсии", max_length=64)
    slug = models.SlugField("Slug (название в URL)", max_length=64, unique=True)

    cluster = models.ForeignKey(Cluster,
                                verbose_name="Кластер",
                                on_delete=models.PROTECT)

    city = ChainedForeignKey(City,
                             verbose_name="Основной город",
                             chained_field="cluster",
                             chained_model_field="cluster",
                             on_delete=models.PROTECT,
                             related_name="main_city")

    cities = ChainedManyToManyField(City,
                                    blank=True,
                                    horizontal=True,
                                    verbose_name="Дополнительные города",
                                    related_name="add_cities",
                                    chained_field="cluster",
                                    chained_model_field="cluster")

    seo_title = models.CharField("Заговок страницы (SEO)", max_length=64)
    seo_description = models.CharField("Описание страницы (SEO)", max_length=128)

    description_mini = models.TextField("Описание экскурсии (мини)")
    description = models.TextField("Описание экскурсии (полное)")

    include_list = ArrayField(
        models.CharField(max_length=30, blank=True),
        verbose_name="Включено",
        size=6,
        blank=True)

    add_price_list = ArrayField(
        models.CharField(max_length=30, blank=True),
        verbose_name="За дополнительную плату",
        size=6,
        blank=True)

    start_list = ArrayField(
        models.TimeField(),
        verbose_name="Начало",
        size=4,
        blank=True, null=True)

    price = models.PositiveIntegerField("Цена")
    image = models.ImageField("Основная фотография")
    groups = models.BooleanField("Тип", choices=GROUP_CHOICES)
    time = models.CharField("Продолжительность экскурсии", max_length=32)

    seat_request = models.BooleanField("Показывать блок 'Запросить места'", default=True)
    count_comment = models.SmallIntegerField('Количество отзывов', default=0)
    rating = models.FloatField("Рейтинг", validators=[MinValueValidator(0), MaxValueValidator(5)], default=5)

    offer = models.CharField("Специальное предложение", max_length=20, blank=True)

    categories = models.ManyToManyField(Category, blank=True, verbose_name="Категории")

    notes = models.CharField("Примечания", blank=True, max_length=64)

    gid = models.BooleanField("Проверенный гид", default=False)
    auto_gid = models.BooleanField("Автоматизировать провернный гид", default=True)
    video = models.URLField("Ссылка на видео", blank=True)

    transfer = models.CharField("Трансфер", max_length=2, choices=TRANSFER_CHOICES, default="yn")
    positions = models.ManyToManyField(Position, blank=True, related_name="positions",
                                       verbose_name="Местоположение экскурсии")
    transfer_no_first = models.CharField("1 строка (Трансфера нет или  не нужен)", max_length=64)
    transfer_no_second = models.CharField("2 строка (Трансфера нет или он не нужен)", max_length=64)

    transfer_points = models.ManyToManyField(Position, blank=True, related_name="transfer_points",
                                             verbose_name="Точки трансфера")
    transfer_yes_first = models.CharField("1 строка (Трансфер есть)", max_length=64)
    transfer_yes_second = models.CharField("2 строка (Трансфер есть)", max_length=64)

    period = models.ForeignKey(Period, verbose_name="Период года", on_delete=models.PROTECT)

    def __str__(self):
        return "Экскурсия '{}'".format(self.title)

    class Meta:
        verbose_name = "экскурсию"
        verbose_name_plural = "экскурсии"

    def get_absolute_url(self):
        return reverse('tour_page', args=[str(self.city.slug), str(self.slug)])

    def save(self, *args, **kwargs):
        self.city.update_tours_count()
        if self.auto_gid is True:
            if self.count_comment > 3 and self.rating > 4:
                self.gid = True

        super().save(*args, **kwargs)

    def get_rating_for_city(self, city: City) -> int:
        """
        :param city: город для которого вычисляется рейтинг
        :return: рейтинг города от 0(25) до 100
        """
        city_rating = 0

        # 20% влияния рейтинга
        city_rating += int(self.rating / 5 * 20)

        # 20% влияния количества комментариев
        if self.count_comment > 9:
            city_rating += int((self.count_comment + 1) / 10 * 20)
        else:
            city_rating += 20

        # 10% влияния специального предложения
        if self.offer:
            city_rating += 10

        # 50% влияния местоположения
        if self.city == city:
            city_rating += 50
        elif city in self.cities.all():
            city_rating += 25
        else:
            city_rating = 0
            print("Ошибка, рейтинг для этого города обнулён, так как данная экскурсия в нем отсутствует")

        return city_rating


class Advantage(models.Model):
    TRANSFER_CHOICES = (
        ("children", "Дети"),
        ("time", "Время"),
        ("transfer", "Трансфер"),
        ("group", "Группа"),
        ("prepay", "Предоплата"),
    )

    tour = models.ForeignKey(Tour, verbose_name="Экскурсия", on_delete=models.PROTECT)
    type = models.CharField("Тип", max_length=10, choices=TRANSFER_CHOICES)
    title = models.CharField("Заголовок", max_length=32, blank=True)
    description = models.CharField("Описание", max_length=64, blank=True)


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

    def save(self, *args, **kwargs):
        print("сюда заходем")
        super().save(*args, **kwargs)
        self.update_count_and_rating_tour()

    def update_count_and_rating_tour(self):
        tour = self.tour  # получаем текущую экскурсию

        # получаем данные о рейтинге и количестве
        comments = Comment.objects.filter(tour=tour, show=True)
        count_comments = comments.count()
        tour_rating = comments.aggregate(Avg('grade'))

        # обновляем данные в объекте экскурсии
        tour.count_comment = count_comments
        if tour_rating['grade__avg'] is None:
            tour.rating = 5
        else:
            tour.rating = round(tour_rating['grade__avg'], 2)
        tour.save()


class ImageItem(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.PROTECT)
    image = models.ImageField("Дополнительная фотография")
    description = models.CharField("Описание фотографии", max_length=128)

    def __str__(self):
        return "Дополнительная фотография к туру {} № {}".format(self.tour, self.id)

    class Meta:
        verbose_name = "дополнительная фотография"
        verbose_name_plural = "дополнительные фотографии"


class Question(models.Model):
    name = models.CharField("Имя", max_length=64)
    text = models.TextField("Текст вопроса")
    tour = models.ForeignKey(Tour, on_delete=models.PROTECT, null=True)
    email = models.EmailField("E-mail", blank=True)
    phone = models.TextField("Телефон", blank=True, max_length=15)
    answer = models.BooleanField("Обработано", default=False)
    date = models.DateTimeField("Дата", auto_now_add=True)
    note = models.TextField("Примечание", blank=True)

    def __str__(self):
        return "Вопрос от {}".format(self.name)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Variable(models.Model):
    TYPE_LIST = [('r', 'Тариф'),
                 ('g', 'Группа'),
                 ('c', 'Дети')]

    name = models.CharField("Название переменной", max_length=32, blank=True)
    tour = models.ForeignKey(Tour, on_delete=models.PROTECT, blank=True)
    type = models.CharField("Тип", max_length=1, choices=TYPE_LIST, blank=True)

    def __str__(self):
        return "Переменная для экскурсии {} - {}".format(self.tour, self.name)

    class Meta:
        verbose_name = "Переменная"
        verbose_name_plural = "Переменные для тарифов"


class Rate(models.Model):
    name = models.CharField("Название", max_length=32, blank=True)
    price = models.FloatField("Цена/Множитель", blank=True)
    variable = models.ForeignKey(Variable, on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return "Вариант для переменной {}".format(self.variable)

    class Meta:
        verbose_name = "Вариант переменной"
        verbose_name_plural = "Варианты переменной"
