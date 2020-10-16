from __future__ import unicode_literals
from django.db import models

import re
# Create your models here.\
class UserManager(models.Manager):
    def create_validator(self, reqPost):   
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(reqPost['user_name'])<5:
            errors['user_name'] = "Name must be at least 5 characters"
        if len(reqPost['email'])<8:
            errors['email'] = "Email must be at least 8 characters"
        if len(reqPost['password'])<8:
            errors['password'] = "Password must be at least 8 characters"
        if reqPost['password'] != reqPost['confirm_password']:
            errors['confirm_password'] = "Passwords must match"
        if not EMAIL_REGEX.match(reqPost['email']):    # test whether a field matches the pattern            
            errors['email'] = ("Invalid email address!")
        return errors

class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
