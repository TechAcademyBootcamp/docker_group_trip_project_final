from django.urls import path
from Hotels.views import HotelsListView,HotelsSinglePage

app_name = 'hotels_app'


urlpatterns = [
    path('hotels/',HotelsListView.as_view(),name='hotels'),
    path('hotels-single/',HotelsSinglePage.as_view(),name='hotels-single'),
]