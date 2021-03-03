from typing import List

from articles.models import Article
from tours.models import City


def get_articles(city: City) -> List[Article]:
    result = list(Article.objects.all())
    return result
