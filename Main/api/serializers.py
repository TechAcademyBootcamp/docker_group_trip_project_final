from rest_framework import serializers
from Main.models import Subscriber,City


class SubscriberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriber
        fields = ('email',)

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('name',
                  'image',)