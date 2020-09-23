from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from Hotels.api.serializers import HotelSerializer
from Hotels.models import Hotel
import math
from rest_framework.response import Response
import requests
import json

class PhoneNumber(APIView):
    def get(self,request):
        data = request.GET
        driver = data.get('driver_id')
        phone_number = data.get('phone_number')
        headers = {
            'api_key': '15b056aae8c5b037ff52ffa5b6cd1180',
            'Content-type': 'application/json'
        }
        driver_request = requests.get(f'http://0727-dmitrov.ligataxi.com/api/v1/drivers/{driver}/',headers=headers)
        driver_data=driver_request.json()
        car = driver_data.get('car')
        text = f'За вами приедет {car} '
        after_url = {'number':phone_number,
                     'text':text,
                     'sign':'Tach Taxi',
                     'channel':'DIRECT'}

        url = requests.get('https://agil.makhmudov@mail.ru:Q9BqK8I8HXoEx1hVIhcE4gRkBVa1@gate.smsaero.ru/v2/sms/send?',params=after_url)
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',url.status_code)


class HotelListView(APIView):

    def get(self,request):
        data = request.GET
        hotelAmenities=data.getlist('hotel_amenities[]')
        roomAmenities = data.getlist('room_amenities[]')
        cityName=data.get('cityName')
        selectedBed = data.get('selectedBed')
        minPrice = data.get('minPrice')
        maxPrice = data.get('maxPrice')
        selectedChildCount = data.get('selectedChildCount')
        filtered_hotels = Hotel.objects.all()
        if cityName :
            filtered_hotels=filtered_hotels.filter(city__name__icontains=cityName).distinct()
        if selectedBed:
            filtered_hotels = filtered_hotels.filter(room_type__beds__count=selectedBed).distinct()
        if selectedChildCount:
            filtered_hotels = filtered_hotels.filter(room_type__child_count__count=selectedChildCount).distinct()
        if minPrice:
            filtered_hotels=filtered_hotels.filter(min_price__gte=minPrice).distinct()
        if maxPrice:
            filtered_hotels=filtered_hotels.filter(min_price__lte=maxPrice).distinct()
        if hotelAmenities:
            for hotelAmenity in hotelAmenities:
                filtered_hotels = filtered_hotels.filter(hotel_amenity__name=hotelAmenity)
        if roomAmenities:
            for roomAmenity in roomAmenities:
                filtered_hotels=filtered_hotels.filter(room_amenity__name=roomAmenity)
        print(filtered_hotels)
        hotels_count = filtered_hotels.count()
        hotel_count_for_each_page = 5
        page_count = math.ceil(hotels_count/hotel_count_for_each_page)
        page_range = range(1,page_count+1)

        page = data.get('page',1)
        print('BBBBBBBBBBBBBBBBBBBBBBBBBBBBB',page)
        if isinstance(page, str) and page.isdigit():
            page = int(page)
        hotels_for_each_page = filtered_hotels[(page-1)*5:page*5]
        serializered_hotels = HotelSerializer(hotels_for_each_page,many=True)
        return Response({
            'filtered_hotels': serializered_hotels.data,
            'page_range': page_count,
        })




