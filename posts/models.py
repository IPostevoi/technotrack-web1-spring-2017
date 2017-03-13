from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='published_blogs', null=True)


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    blog = models.ForeignKey('posts.Blog', null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='published_posts', null=True)