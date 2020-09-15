from django.db import models
from django.contrib.auth import get_user_model
from Main.models import City

USER_MODEL = get_user_model()

class Tours(models.Model):

    #relations
    owner = models.ForeignKey(USER_MODEL, related_name='tur', on_delete=models.CASCADE)
    city = models.ManyToManyField(City, verbose_name='City', related_name='tours')

    name = models.CharField('Basligi', max_length=120)
    trip_route = models.CharField('Yol',max_length=1000)
    trip_time = models.CharField('Vaxt',max_length=1000)  
    trip_transport = models.CharField('Neqliyyat',max_length=200)
    price = models.DecimalField('Qiymet',max_digits=6, decimal_places=2)
    main_image = models.ImageField('Main image',upload_to='images/tourimages')

    #moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=True)

    class Meta():
        verbose_name = 'Tur'
        verbose_name_plural = 'Turlar'
        # ordering = ('-created_at', '-title')

    def __str__(self):
        return f"{self.name}" 

class TourComments(models.Model):

    # relations
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    author = models.ForeignKey(USER_MODEL, related_name='comments', on_delete=models.CASCADE)

    # website = models.URLField('Website', null=True, blank=True)
    content = models.TextField('Content')

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=True)



    def __str__(self):
        return self.content


class TourImages(models.Model):

    # relations
    tours  = models.ForeignKey(Tours, on_delete=models.CASCADE , db_index=True , related_name="tour_images")

    images = models.ImageField('Images' , upload_to="images/tours/tourimages")
    

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



