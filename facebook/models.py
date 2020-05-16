from django.db import models
from django.contrib.auth.models import User
class pub_model (models.Model):

    post=models.CharField(max_length=100)
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return  self.post