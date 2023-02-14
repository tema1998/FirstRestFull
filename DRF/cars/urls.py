from django.contrib import admin
from django.urls import path, include

from cars.views import CarCreateView, CarsListView, CarDetailView, Carss


urlpatterns = [
    path('car/create/', CarCreateView.as_view(), name='create'),
    path('all/', CarsListView.as_view(), name='all_cars'),
    path('car/detail/<int:pk>/', CarDetailView.as_view(), name='detail'),
]