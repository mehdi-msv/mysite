from .views import *
from django.urls import path


app_name = 'accounts'

urlpatterns = [
    path('login/',login_view,name='login'),
#    path('logout',logout_view,name='logout'),
#    path("signup",signup_view,name='signup'),
    
]