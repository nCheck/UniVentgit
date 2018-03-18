from django import forms
from .models import College

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ['name' , 'photo' , 'pincode' ,'website']

