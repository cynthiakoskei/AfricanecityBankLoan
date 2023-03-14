from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import CustomerSignUpForm
from django.contrib import messages
# Create your views here.


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request,f"Logged in Successfully as {username}")
                return redirect('/')
            else:
                messages.info(request,"Account doesn't exists")
                return redirect('register')
        else:
            messages.info(request,'Invalid credentials')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.error(request,f"Account created successfully")
            login(request, user)
            return redirect('/')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = CustomerSignUpForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_request(request):
    logout(request)
    messages.info(request,"Logged out successfully!")
    return redirect('/')