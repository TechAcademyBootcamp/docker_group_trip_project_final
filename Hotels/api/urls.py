from django.urls import path
from Hotels.api.views import HotelListView,PhoneNumber

app_name = 'api_hotel'

urlpatterns = [
    path('',HotelListView.as_view(),name='hotel'),
    path('number',PhoneNumber.as_view(),name='number')
]