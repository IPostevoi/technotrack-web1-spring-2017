from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from posts.models import Blog, Post



class User(AbstractUser):

    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)



