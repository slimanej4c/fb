from django.shortcuts import render
from django.views.generic import TemplateView
from facebook.forms import pub_form , pub_model

class pub_views(TemplateView):
     template_name = "html/pub.html"


     def get(self, request,idd):
          x = pub_model.objects.filter(user=request.user)
          form=pub_form()
          return render(request,self.template_name,{'form':form,'x':x})


     def post(self,request,idd):
          form=pub_form(request.POST)
          text=[]
          if form.is_valid():

               post=form.save(commit=False)
               post.user=request.user
               post.save()
               text.append(form.cleaned_data['post'])

               form = pub_form()
               x = pub_model.objects.filter(user=request.user)

          return render(request, self.template_name, {'form': form,'text':text,'x':x})

