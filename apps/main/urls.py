from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('homepage', views.home),
    path('login', views.login),
    path('register', views.register),
    path('logout', views.logout),
]