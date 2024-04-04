from blog.models import *
from django import forms
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post','name','email','subject','message']