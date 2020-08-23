from django.urls import path
from Places.views import  PlacesClassView

urlpatterns = [
    path('places/',PlacesClassView.as_view(),name='places')
]