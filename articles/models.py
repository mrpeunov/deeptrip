from django.db import models
from tours.models import Tour


class Article(models.Model):
    date
    view_count = 0