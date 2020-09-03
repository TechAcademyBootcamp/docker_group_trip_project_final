from django.db import models
from Main.models import City
from Account.models import User


def upload_location(instance,filename):
    return 'images/restaurants/%s/images/%s' %(instance.restaurant,filename)

def video_upload_location(instance,filename):
    return 'images/restaurants/%s/video/%s' %(instance.restaurant,filename)

def menu_upload_location(instance,filename):
    return 'images/restaurants/%s/menu/%s' %(instance.name,filename)


class Rating(models.Model):
    point = models.DecimalField('Point',max_digits=2,decimal_places=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=True)

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
    
    def __str__(self):
        return self.point

class Options(models.Model):
    input_type_choice = [
        ('radio', 'radio'),
        ('checkbox', 'checkbox'),
    ]
    option_name = models.CharField('Option Name',max_length=120)
    option_svg_file = models.ImageField('Svg file',upload_to='images/restaurants/svg-files')
    option_input_type = models.CharField('Input type',max_length=10,choices=input_type_choice)
    option = models.CharField('Option',max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=True)

    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = 'Options'
    
    def __str__(self):
        return self.option

class Restaurants(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE, db_index=True, related_name='user_restaurant')
    name = models.CharField('Name',max_length=40)
    rating = models.ForeignKey(Rating,on_delete = models.CASCADE,db_index=True, related_name = 'rating_restaurant')
    city = models.ForeignKey(City, on_delete = models.CASCADE,db_index=True, related_name = 'city_name_restaurant')
    options = models.ManyToManyField(Options, verbose_name='Options', related_name='options_restaurant')
    image = models.ImageField('Image',upload_to=upload_location)
    video = models.FileField('Video',upload_to=video_upload_location)
    website = models.CharField('Website',max_length=250)
    location = models.CharField('Location',max_length=250)
    open_time = models.CharField('Open Time',max_length=250)
    description = models.TextField('Description')
    menu = models.ImageField('Menu',upload_to=menu_upload_location)
    price_range = models.CharField('Price Range',max_length = 40)
    special_diets = models.CharField('Special Diets',max_length = 240)
    meals = models.CharField('Meals',max_length = 240)
    cuisines = models.CharField('Cuisines',max_length=240)
    features = models.CharField('Features',max_length=500)


    
    # Top 3 reasons to eat there
    reason_one = models.CharField('Reason 1', max_length=50)
    reason_one_img = models.ImageField('Reason 1 image',upload_to=upload_location)
    reason_one_short_description = models.CharField('Reason 1 description',max_length=60)
    reason_two = models.CharField('Reason 2', max_length=50)
    reason_two_img = models.ImageField('Reason 2 image',upload_to=upload_location)
    reason_two_short_description = models.CharField('Reason 2 description',max_length=60)
    reason_three = models.CharField('Reason 3', max_length=50)
    reason_three_img = models.ImageField('Reason 3 image',upload_to=upload_location)
    reason_three_short_description = models.CharField('Reason 3 description',max_length=60)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=True)

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'
    
    def __str__(self):
        return self.name
    

class RestaurantImages(models.Model):
    restaurant = models.ForeignKey(Restaurants,on_delete=models.CASCADE, db_index=True, related_name='name_restaurant')
    images = models.ImageField('Image',upload_to=upload_location)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=True)

    class Meta:
        verbose_name = 'Restaurant_image'
        verbose_name_plural = 'Restaurants_images'
    
    def __str__(self):
        return self.restaurant

# Create your models here.
