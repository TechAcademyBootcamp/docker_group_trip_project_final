from rest_framework.generics import ListAPIView
from Hotels.api.serializers import HotelSerializer

class HotelListView(ListAPIView):
    serializer_class = HotelSerializer
