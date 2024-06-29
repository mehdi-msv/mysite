from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
import sweetify
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from mysite import setting
from decouple import config
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                sweetify.success(request,'you logged in successfully')
                return redirect('/')
        else:
            sweetify.error(request,'username or password incorrect')
            return redirect('/')
        
    form = AuthenticationForm()
    context = {'form': form}
    return render(request,'accounts/login.html',context)
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                sweetify.success(request,'your account has been created successfully')
                return redirect('/')
            else:
                sweetify.error(request,'your account didnt created')
                return redirect('/')
        form = CreateUserForm()
        context = {'form': form}
        return render(request,'accounts/signup.html', context)
    else:
        return redirect('/')
def password_reset(request):
    if request.method == 'POST':
        passsword_form = PasswordResetForm(request.POST)
        if passsword_form.is_valid():
            data = passsword_form.cleaned_data['email']
            user_email = User.objects.filter(Q(email=data))
            if user_email.exists():
                for user in user_email:
                    subject = 'Password Request'
                    email_template_name = 'accounts/password_reset_email.txt'
                    parameters ={
                        'email': user.email,
                        'domain':config('DOMAIN',default='127.0.0.1'),
                        'sitename':config('SITENAME',default='Travelista'),
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': config('PROTOCOL',default='http'),
                    }
                    email = render_to_string(email_template_name, parameters)
                    try:
                        send_mail(subject, email, setting.prod.DEFAULT_FROM_EMAIL , [user.email],fail_silently=False)
                    except:
                        return HttpResponse('Invalid Header')
                    return redirect('accounts:password_reset_done')
    else:
        passsword_form = PasswordResetForm()
    context ={
        'passsword_form': passsword_form
        }
    return render(request,'accounts/password_reset.html',context)
    