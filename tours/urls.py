from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<slug:city_slug>/', CityPage.as_view(), name="city_page"),
    path('<slug:city_slug>/filter/', FilterPage.as_view(), name="filter_page"),
    path('<slug:city_slug>/map/', MapPage.as_view(), name="filter_page"),
    path('<slug:city_slug>/<slug:tour_slug>', TourPage.as_view(), name="tour_page"),
]
