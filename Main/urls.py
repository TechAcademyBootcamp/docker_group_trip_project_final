from django.urls import path
from Main.views import MainClassView,SubscriberCreateView,ContactSubjectView,ContactPageView

app_name = 'main'

urlpatterns = [
    path('',MainClassView.as_view(),name='home'),
    path('subscribe/',SubscriberCreateView.as_view(),name='subscribe'),
    path('contact/',ContactPageView.as_view(),name='contact'),
    path('contact-form/',ContactSubjectView.as_view(),name='contact-from')
]