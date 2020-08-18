from django.urls import path
from Restaurants.views import RestaurantsClassView

urlpatterns = [
    path('restaurants/',RestaurantsClassView.as_view(),name='restaurants'),
]