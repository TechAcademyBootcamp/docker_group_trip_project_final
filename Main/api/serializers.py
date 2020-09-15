from rest_framework import serializers
from Main.models import Subscriber,City
from Hotels.models import Hotel
from Tours.models import Tours
from Restaurants.models import Restaurants


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('email',)

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name',
                  'image',)


class HotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        fields = ('name',
                  )


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurants
        fields = ('name',
                  )


class TourSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tours
        fields = ('name',
                  )


