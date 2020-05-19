from django import forms
from tweet.models import twwet_pub_model
class tweet_pub_form(forms.ModelForm):

    title_pub=forms.CharField(widget=forms.TextInput(
        attrs={"class":"form-control",}
    ))
    text_pub = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control","placeholder":"creer votre pub ",}
    ))

    class Meta:
        model=twwet_pub_model

        fields=('title_pub','text_pub')




