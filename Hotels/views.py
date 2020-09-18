from django.shortcuts import render, redirect
from django.views.generic import ListView,CreateView,DetailView,View
from Hotels.models import Hotel,HotelAmenities,PoliciesSubFeatures,RoomAmenities,Reservation,RoomType,Policies,Reviews,ReviewFields
from Account.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from django.contrib.sites.models import Site
from django.conf import settings
import stripe
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import date,timedelta
import decimal

stripe.api_key = settings.STRIPE_SECRET_KEY

class HotelsListView(ListView):
    model = Hotel
    template_name = 'hotels.html'
    paginate_by = 1
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
        page = self.request.GET.get('page', 1) if self.request.GET.get('page', 1) != '' else 1
        data = self.get_queryset()
        if data:
            paginator = Paginator(data, self.paginate_by)
            results = paginator.page(page)
            index = results.number - 1
            max_index = len(paginator.page_range)
            start_index = index - 5 if index >= 5 else 0
            end_index = index + 5 if index <= max_index - 5 else max_index
            context['page_range'] = list(paginator.page_range)[start_index:end_index]
        print(context['url'])
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

    def post(self,request, *args, **kwargs):
        publishKey = settings.STRIPE_PUBLISHABLE_KEY
        token = request.POST.get('stripeToken', False)
        if token:
            customer = stripe.Customer.create(
                email=request.user.email,
                name=request.user.username,
                source=token
            )
            charge = stripe.Charge.create(
                customer=customer,
                amount=16000,
                currency='usd',
                description='Example charge',
            )
            start_date=request.GET.get('first_date',date.today())
            fin_date=request.GET.get('second_date',date.today()+timedelta(1))
            day_count = request.GET.get('total_days',1)
            hotel = Hotel.objects.filter(id=request.GET.get('HotelId')).first()
            price = (int(self.get_object().price)*day_count)
            print('PPPPPPPPPPPPPPPPPPPPPPPPP',self.get_object().price)

            reservation = Reservation(
                reservation_start_date=start_date,
                reservation_fin_date=fin_date,
                price=price,
                day_count=day_count,
                room_type=self.get_object(),
                user=request.user,
                hotel=hotel,
            )
            # print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',reservation,reservation.price)
            reservation.save()
            messages.success(request, 'Paid successfull!')
            return redirect(reverse_lazy('hotels-reserve'))
        messages.success(request, 'Token not found!')

        return redirect(reverse_lazy('hotels-reserve'))

    def get_context_data(self, **kwargs):
        context = super(FormMixin,self).get_context_data(**kwargs)
        hotel = Hotel.objects.filter(pk=self.request.GET.get('HotelId')).first()
        context['hotel'] = hotel
        return context


class ReviewSendView(View):
    def get(self,request):
        review_fields = ReviewFields.objects.all()
        user = User.objects.all()[0]
        context={
            'review_fields':review_fields,
            'user':user,
        }
        print(context)
        return render(request,'review.html',context)

