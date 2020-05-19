from django.db import models
from django.contrib.auth.forms import User

class twwet_pub_model(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)

    title_pub=models.CharField(max_length=50)
    text_pub=models.CharField(max_length=50)
    date=models.DateField(auto_now=True)


class friends(models.Model):
    users=models.ManyToManyField(User)
    current_user=models.ForeignKey(User ,related_name='owner', on_delete=models.CASCADE , null=True)


    @classmethod
    def make_friend(cls,current_user, new_friend):
        friend , created=cls.objects.get_or_create(

            current_user=current_user
        )
        friends.users.add(new_friend)

    @classmethod
    def lose_friend(cls,current_user,new_friend):
        friend, created=cls.objects.get_or_create(

            current_user=current_user
        )
        friends.users.remove(new_friend)













class name(models.Model):

    fname=models.CharField(max_length=100)
    age=models.IntegerField(default=18)
    def __str__(self):
        return self.fname


class job(models.Model):
       fname=models.ForeignKey('name',on_delete=models.CASCADE)
       job_name=models.CharField(max_length=100)

       def __str__(self):
           return self.job_name

class adress(models.Model):
    fname=models.ForeignKey('name',on_delete=models.CASCADE)
    job_name=models.ForeignKey('job',on_delete=models.CASCADE,related_name='maps')
    adress=models.CharField(max_length=100)

    def __str__(self):
        return self.adress