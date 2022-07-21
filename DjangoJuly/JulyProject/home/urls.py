from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('girl', views.home, name='home'),
    path('path', views.path, name='path')
]
