from django.shortcuts import render , redirect
from django.http import  HttpResponse
from blog.forms import create_user ,edit_profile  ,User_profile
from django.contrib.auth.forms import UserCreationForm , UserChangeForm

def base(request):

    return  render(request,'html/base.html')
def create_user_view (request):
    if request.method=='POST':
        form=UserCreationForm(request.POST )
        if form.is_valid():
            form.save()
            return redirect('/blog/base')
    else:
        form = UserCreationForm()
        context={'form':form}
        return render(request, 'html/register_view.html', context)

def create_user_form(request):
    if request.method=='POST':
        form=create_user(request.POST )
        if form.is_valid():
            form.save()
            return redirect('/blog/base')
    else:
        form = create_user()
        context={'form':form}
        return render(request, 'html/register_view.html', context)

    """form=create_user(request.POST or None)
    if form.is_valid():
        form.save()
    context={'form':form}
    return render(request, 'html/register_form.html', context)
"""

def profile(request):
    context={'user':request.user}
    return render(request, 'html/profile.html', context)


def edit_profile_view(request):
    if request.method=='POST':
        form=UserChangeForm(request.POST ,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/blog/profile')
    else:
        form=UserChangeForm(instance=request.user)
        context = {'form': form}
        return render(request, 'html/edit_profile_view.html', context)


def edit_profile_form(request):
    if request.method=='POST':
        form=edit_profile(request.POST ,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/blog/profile')
    else:
        form=edit_profile(instance=request.user)
        context = {'form': form}
        return render(request, 'html/edit_profile_form.html', context)


