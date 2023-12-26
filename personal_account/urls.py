from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import *




urlpatterns = [

    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]