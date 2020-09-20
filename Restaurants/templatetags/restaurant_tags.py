from django.template import Library
from Restaurants.models import Restaurants, RestaurantImages, ToEatReason, RestaurantMenuImages
from django.db.models import Sum, F
from django.db.models.expressions import Window
from django.db.models.functions import Rank
register = Library()

@register.simple_tag
def countRestaurants():
    restaurant = Restaurants.objects.filter(is_published = 'True').count()
    context = {
        'restaurant' : restaurant, 
    }
    return context

@register.simple_tag
def countRestaurantsCity(city):
    count = Restaurants.objects.filter(is_published='True',city__name=city).count()
    near_by_restaurants = Restaurants.objects.filter(is_published='True',city__name=city)[:4]
    context = {
        'count' : count,
        'near_by_restaurants' : near_by_restaurants,
    }
    return context


@register.simple_tag
def get_star_count(star_count):
    star_html = ''
    for i in range(int(float(star_count))):
        star_html = star_html + '<span class="fa fa-star checked"></span>'
    for i in range(int(5-float(star_count))):
        star_html = star_html + '<span class="fa fa-star"></span>'
    return star_html

@register.simple_tag
def images_count(id):
    count = RestaurantImages.objects.filter(is_published='True',restaurant__id=id).count()
    return count

@register.simple_tag
def images(id):
    all_images = RestaurantImages.objects.filter(is_published='True',restaurant__id=id)
    return all_images

@register.simple_tag
def reason_to_eat(id):
    reasons = ToEatReason.objects.filter(is_published='True',restaurant__id=id)[:3]
    return reasons

@register.simple_tag
def menu_images(id):
    images = RestaurantMenuImages.objects.filter(is_published='True',restaurant__id=id)
    return images

@register.simple_tag
def restaurant_place(id,city):
    place=1
    ordering = Restaurants.objects.filter(is_published='True',city__name=city).order_by('-rating')
    for item in ordering:
        if item in Restaurants.objects.filter(is_published='True',id=id):
            break
        place += 1
    return place

@register.simple_tag
def restaurant_place_all(id):
    place=1
    ordering = Restaurants.objects.filter(is_published='True').order_by('-rating')
    for item in ordering:
        if item in Restaurants.objects.filter(is_published='True',id=id):
            # print(place)
            break
        place += 1
    return place
