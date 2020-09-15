from django.shortcuts import render, redirect
from django.views.generic import ListView,CreateView,DetailView,TemplateView
from Hotels.models import Hotel,HotelAmenities,PoliciesSubFeatures,RoomAmenities,Reservation,RoomType,Policies,Reviews
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from django.contrib.sites.models import Site
from django.conf import settings
import stripe
from django.contrib import messages

stripe.api_key = settings.STRIPE_SECRET_KEY

class HotelsListView(ListView):
    model = Hotel
    template_name = 'hotels.html'
    paginate_by = 6
    context_object_name = 'hotels'

    def get_context_data(self, **kwargs):
        context = super(HotelsListView, self).get_context_data(**kwargs)
        hotel_amenities = HotelAmenities.objects.all()
        room_amenities= RoomAmenities.objects.all()
        context['room_amenities']=room_amenities
        context['hotel_amenities'] = hotel_amenities
        PoliciesSub = PoliciesSubFeatures.objects.all()
        context['PoliciesSub'] = PoliciesSub
        current_site = Site.objects.last()
        context['url'] = f"{self.request.get_host()}{reverse_lazy('api_hotel:hotel')}"
        return context



class HotelsSinglePage(DetailView):
    model = Hotel
    template_name = 'single_page.html'

    def get_context_data(self, **kwargs):
        context = super(HotelsSinglePage, self).get_context_data(**kwargs)
        hotels = Hotel.objects.all()[:4]
        context['nearest_hotels'] = hotels
        policies = Policies.objects.all()
        context['policyy']=policies
        reviews = Reviews.objects.all()
        context['reviews'] = reviews
        return context
    # def get_context_data(self, **kwargs):
    #     context = super(HotelsSinglePage, self).get_context_data(**kwargs)
    #     context['url'] = f"{self.request.get_host()}{reverse_lazy('hotels_app:hotels-single')}"
    #     print(context['url'])
    #     return context
#

class ReservePage(FormMixin,DetailView):
    template_name = 'payment.html'
    model = RoomType
    context_object_name = 'room_type'

    def post(self,request):
       publishKey = settings.STRIPE_PUBLISHABLE_KEY
       token = request.POST.get('stripeToken', False)
       print('AAAAAAAAAAAAAa')
       if token:
           try:
               charge = stripe.Charge.create(
                   amount=1,
                   currency='usd',
                   description='Example charge',
                   source=token,
               )
               messages.info('Paid successfull')
               return redirect(reverse_lazy('hotels-reserve'))
           except stripe.CardError as e:
                messages.info(request, "Your card has been declined.")
       messages.info('Token not found')
       return redirect(reverse_lazy('hotels-reserve'))

    def get_context_data(self, **kwargs):
        context = super(FormMixin,self).get_context_data(**kwargs)
        hotel = Hotel.objects.filter(pk=self.request.GET.get('HotelId')).first()
        context['hotel'] = hotel
        return context