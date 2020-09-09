from django.urls import path
from Hotels.api.views import HotelListView

app_name = 'api_hotel'

urlpatterns = [
    path('',HotelListView.as_view(),name='hotel')
]