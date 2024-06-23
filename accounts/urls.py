from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views
app_name = 'accounts'

urlpatterns = [
    path('login/',login_view,name='login'),
    path('logout',logout_view,name='logout'),
    path("signup",signup_view,name='signup'),
    path("password_reset/",password_reset,name='password_reset'),
    path("password_reset_done/",auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path("password_reset_confirm/<uidb64>/<token>",auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path("password_reset_complete/",auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]
