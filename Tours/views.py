from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

# Create your views here.

class ToursPage(TemplateView):
    template_name = 'tourspage.html'


