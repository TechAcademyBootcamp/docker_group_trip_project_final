from django.urls import path
from Tours.views import ToursPage,ToursSinglePage

app_name = 'tours'

urlpatterns = [
    path('page/',ToursPage.as_view(),name ='tourspage'),  
    path('single-page/',ToursSinglePage.as_view(),name ='tours_single_page'),  

]