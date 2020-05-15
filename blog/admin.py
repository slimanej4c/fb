from django.contrib import admin
from blog.models import  User_profile



class user_profile_admin(admin.ModelAdmin):
    list_display = ['city','website','phone','description','user_info']
    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset=super(user_profile_admin,self).get_queryset(request)
        queryset=queryset.order_by('phone')
        return queryset


admin.site.register(User_profile, user_profile_admin)
# Register your models here.

