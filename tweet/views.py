from django.shortcuts import render
from tweet.forms import tweet_pub_form , twwet_pub_model
from django.views.generic import TemplateView
def tweet_home(request):
    return render(request,'html/tweet_home.html')


class pub_tweet(TemplateView):
    TemplateView='html/tweet_pub.html'
    a=''
    def get(self,request):

        form=tweet_pub_form()
        self.a = ''
        return render(request,self.TemplateView,{'form':form,'a':self.a})




    def post(self,request):
        form=tweet_pub_form(request.POST)
        if form.is_valid():
            self.a='hellooooo'
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            form = tweet_pub_form()
            x = twwet_pub_model.objects.filter(user=request.user)


        return render(request,self.TemplateView,{'form':form,'a':self.a,'x':x})



