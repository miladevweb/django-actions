from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

def upload_to(instance, filename):
    return f'thumbnails/user/{instance.username}/{filename}'

class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    thumbnail = models.ImageField(max_length=500, blank=False, null=False)
    thumbnail_url = models.CharField(blank=True, null=True, max_length=500)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('users')
    
    @property
    def get_thumbnail_url(self):
        basic_url = self.thumbnail.url.replace('https%3A/firebasestorage.googleapis.com/v0/b/docker-actions-58467.appspot.com/o/', '')
        user_with_equal = basic_url.replace('%3D', '=')
        user_with_ampersand = user_with_equal.replace('%26', '&')
        user_with_interrogant = user_with_ampersand.replace('%3F', '?')
        if '%252F' in user_with_interrogant:
            user_with_2f = user_with_interrogant.replace('%252F', '%2F')
            if '%2520' in user_with_2f:
                user_with_20 = user_with_2f.replace('%2520', '%20')
                return user_with_20
            return user_with_2f
        else:
            pass


    
    


    