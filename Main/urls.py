from django.urls import path
from Main.views import MainClassView,SubscriberCreateView,CitySinglePage

urlpatterns = [
    path('',MainClassView.as_view(),name='home'),
    path('subscribe/',SubscriberCreateView.as_view(),name='subscribe'),
    path('city-single-page/',CitySinglePage.as_view(),name='city_single_page')
]