from django.db import models
from django.contrib.auth.forms import User

class twwet_pub_model(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)

    title_pub=models.CharField(max_length=50)
    text_pub=models.CharField(max_length=50)
    date=models.DateField(auto_now=True)
