from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import  post_save

class User_profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    description=models.CharField(max_length=100,default='')
    city=models.CharField(max_length=20,default=' ')
    website=models.URLField(default='')
    phone=models.IntegerField(default=0)
    def __str__(self):
        return  self.user.username

def create_profile(sender,**kwargs):
    if kwargs['created']:
        USER_profile=User_profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile , sender=User)


