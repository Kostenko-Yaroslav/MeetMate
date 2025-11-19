from django.contrib.auth.models import User
from django.db import models
from django.utils.crypto import get_random_string


def generate_unique_code():
    return get_random_string(length=10)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    unique_code = models.CharField(max_length=10, default=generate_unique_code, null=True, blank=True)
    telegram_id = models.CharField(max_length=20, null=True, blank=True)
    chat_id = models.CharField(max_length=50, null=True, blank=True)
