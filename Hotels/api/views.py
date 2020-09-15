from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from Hotels.api.serializers import HotelSerializer
from Hotels.models import Hotel

class PhoneNumber(APIView):
    def get(self,request):
        data = request.GET
        print(data.get('phone_number'))


class HotelListView(ListAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()

    def get_queryset(self):
        data = self.request.GET
        print(data.getlist('hotel_amenities[]'))
        hotelAmenities=data.getlist('hotel_amenities[]')
        roomAmenities = data.getlist('room_amenities[]')
        cityName=data.get('cityName')
        selectedBed = data.get('selectedBed')
        minPrice = data.get('minPrice')
        maxPrice = data.get('maxPrice')
        selectedChildCount = data.get('selectedChildCount')
        filtered_hotels = Hotel.objects.all()
        if cityName :
            filtered_hotels=Hotel.objects.filter(city__name__icontains=cityName)
            print('AAAAA111111',filtered_hotels)
        #     filtered_hotels=Hotel.objects.filter(hotel_amenities__in=[hotel_amenity for hotel_amenity in
        # data.get('hotel_amenities')])
        if selectedBed:
            filtered_hotels = filtered_hotels.filter(room_type__beds__count=selectedBed)
            print('AAAAA222222222', filtered_hotels)
        if selectedChildCount:
            filtered_hotels = filtered_hotels.filter(room_type__child_count__count=selectedChildCount)
            print('AAAAA33333333333', filtered_hotels)
        if minPrice:
            filtered_hotels=filtered_hotels.filter(min_price__gte=minPrice)
            print('AAAAA4444444444444444', filtered_hotels)
        if maxPrice:
            filtered_hotels=filtered_hotels.filter(min_price__lte=maxPrice)
            print('AAAAA555555555555555', filtered_hotels)
        if hotelAmenities:
            filtered_hotels=filtered_hotels.filter(hotel_amenity__name_in=hotelAmenities).distinct('name')
            print('AAAAA6666666666666666', filtered_hotels)
        if roomAmenities:
            filtered_hotels=filtered_hotels.filter(room_amenity__name__in=roomAmenities)
            print('AAAA77777777777777777', filtered_hotels)
        print(filtered_hotels)
        return filtered_hotels