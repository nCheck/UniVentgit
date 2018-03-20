import itertools
from django import forms
from .models import College
from django.utils.text import slugify

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ['name' , 'photo' , 'pincode' ,'website']
        exclude = ['slug']

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
