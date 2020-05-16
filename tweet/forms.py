from django import forms
from tweet.models import twwet_pub_model
class tweet_pub_form(forms.ModelForm):

    #title_pub=forms.CharField(max_length=100)
    #text_pub=forms.CharField(max_length=100)
    class Meta:
        model=twwet_pub_model

        fields=('title_pub','text_pub')




