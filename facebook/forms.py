from django import forms
from facebook.models import pub_model
class pub_form(forms.ModelForm):
    post=forms.CharField()
    class Meta:

        model=pub_model
        fields=('post',)

