from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

# Create your views here.

class ToursPage(TemplateView):
    template_name = 'tourspage.html'


class ToursSinglePage(TemplateView):
    template_name = 'tours_single_page.html'


