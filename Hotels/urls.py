from django.urls import path
from Hotels.views import HotelsListView,HotelsSinglePage,PaymentPage

app_name = 'hotels_app'


urlpatterns = [
    path('hotels/',HotelsListView.as_view(),name='hotels'),
    path('hotels-single/<slug:slug>/',HotelsSinglePage.as_view(),name='hotels-single'),
    path('payment/',PaymentPage.as_view(),name='hotels-payment')
]