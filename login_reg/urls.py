from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('successRegister', views.reg_success),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout)
]