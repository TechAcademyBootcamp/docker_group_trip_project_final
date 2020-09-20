from rest_framework.decorators import api_view
from Restaurants.models import Restaurants
from Restaurants.api.serializers import RestaurantSerializer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT
from django.db.models import Q


@api_view(http_method_names=('GET',))
def restaurants_api(request):
    checkbox_options = request.GET.getlist('option_checkbox_input[]')
    radio_options = request.GET.get('option_radio_input')
    input_value = request.GET.get('find_restaurant')
    dropdown_filter = request.GET.get('restaurant_dropdown_text')
    list_restaurants = Restaurants.objects.all()
    if input_value:
        list_restaurants  = list_restaurants.filter(Q(city__name__icontains=input_value)|Q(name__icontains=input_value))
    if checkbox_options :
        for checkbox_option in checkbox_options:
            list_restaurants = list_restaurants.filter(is_published=True,checkbox_options__option_name=checkbox_option)
    if radio_options :
        list_restaurants = list_restaurants.filter(is_published=True,radio_options__option_name=radio_options)
    if not input_value and not checkbox_options and not radio_options:
        list_restaurants = Restaurants.objects.filter(is_published=True)
    restaurants = list_restaurants
    serializer = RestaurantSerializer(restaurants,many=True)
    response_data = {
        'message' : 'success',
        'action' : 'read',
    }
    response_data['restaurants'] = serializer.data

    status_code = HTTP_200_OK

    return Response(response_data, status=status_code)


# @api_view(http_method_names=('GET',))
# def restaurants_query(request):
#     input_value = request.GET.get('search_input')
#     restaurant_query = Restaurants.objects.filter(Q(city__name__icontains=input_value)|Q(name__icontains=input_value))[:2]
#     response_data = {
#         'message' : 'success',
#         'action' : 'read',
#     }
#     restaurant_serializer = RestaurantSerializer(restaurant_query, many=True)
#     response_data['restaurants_query'] = restaurant_serializer.data
#     status_code = HTTP_200_OK
#     return Response(response_data, status=status_code)

