from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from Restaurants.models import Restaurants, OptionsTypeRadio, OptionsTypeCheckbox, RestaurantImages, ToEatReason

class RestaurantsListView(ListView):
    model = Restaurants
    template_name = 'restaurants.html'
    paginate_by = 1

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data( *args, **kwargs)
        context['type_radio'] = OptionsTypeRadio.objects.all()
        context['type_checkbox'] = OptionsTypeCheckbox.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)

class RestaurantsSinglePageClassView(DetailView):
    model = Restaurants
    template_name = 'restaurant_single_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data( *args, **kwargs)
        return context



