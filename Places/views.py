from django.shortcuts import render
from django.views.generic import TemplateView

class PlacesClassView(TemplateView):
    template_name = 'where_to_go.html'
