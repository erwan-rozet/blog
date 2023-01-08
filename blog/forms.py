from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = {
             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is title placeholder for example...'}),
             'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
             'author': forms.Select(attrs={'class': 'form-control'}),
             'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm): # une autre class de Form
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
             'title': forms.TextInput(attrs={'class': 'form-control'}),
             'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
             'body': forms.Textarea(attrs={'class': 'form-control'}),
        }