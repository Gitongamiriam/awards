from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    prof_pic = models.ImageField(upload_to='images/')
    bio = models.TextField(blank=True)
    objects = models.Manager()

    class Meta:
        ordering = ['bio']

        

    def __str__(self):
       return f'{self.user.username} Profile'

