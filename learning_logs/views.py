from django.shortcuts import render,HttpResponse
from . import models
#def index(request):
#    return render(request,
#                  'learning_logs\index.html',
#                      models.Topics())
def index(request):
    return HttpResponse('<h1>Home page</h1>')
def about(request):
    return HttpResponse('<h1>about page</h1>')
def contact(request):
    return HttpResponse('<h1>contact page</h1>') 