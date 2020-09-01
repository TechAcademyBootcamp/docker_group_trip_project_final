from django.shortcuts import render
from django.views.generic import TemplateView

class RestaurantsClassView(TemplateView):
    template_name = 'restaurants.html'

class RestaurantsSinglePageClassView(TemplateView):
    template_name = 'restaurant_single_page.html'



