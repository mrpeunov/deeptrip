from django.urls import path
from tours.views import get_more_tours

urlpatterns = [
    path('api/v1/get_more_tours/', get_more_tours, name="city_page"),
]