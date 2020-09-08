from django.shortcuts import render
from django.views.generic import ListView,CreateView,TemplateView
from Hotels.models import Hotel
# Create your views here.


class HotelsListView(ListView):
    model = Hotel
    template_name = 'hotels.html'
    paginate_by = 6
    context_object_name = 'hotels'

class HotelsSinglePage(TemplateView):
    template_name = 'single_page.html'