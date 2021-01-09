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
    site_name = 0
    number_phone = 0
    user_agreement = 0
    help_title = 0  # помощь в выборе заголовок
    help_text = 0  # помощь в выборе текст
    map_title = 0  # найти экскурсии на карте
    map_text = 0  # покажем, что есть в шаговой доступности


class SocialNetwork(models.Model):
    icon = 0
    name = 0
    link = 0


