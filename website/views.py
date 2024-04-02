from django.shortcuts import render
from website.forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages
import sweetify
def index(request):
    return render(request,'website/index.html')
def about(request):
    return render(request,'website/about.html')
def contact(request):
    if request.method == 'POST':
        post = request.POST.copy()
        post['name']= 'unknown'
        form = ContactForm(post)
        if form.is_valid():
            form.save()
            sweetify.success(request,'your ticket submitted successfully')
            
        else:
            sweetify.error(request,'your ticket didnt submitted')
    form = ContactForm()
    context = {'form': form}
    return render(request,'website/contact.html',context)
def elements(request):
    return render(request,'website/elements.html')
def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'___________')
        else:
            messages.error(request,'--------')