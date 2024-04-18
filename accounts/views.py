from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
import sweetify

def login_view(request):
    if request.user.is_authenticated:
        next_url = request.POST.get('next')
        print(next_url)
        return redirect(next_url)
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                next_url = request.POST.get('next')
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
            
        
            
        
