from django.contrib import admin
from django.urls import path
from django.conf.urls import url , include
from tweet.views import tweet_home , pub_tweet ,friend_profile ,change_friend

app_name='tweet'
urlpatterns = [
    url('^tweet_home$',tweet_home,name='tweet_home'),
    url('^tweet_friend/(?P<idd>\d+)/$',friend_profile,name='tweet_friend'),
    url('^change_friend/(?P<operation>.+)/(?P<pk>\d+)/$',change_friend,name='change_friend'),
    url('^tweet_pub$',pub_tweet.as_view(),name='tweet_pub'),
    #url('^testget/$',testhome.get.as_view()),

]
