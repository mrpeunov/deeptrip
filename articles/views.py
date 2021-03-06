from django.shortcuts import render

# Create your views here.
from articles.models import Article
from base.services import FooterAndMenuTemplateView


class MagazinePage(FooterAndMenuTemplateView):
    """
    Страница журнала
    """
    template_name = 'magazine/magazine.html'

    def add_in_context(self, context):
        context['articles'] = Article.objects.all()
        context['not_empty'] = True
        context['title'] = "Туристический журнал"


class ArticlePage(FooterAndMenuTemplateView):
    """
    Страница журнала
    """
    template_name = 'article/article.html'

    def add_in_context(self, context):
        pass
