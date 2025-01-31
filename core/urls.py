from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from core.views import *
from .forms import LoginForm

app_name = 'core'
urlpatterns = [
    path('', index,name="index"),
    path('contact/',contact, name='contact'),
    path('signup/',signup,name='signup' ),
    path('login/',auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login')
]