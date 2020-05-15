from django.contrib import admin
from django.urls import path
from django.conf.urls import url , include
from facebook.views import pub_views

app_name='facebook'
urlpatterns = [
    url('^pub/(?P<idd>[0-9])$',pub_views.as_view(),name='pub'),
    #url('^testget/$',testhome.get.as_view()),

]
