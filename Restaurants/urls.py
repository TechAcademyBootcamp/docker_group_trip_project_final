from django.urls import path
from Restaurants.views import RestaurantsClassView , RestaurantsSinglePageClassView 

urlpatterns = [
    path('restaurants/',RestaurantsClassView.as_view(),name='restaurants'),
    path('single_page/',RestaurantsSinglePageClassView.as_view(),name='restaurant_single_page'),

]