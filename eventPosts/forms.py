from django import forms
from .models import Post , Comment

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'event_date', 'pdf')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'textinputclass'}) ,
            'text' : forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author' , 'text')
        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
