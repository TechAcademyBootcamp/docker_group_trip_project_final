from django.urls import path
from Tours.views import ToursPage

urlpatterns = [
    path('tours-page/',ToursPage.as_view(),name='tourspage'),  
]