from django.contrib import admin
from django.urls import path
from core.views import *

app_name = 'core'
urlpatterns = [
    path('', index,name="index"),
    path('contact/',contact, name='contact'),
    path('signup/',signup,name='signup' ),
]