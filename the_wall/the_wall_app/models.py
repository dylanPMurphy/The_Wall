from django.db import models
from login_reg.models import *

# Create your models here.

class Message(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    user_who_posted = models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    message_parent = models.ForeignKey(Message, related_name="comments", on_delete = models.CASCADE)
    user_who_commented = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)