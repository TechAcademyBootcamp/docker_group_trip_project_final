from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from Tours.models import Tours

# Create your views here.

class ToursPage(TemplateView):
    model = Tours
    template_name = 'tourspage.html'
    def get_context_data(self,*args , **kwargs):
        context = super().get_context_data(**kwargs)
        context["tours"] = Tours.objects.all
        return context
    


class ToursSinglePage(TemplateView):
    template_name = 'tours_single_page.html'


