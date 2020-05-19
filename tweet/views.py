from django.shortcuts import render ,redirect
from tweet.forms import tweet_pub_form , twwet_pub_model
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from tweet.models import job ,friends
def tweet_home(request):
    jobb=job.objects.all()
    return render(request,'html/tweet_home.html', {'job':jobb})

def friend_profile(request,idd):

    profile=User.objects.filter(id=idd)
    return render(request,"html/friend_profile.html",{'profile':profile})


def change_friend(request,operation , pk ):
    new_friend=User.objects.get(pk=pk)
    if operation =='add':
        friends.make_friend(request.user, new_friend)
    elif operation=='remove':
        friends.lose
    return redirect('blog:base')
class pub_tweet(TemplateView):
    TemplateView='html/tweet_pub.html'
    a=''
    def get(self,request):
        form=tweet_pub_form()
        self.a = ''
        users=User.objects.exclude(id=request.user.id)
        x = twwet_pub_model.objects.filter(user=request.user).order_by('-date')
        return render(request,self.TemplateView,{'form':form,'a':self.a,'x':x,'users':users})

    def post(self,request):
        form=tweet_pub_form(request.POST)
        if form.is_valid():
            self.a='hellooooo'
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('/tweet/tweet_pub')

            form = tweet_pub_form()
            x = twwet_pub_model.objects.filter(user=request.user).order_by('-date')




        return render(request,self.TemplateView,{'form':form,'a':self.a,'x':x})



