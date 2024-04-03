from django.forms import ModelForm
from website.models import *
from django import forms
from captcha.fields import CaptchaField
class ContactForm(forms.Form):
    captcha = CaptchaField()
    class Meta:
         model = Contact
         fields = '__all__'
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'