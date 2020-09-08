from django.template import Library
from Restaurants.models import Restaurants
register = Library()

@register.simple_tag
def countRestaurants():
    restaurant = Restaurants.objects.filter(is_published = 'True').count()
    context = {
        'restaurant' : restaurant
    }
    return context

@register.simple_tag
def get_star_count(star_count):
    star_html = ''
    print(type(star_count))
    for i in range(int(float(star_count))):
        star_html = star_html + '<span class="fa fa-star checked"></span>'
    for i in range(int(5-star_count)):
        star_html = star_html + '<span class="fa fa-star"></span>'
    return star_html
