from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(username, email, password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('users:index')

    return render(request, 'users/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('users:index')

    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('users:index')

def index(request):
    return render(request, 'users/index.html')
