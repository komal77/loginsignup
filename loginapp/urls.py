from django.contrib import admin
from django.urls import path, include
from .views import *
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Home.as_view() , name='home'),
    path('login/',Login.as_view(), name = 'login'),
    path('Logout/',Logout.as_view(), name = 'logout'),
    path('signup/',Signup.as_view(), name = 'signup'),
]