from django.urls import path

from . import views

urlpatterns = [
    path('<str:city>/tours/', views.tours_filter_page),
    path('<str:city>/tours/<str:slug>', views.tour_page)
]