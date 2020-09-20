from django.urls import path
from Restaurants.views import RestaurantsListView, RestaurantsSinglePageClassView 

app_name = 'restaurants_app'

urlpatterns = [
    path('',RestaurantsListView.as_view(),name='restaurants'),
    path('single-page/<slug:slug>/',RestaurantsSinglePageClassView.as_view(),name='restaurant_single_page'),

]