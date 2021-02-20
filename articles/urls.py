from django.urls import path
from .views import *

urlpatterns = [
    path('', MagazinePage.as_view(), name="magazine_page"),
]