from django.shortcuts import render
from django.views.generic import ListView,CreateView,TemplateView
# Create your views here.


class HotelsListView(TemplateView):
    template_name = 'hotels.html'


class HotelsSinglePage(TemplateView):
    template_name = 'single_page.html'