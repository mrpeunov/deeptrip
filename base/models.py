from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()


class Config(SingletonModel):
    site_name = models.CharField("Заголовок сайта", max_length=32)
    site_description = models.CharField("Подзагловок", max_length=32)
    seo_title = models.CharField("Заговок страницы (SEO)", max_length=64)
    number_phone = models.CharField("Номер телефона", max_length=10)
    user_agreement = models.TextField('Пользовательноское соглашение')

    def __str__(self):
        return "Конфиг"

    class Meta:
        verbose_name = "Конфиг"
        verbose_name_plural = "Конфиг"


class SocialNetwork(models.Model):
    icon = models.ImageField("Иконка")
    name = models.CharField("Название", max_length=16)
    link = models.URLField("Ссылка")

    def __str__(self):
        return "Социальная сеть {}".format(self.name)

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"


