from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout , authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'User already exist')
                return redirect('signup')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email already exist')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                    user.save()
                    messages.success(request, 'Account successful')
                    return redirect('signin')
        else:
            messages.error(request, 'User already exist')
            return redirect('signin')
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('profile')

    return render(request, 'signin.html')

def profile(request):
    return render(request, 'profile.html')

def signout(request):
    logout(request)
    messages.error(request, 'You are signed out')
    return redirect('signin')