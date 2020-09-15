from django.urls import path
from Hotels.views import HotelsListView,HotelsSinglePage,ReservePage

app_name = 'hotels_app'


urlpatterns = [
    path('hotels/',HotelsListView.as_view(),name='hotels'),
    path('hotels-single/<slug:slug>/',HotelsSinglePage.as_view(),name='hotels-single'),
    path('hotels-reserve/<int:pk>/',ReservePage.as_view(),name='hotels-reserve'),
    # path('payment/',PaymentPage.as_view(),name='hotels-payment')
]