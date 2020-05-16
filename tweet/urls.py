from django.contrib import admin
from django.urls import path
from django.conf.urls import url , include
from tweet.views import tweet_home , pub_tweet

app_name='tweet'
urlpatterns = [
    url('^tweet_home$',tweet_home,name='tweet_home'),
    url('^tweet_pub$',pub_tweet.as_view(),name='tweet_pub'),
    #url('^testget/$',testhome.get.as_view()),

]
