from django.urls import path

from users.views import register, login_view, index, ProfileCreate

app_name = 'users'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('index/', index, name='index'),
    path('profile/', ProfileCreate.as_view(), name='profile'),
]