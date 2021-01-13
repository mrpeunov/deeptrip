from django.urls import path

from .views import *

urlpatterns = [
    path('', CityPage.as_view(), name="city_page"),
    path('tours/', ToursFilterPage.as_view(), name="tours_filter_page"),
    # path('tours/<str:tour_slug>', views.tour_page, name="tour_page"),
    # path('categories/', views.categories_page, name="categories_page"),
    # path('categories/<str:category_slug>/', views.category_page, name="category_page"),
    # path('maps/', views.maps_page, name="maps_page")
]
