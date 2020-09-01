from django.urls import path
from Places.views import  PlacesClassView,PlacesSinglePageClassView

urlpatterns = [
    path('places/',PlacesClassView.as_view(),name='places'),
    path('single-page/',PlacesSinglePageClassView.as_view(),name='place_single_page'),
]