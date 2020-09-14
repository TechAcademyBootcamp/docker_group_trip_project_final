from django.db import models
from Account.models import User
from Main.models import City
from Hotels.tools.slug_generator import slugify
from datetime import datetime

class RoomTypeBeds(models.Model):
    #information
    count = models.PositiveIntegerField('Count')

    class Meta:
        verbose_name = 'RoomTypeBed'
        verbose_name_plural = 'RoomTypeBeds'

    def __str__(self):
        return str(self.count)

class HotelAmenities(models.Model):
    #information
    name = models.CharField('Name',max_length=40)

    class Meta:
        verbose_name = 'HotelAmenity'
        verbose_name_plural = 'HotelAmenities'

    def __str__(self):
        return self.name

class RoomAmenities(models.Model):
    #information
    name = models.CharField('Name',max_length=40)
    icon = models.CharField('Icon',max_length=200,blank=True,null=True)

    class Meta:
        verbose_name = 'RoomAmenity'
        verbose_name_plural = 'RoomAmenities'

    def __str__(self):
        return self.name

class Hotel(models.Model):
    #information
    name= models.CharField('Name',max_length=50)
    name_description = models.CharField('Name Description',max_length=500)
    short_description = models.CharField('Short Description',max_length=500)
    long_description = models.TextField('Long Description')
    longitude = models.DecimalField('Longitude',max_digits=17,decimal_places=15)
    latitude = models.DecimalField('Latitude', max_digits=17, decimal_places=15)
    phone_number=models.PositiveIntegerField('Phone number')
    website = models.CharField('Website',max_length=50)
    rating = models.DecimalField('Rating',max_digits=2,decimal_places=1)
    main_image = models.ImageField('Main image',upload_to='images/hotelImages')

    #relations
    city = models.ForeignKey(City,verbose_name='City',on_delete=models.CASCADE,
                               db_index=True, related_name='hotels')
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE,
                               db_index=True, related_name='hotels')
    policies = models.ManyToManyField('Policies', verbose_name='Policies', related_name='hotels')
    room_type = models.ManyToManyField('RoomType', verbose_name='Room type', related_name='hotels')
    hotel_amenity=models.ManyToManyField(HotelAmenities,verbose_name='Hotel Amenity',related_name='hotels')
    room_amenity = models.ManyToManyField(RoomAmenities, verbose_name='Room Amenity', related_name='hotels')
    review_fields = models.ManyToManyField('ReviewFields',verbose_name='Review Rating',related_name='hotels')

    #moderations
    slug = models.SlugField('slug', max_length=255, editable=False, unique=True)

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(self.name)}-{datetime.now().strftime("%Y%m%d-%H%M%S")}'
        super().save()

class RoomType(models.Model):
    #information
    title= models.CharField('Room type',max_length=50)
    description = models.CharField('Description',max_length=300)
    price = models.DecimalField('Price',max_digits=7,decimal_places=2)

    #relations
    beds = models.ManyToManyField(RoomTypeBeds,verbose_name='RoomTypeBeds',related_name='room_types')
    child_count = models.ManyToManyField('ChildCount',verbose_name='ChildCount',related_name='room_types')
    room_amenity = models.ManyToManyField(RoomAmenities,verbose_name='Room Amenities',related_name='room_types')

    class Meta:
        verbose_name = 'RoomType'
        verbose_name_plural = 'RoomTypes'

    def __str__(self):
        return self.title

class HotelImages(models.Model):
    #information
    image = models.ImageField('Image',upload_to='images/hotelImages')


    #relations
    hotel=models.ForeignKey(Hotel,verbose_name='Hotel images',on_delete=models.CASCADE,db_index=True,related_name='hotel_images')

    class Meta:
        verbose_name = 'HotelImage'
        verbose_name_plural = 'HotelImages'

    def __str__(self):
        return self.hotel

class Reservation(models.Model):
    reservation_time = models.DateTimeField()
    price = models.DecimalField('Price',max_digits=7,decimal_places=2)
    note = models.CharField('Note',max_length=300)
    day_count = models.PositiveSmallIntegerField('Day count')

    #relations
    room_type = models.ForeignKey(RoomType,verbose_name='Room type',on_delete=models.CASCADE,db_index=True,related_name='reservations')
    user = models.ForeignKey(User,verbose_name='User',on_delete=models.CASCADE,db_index=True,related_name='reservations')
    hotel = models.ForeignKey(Hotel,verbose_name='Hotel',on_delete=models.CASCADE,db_index=True,related_name='reservations')



    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return self.hotel.name


# class Rating(models.Model):
#     #information
#     point = models.PositiveSmallIntegerField()
#
#     #relations
#     hotel = models.ForeignKey(Hotel,verbose_name='Rating',on_delete=models.CASCADE,db_index=True,related_name='ratings')
#     user = models.ForeignKey(User, verbose_name='Rating', on_delete=models.CASCADE, db_index=True,
#                                 related_name='ratings')
#
#     class Meta:
#         verbose_name = 'Rating'
#         verbose_name_plural = 'Ratings'
#
#     def __str__(self):
#         return self.hotel_id

class Reviews(models.Model):
    #information
    title = models.CharField('Title',max_length=50)
    subject= models.TextField('Subject')


    #relations
    # hotel = models.ForeignKey(Hotel, verbose_name='Review of hotel', on_delete=models.CASCADE, db_index=True,
    #                              related_name='reviews')
    # user = models.ForeignKey(User, verbose_name='Review of user', on_delete=models.CASCADE, db_index=True,
    #                             related_name='reviews')
    # review_fields = models.ManyToManyField('ReviewFields',verbose_name='Rating of review',
    #                              related_name='reviews')
    reservation = models.ForeignKey(Reservation,verbose_name='Reservation', on_delete=models.CASCADE, db_index=True,
                                 related_name='reviews')
    review_rating = models.ManyToManyField('ReviewRating',verbose_name='REview rating',related_name='reviews')

    #moderation
    created_at = models.DateTimeField()

    class Meta:
        verbose_name = 'Reviews'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.title

class PoliciesSubFeatures(models.Model):
    # information
    title = models.CharField('Title', max_length=100)
    #relations
    policies = models.ForeignKey('Policies', verbose_name='Policies', on_delete=models.CASCADE,
                                 db_index=True,
                                 related_name='PoliciesSubFeatures')
    class Meta:
        verbose_name = 'Policies SubFeatures'
        verbose_name_plural = 'Policies SubFeatures'

    def __str__(self):
        return self.title

class Policies(models.Model):
    #information
    title=models.CharField('Title',max_length=100)



    class Meta:
        verbose_name = 'Policies'
        verbose_name_plural = 'Policies'

    def __str__(self):
        return self.title


class ReviewFields(models.Model):
    #information
    title = models.CharField('Title',max_length=100)

    #relations
    class Meta:
        verbose_name = 'ReviewFields'
        verbose_name_plural = 'ReviewFields'

    def __str__(self):
        return self.title

class ReviewRating(models.Model):
    #information
    rating_point = models.PositiveSmallIntegerField('Review Rating',default=5)

    #relations
    # review = models.ManyToManyField(Reviews,verbose_name='Review',related_name='reviewRating')
    review_field = models.ManyToManyField(ReviewFields, verbose_name='Review field', related_name='reviewRating')

    class Meta:
        verbose_name = 'ReviewRating'
        verbose_name_plural = 'ReviewRatings'

    def __str__(self):
        return f'{self.rating_point}'

class ChildCount(models.Model):
    #information
    count = models.PositiveIntegerField('Count')

    class Meta:
        verbose_name = 'ChildCount'
        verbose_name_plural = 'ChildCount'

    def __str__(self):
        return str(self.count)
