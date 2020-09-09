from rest_framework.generics import ListAPIView
from Hotels.api.serializers import HotelSerializer
from Hotels.models import Hotel


class HotelListView(ListAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()