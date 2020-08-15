from django.db import models
from ckeditor.fields import RichTextField

class Contact(models.Model):
    #information
    name = models.CharField('Name',max_length=40)
    email = models.EmailField('Email',max_length=40)
    subject = models.CharField('Subject',max_length=255)
    message = models.TextField('Message')

    # moderation
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f'{self.name} subject:{self.subject}'

    def get_email(self):
        return self.email

# Create your models here.
class City(models.Model):
    #information
    name = models.CharField('Name',max_length=40)
    image = models.ImageField('Image',upload_to='images')

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name

class Places(models.Model):
    #relations
    city = models.ForeignKey(City,verbose_name='City',on_delete=models.CASCADE,related_name='places')

    #information
    title = models.CharField('Name',max_length=40)
    location = models.CharField('Name',max_length=40)
    image = models.ImageField('Image',upload_to='images')
    description = models.TextField('Description')
    latitude = models.DecimalField('Price',max_digits=6,decimal_places=2)
    longtitude = models.DecimalField('Price', max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'Places'
        verbose_name_plural = 'Places'

    def __str__(self):
        return self.title

class Helps(models.Model):
    #information
    popular_questions = models.TextField('Popular questions')
    answers = models.TextField('Answers')

    #moderation
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_published = models.BooleanField('is published', default=True)

    class Meta:
        verbose_name = 'Helps'
        verbose_name_plural = 'Helps'

    def __str__(self):
        return self.popular_questions

class ContactInfo(models.Model):
    #information
    fullname = models.CharField('Fullname',max_length=60)
    email = models.CharField('Email',max_length=40)
    phone_number = models.PositiveIntegerField('Phone Number')
    location = models.CharField('Our location',max_length=100)

    class Meta:
        verbose_name = 'Our Contact'
        verbose_name_plural = 'Our Contacts'

    def __str__(self):
        return self.fullname

class StaticPage(models.Model):
    #information
    terms_of_service = RichTextField('Terms of Service')
    privacy_policy = RichTextField('Privacy Policy')

    #moderation
    # moderation
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_published = models.BooleanField('is published', default=True)

class AboutProject(models.Model):
    #information
    project_devops = models.CharField('Fullname',max_length=60)
    project_developing_start_time = models.DateField()
    project_developing_finish_time = models.DateField()

class WebsiteSettings(models.Model):
    #information
    type_choice = [
        ('az', 'Azerbaijan'),
        ('eng', 'English'),
        ('rus', 'Russian'),
    ]
    languages = models.CharField('Type', max_length=5, choices=type_choice)
