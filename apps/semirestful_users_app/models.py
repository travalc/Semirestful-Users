# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = []
        if len(postData['first_name']) < 1:
            errors.append('First name is required')
        if len(postData['last_name']) < 1:
            errors.append('Last name is required')
        if len(postData['email']) < 1:
            errors.append('Email is required')
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()