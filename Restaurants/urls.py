from django.urls import path
from Restaurants.views import RestaurantsListView, RestaurantsSinglePageClassView , ReviewCreateView, SavedRestaurantView, SavedRestaurantListView,SavedRestaurantView

app_name = 'restaurants_app'

urlpatterns = [
    path('',RestaurantsListView.as_view(),name='restaurants'),
    path('review/',ReviewCreateView.as_view(),name='restaurants_review'),
    path('single-page/<slug:slug>/',RestaurantsSinglePageClassView.as_view(),name='restaurant_single_page'),
    path('save-tour/<int:pk>/',SavedRestaurantView.as_view(),name ='save_wishlist'),
    path('saved-tour/',SavedRestaurantListView.as_view(),name ='saved_wishlist'),

]