# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Replace 'home' with your home URL
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm  # Import your custom form

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Use your custom form
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with your home URL
    else:
        form = CustomUserCreationForm()  # Use your custom form
    return render(request, 'signup.html', {'form': form})




def home_view(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('hello_user', username=user.username)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def hello_user_view(request, username):
    return render(request, 'hello_user.html', {'username': username})