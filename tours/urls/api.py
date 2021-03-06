from django.urls import path
from tours import views

urlpatterns = [
    path('api/v1/get_more_tours/', views.get_more_tours, name="city_page"),
    path('api/v1/get_count_tours_for_filter_list/', views.get_count_tours_for_filter_list, name="city_page"),
    path('api/v1/get_more_comments/', views.get_more_comments, name="get_more_comments"),
    path('api/v1/get_more_recommended/', views.get_more_recommended, name="get_more_recommended")
]