from rest_framework.generics import ListAPIView
from Hotels.api.serializers import HotelSerializer
from Hotels.models import Hotel


class HotelListView(ListAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()

    def get_queryset(self):
        data = self.request.GET
        print(data)
        print(data.get('hotel_amenities[]'))
        cityName=data.get('cityName')
        selectedBed = data.get('selectedBed')
        filtered_hotels = Hotel.objects.all()
        if cityName or selectedBed:
            filtered_hotels=Hotel.objects.filter(city__name__icontains=cityName)
            # filtered_hotels=Hotel.objects.filter(hotel_amenities__in=[hotel_amenity for hotel_amenity in
        # data.get('hotel_amenities')])
        return filtered_hotels