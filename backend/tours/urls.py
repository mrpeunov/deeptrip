from django.urls import path
from rest_framework import routers

from .views import *

urlpatterns = [
    #path('', CityPage.as_view(), name="city_page"),
    path('tours/', ToursFilterPage.as_view(), name="tours_filter_page"),
    # path('tours/<slug:tour_slug>', TourPage.as_view(), name="tour_page"),
    # path('categories/', views.categories_page, name="categories_page"),
    # path('categories/<str:category_slug>/', views.category_page, name="category_page"),
    # path('maps/', views.maps_page, name="maps_page")
]

router = routers.DefaultRouter()
router.register(r'notes', ToursApiView)
urlpatterns += router.urls