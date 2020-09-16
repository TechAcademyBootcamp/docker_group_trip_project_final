from django.urls import path
from Tours.views import ToursPage,ToursSinglePage

app_name = 'tours'

urlpatterns = [
    path('',ToursPage.as_view(),name ='tours-list'),  
    path('<slug:slug>/',ToursSinglePage.as_view(),name ='tour-detail'),  
]