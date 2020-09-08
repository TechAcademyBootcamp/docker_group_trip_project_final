from django.db import models
from Main.models import City
from Account.models import User


def upload_location(instance,filename):
    return 'images/restaurants/%s/images/%s' %(instance.name,filename)

def video_upload_location(instance,filename):
    return 'images/restaurants/%s/video/%s' %(instance.name,filename)

def menu_upload_location(instance,filename):
    return 'images/restaurants/%s/menu/%s' %(instance.name,filename)

class OptionListTypeCheckbox(models.Model):
    option_name = models.CharField('Option',max_length=120)

    class Meta:
        verbose_name = 'Option List Type Checkbox'
        verbose_name_plural = 'Option Lists Type Checkbox'
    
    def __str__(self):
        return self.option_name

class OptionsTypeCheckbox(models.Model):
    option_name = models.CharField('Option Name',max_length=120)
    option_svg_file = models.FileField('Svg file',upload_to='images/restaurants/svg-files')
    option_inputs =  models.ManyToManyField(OptionListTypeCheckbox, verbose_name='Options', related_name='input_restaurant_checkbox')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=True)

    class Meta:
        verbose_name = 'Option Type Checkbox'
        verbose_name_plural = 'Options Type Checkbox'
    
    def __str__(self):
        return self.option_name

class OptionListTypeRadio(models.Model):
    option_name = models.CharField('Option',max_length=120)

    class Meta:
        verbose_name = 'Option List Type Radio'
        verbose_name_plural = 'Option Lists Type Radio'
    
    def __str__(self):
        return self.option_name

class OptionsTypeRadio(models.Model):
    option_name = models.CharField('Option Name',max_length=120)
    option_svg_file = models.FileField('Svg file',upload_to='images/restaurants/svg-files')
    option_inputs =  models.ManyToManyField(OptionListTypeRadio,verbose_name='Option',related_name='input_restaurant_radio')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=True)

    class Meta:
        verbose_name = 'Option Type Radio'
        verbose_name_plural = 'Options Type Radio'
    
    def __str__(self):
        return self.option_name

class Restaurants(models.Model):
    rating_type_choice = [
        ('0.5', '0.5'),
        ('1.0', '1.0'),
        ('1.5', '1.5'),
        ('2.0', '2.0'),
        ('2.5', '2.5'),
        ('3.0', '3.0'),
        ('3.5', '3.5'),
        ('4.0', '4.0'),
        ('4.5', '4.5'),
        ('5.0', '5.0'),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE, db_index=True, related_name='user_restaurant')
    name = models.CharField('Name',max_length=40)
    rating = models.CharField('Rating',max_length=10,choices=rating_type_choice)
    city = models.ForeignKey(City, on_delete = models.CASCADE,db_index=True, related_name = 'city_name_restaurant')
    checkbox_options = models.ManyToManyField(OptionListTypeCheckbox, verbose_name='Options', related_name='options_restaurant_checkbox')
    radio_options = models.ForeignKey(OptionListTypeRadio,on_delete = models.CASCADE,db_index=True,related_name='options_restaurant_radio')
    image = models.ImageField('Main Image',upload_to=upload_location)
    phone_number = models.CharField('Phone Number',max_length=40)
    video = models.FileField('Video',upload_to=video_upload_location)
    website = models.CharField('Website',max_length=250)
    location = models.CharField('Location',max_length=250)
    open_time = models.TimeField('Open Time')
    close_time = models.TimeField('Close Time')
    description = models.TextField('Description')
    menu = models.ImageField('Menu',upload_to=menu_upload_location)
    price_range = models.CharField('Price Range',max_length = 40)
    special_diets = models.CharField('Special Diets',max_length = 240)
    meals = models.CharField('Meals',max_length = 240)
    cuisines = models.CharField('Cuisines',max_length=240)
    features = models.CharField('Features',max_length=500)

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



class ToEatReason(models.Model):
    rating_type_choice = [
        ('0.5', '0.5'),
        ('1', '1'),
        ('1.5', '1.5'),
        ('2', '2'),
        ('2.5', '2.5'),
        ('3', '3'),
        ('3.5', '3.5'),
        ('4', '4'),
        ('4.5', '4.5'),
        ('5', '5'),
    ]
    restaurant = models.ForeignKey(Restaurants,on_delete=models.CASCADE, db_index=True, related_name='eat_reason_restaurant')
    reason = models.CharField('Reason ', max_length=50)
    reason_img = models.ImageField('Reason image',upload_to=upload_location)
    reason_rating = models.CharField('Rating',max_length=10,choices=rating_type_choice)
    reason_short_description = models.CharField('Reason description',max_length=60)

# Create your models here.
