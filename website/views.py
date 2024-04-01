from django.shortcuts import render
from website.forms import *
from django.http import HttpResponseRedirect
def index(request):
    return render(request,'website/index.html')
def about(request):
    return render(request,'website/about.html')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    form = ContactForm()
    context = {'form': form}
    return render(request,'website/contact.html',context)
def elements(request):
    return render(request,'website/elements.html')
def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        print(form,'_______________________')
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')