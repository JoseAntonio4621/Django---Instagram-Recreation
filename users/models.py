#users models

#django
from django.db import models
from django.contrib.auth.models import User 

class Profile(models.Model):
    #profile model
    #Proxy model that extends the base data with other info

    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)

    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        #return username
        return self.user.username



