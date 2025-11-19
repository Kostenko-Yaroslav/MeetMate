from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from users.models import Profile


class UserRegisterForm(UserCreationForm):
    city = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'city']

    def save(self, commit=True):
        user = super().save(commit=True)

        city_data = self.cleaned_data['city']

        token = get_random_string(length=10)

        Profile.objects.create(user=user, city=city_data, unique_code=token)

        return user
