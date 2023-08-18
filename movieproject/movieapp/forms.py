from django import forms
from.models import Movie1
# from.forms import movie_form
class movie_form(forms.ModelForm):
     class Meta:
        model=Movie1
        fields=['name','desc','year','img']

