from django.shortcuts import render
from django.views.generic import ListView,CreateView,TemplateView
from Hotels.models import Hotel,HotelAmenities,PoliciesSubFeatures
from django.urls import reverse_lazy
from django.contrib.sites.models import Site
from django.conf import settings


class HotelsListView(ListView):
    model = Hotel
    template_name = 'hotels.html'
    paginate_by = 6
    context_object_name = 'hotels'

    def get_context_data(self, **kwargs):
        context = super(HotelsListView, self).get_context_data(**kwargs)
        hotel_amenities = HotelAmenities.objects.all()
        context['hotel_amenities'] = hotel_amenities
        PoliciesSub = PoliciesSubFeatures.objects.all()
        context['PoliciesSub'] = PoliciesSub
        current_site = Site.objects.last()
        context['url'] = f"{self.request.get_host()}{reverse_lazy('api_hotel:hotel')}"
        return context



class HotelsSinglePage(TemplateView):
    template_name = 'single_page.html'

#