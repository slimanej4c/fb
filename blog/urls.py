from django.contrib import admin
from django.urls import path
from django.conf.urls import url , include
from blog.views import create_user_view , create_user_form ,profile,edit_profile_view,edit_profile_form ,base
from django.contrib.auth.views import LoginView,LogoutView
app_name='blog'
urlpatterns = [
    url(r'^user_view/$',create_user_view,name='create_user_view'),
    url(r'^base/$',base,name='base'),
    url(r'^user_form/$',create_user_form,name='create_user_form'),
    url(r'^profile/$',profile,name='create_profile'),
    url(r'^profile/edit_view/$',edit_profile_view,name='edit_view'),
    url(r'^profile/edit_form/$',edit_profile_form,name='edit_form'),

    url(r'^login/$',LoginView.as_view(template_name='html/login.html'),name='login'),
    url(r'^logout/$',LogoutView.as_view(template_name='html/logout.html'),name='logout'),

]
