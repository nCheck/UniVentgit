import itertools
from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import College, Profile
from django.utils.text import slugify

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ['name' , 'photo' , 'pincode' ,'website']
        exclude = ['slug']



class SignUpForm(UserCreationForm):
    college = forms.ModelChoiceField(queryset=College.objects.all() ,to_field_name='name' , empty_label=None)
    class Meta:
        model = User
        fields = ('username', 'email' , 'college', 'password1', 'password2' )



    # def save(self):
    #     instance = super(College, self).save(commit=False)
    #
    #     instance.slug = orig = slugify(instance.title)
    #
    #     for x in itertools.count(1):
    #         if not College.objects.filter(slug=instance.slug).exists():
    #             break
    #         instance.slug = '%s-%d' % (orig, x)
    #
    #     instance.save()
    #
    #     return instance
