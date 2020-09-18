from django.urls import path
from Hotels.views import HotelsListView,HotelsSinglePage,ReservePage,ReviewSendView

app_name = 'hotels_app'


urlpatterns = [
    path('hotels/',HotelsListView.as_view(),name='hotels'),
    path('hotels-single/<slug:slug>/',HotelsSinglePage.as_view(),name='hotels-single'),
    path('hotels-reserve/<int:pk>/',ReservePage.as_view(),name='hotels-reserve'),
    path('hotels-reviews/',ReviewSendView.as_view(),name='hotels-reviews')
]