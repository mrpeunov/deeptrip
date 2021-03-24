from django.db.models.signals import m2m_changed, pre_delete, post_delete
from django.dispatch import receiver
from tours.models import Tour, Comment


@receiver(m2m_changed, sender=Tour.cities.through)
def tour_cities_changed(sender, **kwargs):
    """обновляет количество экускурсий в городах при обновлении экскурсии"""
    action = kwargs["action"]

    if action == "post_add":
        for city in kwargs["instance"].cities.all():
            city.update_tours_count()

    if action == "pre_remove":
        kwargs["instance"].pre_remove_cities = list(kwargs["instance"].cities.all())

    if action == "post_remove":
        for city in kwargs["instance"].pre_remove_cities:
            city.update_tours_count()


@receiver(post_delete, sender=Comment)
def comment_delete(sender, instance, **kwargs):
    """в случае удаление комментария обновляет рейтинг экскурсии"""
    instance.update_count_and_rating_tour()
