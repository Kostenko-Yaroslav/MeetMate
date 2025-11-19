from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.models import Profile


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


class ProfileFrom(ModelForm):
    class Meta:
        model = Profile
        fields = ['city']

class ProfileCreate(CreateView):
    model = Profile
    form_class = ProfileFrom
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

