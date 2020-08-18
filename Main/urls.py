from django.urls import path
from Main.views import MainClassView,SubscriberCreateView

urlpatterns = [
    path('',MainClassView.as_view(),name='home'),
    path('subscribe/',SubscriberCreateView.as_view(),name='subscribe')
]