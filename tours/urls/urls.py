from django.urls import path

from tours.views import *

urlpatterns = [
    path('', CityPage.as_view(), name="city_page"),
    path('filter/', FilterPage.as_view(), name="filter_page"),
    path('map/', MapPage.as_view(), name="filter_page"),
    path('<slug:tour_slug>', TourPage.as_view(), name="tour_page"),
    path('<slug:tour_slug>/comment/', send_new_comment, name="send_new_comment"),
]
