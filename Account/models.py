from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    image = models.ImageField(upload_to='user_images', null=True, blank=True)
    name = models.CharField('name',max_length=50)
    surname = models.CharField('surname' , max_length=50)


    # bio = models.TextField(_('Biography'), null=True, blank=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_avatar(self):
        if self.image:
            return self.image.url
        return 'https://cdt.org/files/2015/10/2015-10-06-FB-person.png'

    @property
    def fullname(self):
        return self.name + self.surname