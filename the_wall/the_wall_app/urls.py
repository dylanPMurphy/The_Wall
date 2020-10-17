from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('/messages/new', views.addNewMessage),
    path('/comments/new', views.addNewComment)

]
