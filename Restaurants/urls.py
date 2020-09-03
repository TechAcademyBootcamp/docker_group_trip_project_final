from django.urls import path
from Restaurants.views import RestaurantsClassView , RestaurantsSinglePageClassView 

app_name = 'restaurants_app'

urlpatterns = [
    path('restaurants/',RestaurantsClassView.as_view(),name='restaurants'),
    path('single-page/',RestaurantsSinglePageClassView.as_view(),name='restaurant_single_page'),

]