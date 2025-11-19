from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from users.forms import UserRegisterForm

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('users:profile')

class UserProfileView(ListView):
    model = User
    template_name = 'users/profile.html'

def logout_view(request):
    logout(request)
    return redirect('users:register')

def index(request):
    return render(request, 'users/index.html')



