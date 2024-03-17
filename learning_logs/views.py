from django.shortcuts import render,HttpResponse
from . import models
#def index(request):
#    return render(request,
#                  'learning_logs\index.html',
#                      models.Topics())
def index(request):
    return render(request,'website/index.html')
def about(request):
    return render(request,'website/about.html')
def contact(request):
    return render(request,'website/contact.html')