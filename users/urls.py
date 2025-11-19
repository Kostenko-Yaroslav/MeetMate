from django.urls import path

from users.views import index, RegisterView, LoginView, logout_view, UserProfileView

app_name = 'users'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', logout_view, name='logout'),
    path('index/', index, name='index'),
]