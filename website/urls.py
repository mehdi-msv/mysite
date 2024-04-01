from django.conf.urls import url
from website.views import *
from django.urls import path


app_name = 'website'
 
 
urlpatterns = [
    path('',index,name = 'index'),
    path('contact',contact,name='contact'),
    path('about',about,name='about'),
    path('elements',elements,name='elements'),
    path('newsletter',newsletter,name='newsletter'),
]