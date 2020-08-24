from django.urls import path
from Tours.views import ToursPage,ToursSinglePage

urlpatterns = [
    path('tours-page/',ToursPage.as_view(),name='tourspage'),  
    path('tours-single-page/',ToursSinglePage.as_view(),name='tours_single_page'),  

]