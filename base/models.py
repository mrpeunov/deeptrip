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
    site_name = models.CharField("Название сайта", max_length=32)
    seo_title = models.CharField("Заговок страницы (SEO)", max_length=64)
    number_phone = models.CharField("Номер телефона", max_length=10)
    user_agreement = models.TextField('Пользовательноское соглашение')
    help_title = models.CharField("'Помощь в выборе' заголовок", max_length=32)
    help_text = models.TextField("'Помощь в выборе' текст")
    map_title = models.CharField("'Экскурсии на карте' заголовок", max_length=32)
    map_text = models.TextField("'Экскурсии на карте' текст")


class SocialNetwork(models.Model):
    icon = models.ImageField("Иконка")
    name = models.CharField("Название")
    link = models.URLField("Ссылка")


