from django.conf.urls import url
from .views import *
from django.urls import path
urlpatterns = [
    path('',index),
    path('contact',contact),
    path('about',about),
]