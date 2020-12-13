from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('homepage', views.home),
    path('login', views.login),
    path('register', views.register),
    path('logout', views.logout),
    path('hats', views.create_hat),
    path('hats/<int:hat_id>/update', views.update_hat),
    path('hats/<int:hat_id>', views.show_hat),
    path('hats/<int:hat_id>/edit', views.edit_hat),
    path('hats/<int:hat_id>/delete', views.delete_hat),
    path('hats/new', views.add_hat),
]